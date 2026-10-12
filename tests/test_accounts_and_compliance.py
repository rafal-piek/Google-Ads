import pytest

from gads_audit.accounts import FUNDACJA, MENTAL, OSRODEK, get_profile
from gads_audit.audit import AccountMismatchError, run_audit
from gads_audit.checks import ad_grants, compliance
from gads_audit.model import (AccountSnapshot, AdAsset, Area, CampaignInfo,
                              KeywordInfo, MonthlyStats, ResponsiveSearchAd,
                              Severity)


def make_ad(headlines, descriptions, url):
    return ResponsiveSearchAd(
        ad_id=1, campaign="C", ad_group="G", status="ENABLED",
        headlines=[AdAsset(t) for t in headlines],
        descriptions=[AdAsset(t) for t in descriptions],
        final_urls=[url],
    )


def messages(findings, area=None, severity=None):
    return [f.message for f in findings
            if (area is None or f.area == area)
            and (severity is None or f.severity == severity)]


def test_get_profile_by_key_and_id():
    assert get_profile("Osrodek") is OSRODEK
    assert get_profile("7985772656") is FUNDACJA
    assert get_profile("311-878-5541") is MENTAL
    with pytest.raises(KeyError):
        get_profile("123-456-7890")


def test_only_fundacja_is_ad_grants():
    assert FUNDACJA.is_ad_grants
    assert not OSRODEK.is_ad_grants and not MENTAL.is_ad_grants
    assert OSRODEK.legal_entity == MENTAL.legal_entity == "YELLOW SCARF CIC"
    assert FUNDACJA.legal_entity == "Yellow Scarf CIO"


def test_domain_from_other_account_is_error():
    ad = make_ad(["Terapia online"], ["Opis"], "https://www.osrodek.uk/kontakt")
    f = compliance.check_ad(ad, MENTAL)
    errs = messages(f, Area.ACCOUNT_MATCH, Severity.ERROR)
    assert any("Osrodek" in m for m in errs)
    assert not messages(compliance.check_ad(ad, OSRODEK), Area.ACCOUNT_MATCH)


def test_polish_forbidden_phrases():
    ad = make_ad(["Gwarantujemy poprawę", "Nie czekaj!"],
                 ["Masz depresję? Pozbądź się jej raz na zawsze."],
                 "https://osrodek.uk")
    f = compliance.check_ad(ad, OSRODEK)
    pol = messages(f, Area.POLICY)
    for needle in ("Gwarant", "Nie czekaj", "Masz depresj", "Pozbądź się",
                   "raz na zawsze"):
        assert any(needle in m for m in pol), needle


def test_english_forbidden_and_spelling():
    ad = make_ad(["Best Therapy in the UK", "Guaranteed Results"],
                 ["Counseling that will fix your life. Book now."],
                 "https://www.yellowscarftherapy.co.uk/")
    f = compliance.check_ad(ad, MENTAL)
    pol = messages(f, Area.POLICY)
    assert any("Guarantee" in m for m in pol)
    assert any("fix your" in m for m in pol)
    assert any("Best Therapy" in m for m in pol)
    assert any("counseling" in m for m in messages(f, Area.COPYWRITING))


def test_calm_therapy_ad_passes_cleanly():
    ad = make_ad(
        ["Online Therapy Across the UK", "Talk to a Qualified Therapist"],
        ["You do not need to have everything figured out before reaching "
         "out. Book a consultation."],
        "https://www.yellowscarftherapy.co.uk/contact")
    assert compliance.check_ad(ad, MENTAL) == []


def test_missing_cta_warns():
    ad = make_ad(["Terapia online po polsku"], ["Spokojna przestrzeń."],
                 "https://osrodek.uk")
    assert any("CTA" in m for m in messages(compliance.check_ad(ad, OSRODEK)))


def test_polish_text_in_mental_is_flagged():
    ad = make_ad(["Terapia dla Ciebie"], ["Umów konsultację — zadzwoń."],
                 "https://yellowscarftherapy.co.uk")
    assert any("Polskie znaki" in m
               for m in messages(compliance.check_ad(ad, MENTAL)))


def grants_snapshot(**kw):
    base = dict(
        customer_id="798-577-2656",
        campaigns=[CampaignInfo("Grupy", bidding_strategy="MAXIMIZE_CONVERSIONS",
                                ad_group_count=2, geo_target_count=1)],
        keywords=[KeywordInfo("Grupy", "G", "grupa wsparcia online",
                              quality_score=7)],
        sitelink_count=2,
        monthly_stats=[MonthlyStats("2026-09", 1000, 80, 3)],
    )
    base.update(kw)
    return AccountSnapshot(**base)


def test_compliant_grants_account_has_no_findings():
    assert ad_grants.check_account(grants_snapshot(), FUNDACJA) == []


def test_grants_rules_violations():
    snap = grants_snapshot(
        campaigns=[CampaignInfo("Grupy", bidding_strategy="MAXIMIZE_CLICKS",
                                ad_group_count=1, geo_target_count=0)],
        keywords=[KeywordInfo("Grupy", "G", "terapia"),
                  KeywordInfo("Grupy", "G", "yellowscarf"),
                  KeywordInfo("Grupy", "G", "terapia grupowa online",
                              quality_score=2)],
        sitelink_count=1,
        monthly_stats=[MonthlyStats("2026-08", 1000, 30, 1),
                       MonthlyStats("2026-09", 1000, 40, 0)],
    )
    msgs = messages(ad_grants.check_account(snap, FUNDACJA), Area.AD_GRANTS,
                    Severity.ERROR)
    joined = " | ".join(msgs)
    for needle in ("2 kolejne miesiące", "konwersji", "grup reklam",
                   "MAXIMIZE_CLICKS", "geograficznego", "linków do podstron",
                   "Jednowyrazowe", "Wynik jakości 2"):
        assert needle in joined, needle
    # słowo marki jest dozwolone jako jednowyrazowe
    assert sum("Jednowyrazowe" in m for m in msgs) == 1


def test_grants_rules_not_applied_to_commercial_accounts():
    snap = grants_snapshot(customer_id="733-094-4080", sitelink_count=0)
    assert ad_grants.check_account(snap, OSRODEK) == []


def test_run_audit_refuses_snapshot_from_other_account():
    with pytest.raises(AccountMismatchError):
        run_audit("fundacja", [], grants_snapshot(customer_id="311-878-5541"))
