"""Kontrole reklam zależne od profilu konta: domena, język, CTA i zakazane
sformułowania w usługach terapeutycznych."""

from __future__ import annotations

import re
from urllib.parse import urlparse

from .. import rules
from .. import therapy_vocab as vocab
from ..accounts import AccountProfile, profile_for_domain
from ..model import Area, Finding, ResponsiveSearchAd, Severity

_PHONE = re.compile(rules.PHONE_PATTERN)


def _ad_texts(ad: ResponsiveSearchAd) -> list[str]:
    return [a.text for a in ad.headlines + ad.descriptions]


def _check_domain(ad: ResponsiveSearchAd, profile: AccountProfile) -> list[Finding]:
    findings: list[Finding] = []
    for url in ad.final_urls:
        host = urlparse(url).netloc
        if not host:
            continue  # niepoprawny URL zgłasza checks.technical
        owner = profile_for_domain(host)
        if owner is profile:
            continue
        if owner is not None:
            findings.append(Finding(
                Severity.ERROR, Area.ACCOUNT_MATCH, ad.label,
                f"Finalny URL „{url}” należy do konta {owner.name} "
                f"({owner.domain}), a audytujemy konto {profile.name} "
                f"({profile.domain}).",
                f"Pomieszanie kont: reklama w {profile.name} może prowadzić "
                f"tylko na {profile.domain}. Przenieś ją do właściwego konta "
                "albo zmień URL.",
            ))
        else:
            findings.append(Finding(
                Severity.ERROR, Area.ACCOUNT_MATCH, ad.label,
                f"Finalny URL „{url}” jest poza domeną konta "
                f"({profile.domain}).",
                f"Ustaw stronę docelową w domenie {profile.domain}.",
            ))
    return findings


def _check_forbidden(ad: ResponsiveSearchAd, profile: AccountProfile) -> list[Finding]:
    findings: list[Finding] = []
    for text in _ad_texts(ad):
        for rule in profile.forbidden_rules:
            m = rule.compiled().search(text)
            if m:
                findings.append(Finding(
                    rule.severity, Area.POLICY, ad.label,
                    f"„{m.group(0)}” w tekście „{text}”. {rule.reason}",
                    rule.suggestion,
                ))
    return findings


def _check_editorial(ad: ResponsiveSearchAd) -> list[Finding]:
    findings: list[Finding] = []
    for text in _ad_texts(ad):
        if _PHONE.search(text):
            findings.append(Finding(
                Severity.ERROR, Area.POLICY, ad.label,
                f"Numer telefonu w treści reklamy: „{text}”.",
                "Przenieś numer do komponentu z numerem telefonu (call asset).",
            ))
        if any(p in text for p in rules.EXCESSIVE_PUNCTUATION):
            findings.append(Finding(
                Severity.WARNING, Area.POLICY, ad.label,
                f"Nadmierna interpunkcja: „{text}”.",
                "Usuń powtórzone znaki — to łamie standardy redakcyjne.",
            ))
        symbols = [s for s in rules.GIMMICKY_SYMBOLS if s in text]
        if symbols:
            findings.append(Finding(
                Severity.WARNING, Area.POLICY, ad.label,
                f"Symbole {' '.join(symbols)} w tekście: „{text}”.",
                "Usuń symbole ozdobne.",
            ))
    return findings


def _check_cta(ad: ResponsiveSearchAd, profile: AccountProfile) -> list[Finding]:
    joined = " ".join(_ad_texts(ad)).lower()
    for phrase in profile.cta_phrases:
        if re.search(r"(?<!\w)" + re.escape(phrase.lower()), joined):
            return []
    examples = ", ".join(f"„{p}”" for p in profile.cta_phrases[:4])
    return [Finding(
        Severity.WARNING, Area.COPYWRITING, ad.label,
        "Brak spokojnego wezwania do pierwszego kroku (CTA).",
        f"Dodaj CTA bez presji, np. {examples}.",
    )]


def _check_language(ad: ResponsiveSearchAd, profile: AccountProfile) -> list[Finding]:
    if profile.language != "en-GB":
        return []
    findings: list[Finding] = []
    for text in _ad_texts(ad):
        if vocab.POLISH_DIACRITICS.search(text):
            findings.append(Finding(
                Severity.WARNING, Area.ACCOUNT_MATCH, ad.label,
                f"Polskie znaki w reklamie anglojęzycznego konta: „{text}”.",
                "Konto Mental jest dla klientów brytyjskich — tekst po "
                "angielsku (en-GB).",
            ))
        for us, uk in vocab.US_TO_UK_SPELLING.items():
            if re.search(rf"(?<!\w){us}(?!\w)", text, re.IGNORECASE):
                findings.append(Finding(
                    Severity.WARNING, Area.COPYWRITING, ad.label,
                    f"Pisownia amerykańska „{us}” w „{text}”.",
                    f"Użyj brytyjskiej: „{uk}”.",
                ))
    return findings


def check_ad(ad: ResponsiveSearchAd, profile: AccountProfile) -> list[Finding]:
    return (
        _check_domain(ad, profile)
        + _check_forbidden(ad, profile)
        + _check_editorial(ad)
        + _check_cta(ad, profile)
        + _check_language(ad, profile)
    )
