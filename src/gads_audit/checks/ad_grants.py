"""Kontrole zasad Google Ad Grants (tylko konto Fundacja).

Źródła sprawdzone 2026-10-12 (sprawdzaj ponownie przy każdej pracy nad kontem):
- Ad Grants Policy Compliance Guide:
  https://support.google.com/nonprofits/answer/9314402
- Ad Grants account management policy:
  https://support.google.com/grants/answer/117827

Zasady zakodowane poniżej:
- CTR konta >= 5% w każdym miesiącu; 2 kolejne miesiące poniżej = czasowa
  dezaktywacja konta.
- Brak jednowyrazowych słów kluczowych (wyjątki: marka, zatwierdzone schorzenia).
- Słowa kluczowe z Quality Score 1 lub 2 muszą być wstrzymane lub usunięte.
- Co najmniej 2 grupy reklam w kampanii, co najmniej 2 linki do podstron.
- Strategia oparta na konwersjach (Maximize conversions / conversion value,
  Target CPA, Target ROAS), chyba że kampanie inteligentne.
- Co najmniej 1 konwersja miesięcznie przy prawidłowym śledzeniu.
- Właściwe kierowanie geograficzne.
"""

from __future__ import annotations

from ..accounts import AccountProfile
from ..model import AccountSnapshot, Area, Finding, Severity

CTR_MIN = 0.05
CTR_CONSECUTIVE_MONTHS_FOR_DEACTIVATION = 2
LOW_QUALITY_SCORES = {1, 2}
MIN_AD_GROUPS_PER_CAMPAIGN = 2
MIN_SITELINKS = 2
MIN_CONVERSIONS_PER_MONTH = 1
ALLOWED_BIDDING = {
    "MAXIMIZE_CONVERSIONS",
    "MAXIMIZE_CONVERSION_VALUE",
    "TARGET_CPA",
    "TARGET_ROAS",
}
SMART_CHANNEL = "SMART"


def _is_single_word(text: str) -> bool:
    cleaned = text.strip().strip('"[]').replace("+", "")
    return len(cleaned.split()) == 1


def _is_brand(text: str, profile: AccountProfile) -> bool:
    t = text.strip().strip('"[]').lower()
    return any(t == b or t.replace(" ", "") == b.replace(" ", "")
               for b in profile.brand_terms)


def check_account(snapshot: AccountSnapshot, profile: AccountProfile,
                  medical_terms: frozenset[str] = frozenset()) -> list[Finding]:
    """`medical_terms` — jednowyrazowe nazwy schorzeń, które Google dopuszcza
    (lista z Google; uzupełnij ręcznie, jeśli trzeba)."""
    if not profile.is_ad_grants:
        return []
    findings: list[Finding] = []
    acct = f"Konto {profile.name} ({profile.customer_id})"
    active = [c for c in snapshot.campaigns if c.status == "ENABLED"]
    only_smart = bool(active) and all(c.channel == SMART_CHANNEL for c in active)

    # --- CTR miesięczny ---
    if not only_smart and snapshot.monthly_stats:
        streak = 0
        for m in snapshot.monthly_stats:
            streak = streak + 1 if m.impressions and m.ctr < CTR_MIN else 0
        last = snapshot.monthly_stats[-1]
        if streak >= CTR_CONSECUTIVE_MONTHS_FOR_DEACTIVATION:
            findings.append(Finding(
                Severity.ERROR, Area.AD_GRANTS, acct,
                f"CTR poniżej 5% przez {streak} kolejne miesiące "
                f"(ostatnio {last.ctr:.1%} w {last.month}) — ryzyko "
                "dezaktywacji konta.",
                "Wstrzymaj słowa kluczowe z dużą liczbą wyświetleń i niskim "
                "CTR, aż CTR konta wróci do min. 5%.",
            ))
        elif streak == 1:
            findings.append(Finding(
                Severity.WARNING, Area.AD_GRANTS, acct,
                f"CTR {last.ctr:.1%} w {last.month} — poniżej wymaganych 5%.",
                "Popraw CTR w tym miesiącu; drugi miesiąc z rzędu grozi "
                "dezaktywacją.",
            ))

    # --- Konwersje ---
    if snapshot.monthly_stats:
        last = snapshot.monthly_stats[-1]
        if last.conversions < MIN_CONVERSIONS_PER_MONTH:
            findings.append(Finding(
                Severity.ERROR, Area.AD_GRANTS, acct,
                f"{last.conversions:g} konwersji w {last.month} (wymagana "
                "min. 1 miesięcznie).",
                "Sprawdź śledzenie konwersji (np. zapis na grupę, wysłany "
                "formularz kontaktowy) — bez danych o zdrowiu w tagach.",
            ))

    # --- Struktura i ustawienia kampanii ---
    for c in active:
        if c.channel == SMART_CHANNEL:
            continue
        if c.ad_group_count < MIN_AD_GROUPS_PER_CAMPAIGN:
            findings.append(Finding(
                Severity.ERROR, Area.AD_GRANTS, c.name,
                f"{c.ad_group_count} grup reklam (wymagane min. "
                f"{MIN_AD_GROUPS_PER_CAMPAIGN}).",
                "Dodaj drugą grupę ze ściśle powiązanymi słowami, reklamami "
                "i stroną docelową.",
            ))
        if c.bidding_strategy not in ALLOWED_BIDDING:
            findings.append(Finding(
                Severity.ERROR, Area.AD_GRANTS, c.name,
                f"Strategia „{c.bidding_strategy}” nie jest oparta na "
                "konwersjach.",
                "Przełącz na Maksymalizację konwersji lub Docelowy CPA "
                "(Google może zmienić ją automatycznie).",
            ))
        if c.geo_target_count == 0:
            findings.append(Finding(
                Severity.ERROR, Area.AD_GRANTS, c.name,
                "Brak kierowania geograficznego.",
                "Ustaw lokalizacje, w których działają usługi Fundacji.",
            ))

    if snapshot.sitelink_count < MIN_SITELINKS:
        findings.append(Finding(
            Severity.ERROR, Area.AD_GRANTS, acct,
            f"{snapshot.sitelink_count} linków do podstron (wymagane min. "
            f"{MIN_SITELINKS}).",
            "Dodaj co najmniej 2 unikalne linki do podstron yellowscarf.org.",
        ))

    # --- Słowa kluczowe ---
    medical = {t.lower() for t in medical_terms}
    for kw in snapshot.keywords:
        if kw.status != "ENABLED":
            continue
        if (_is_single_word(kw.text) and not _is_brand(kw.text, profile)
                and kw.text.strip().strip('"[]').lower() not in medical):
            findings.append(Finding(
                Severity.ERROR, Area.AD_GRANTS, kw.label,
                "Jednowyrazowe słowo kluczowe — niedozwolone w Ad Grants.",
                "Rozbuduj do frazy (np. „grupa wsparcia online”) albo wstrzymaj.",
            ))
        if kw.quality_score in LOW_QUALITY_SCORES:
            findings.append(Finding(
                Severity.ERROR, Area.AD_GRANTS, kw.label,
                f"Wynik jakości {kw.quality_score}/10 — w Ad Grants musi być "
                "wstrzymane lub usunięte.",
                "Wstrzymaj słowo albo popraw trafność reklamy i strony.",
            ))
    return findings
