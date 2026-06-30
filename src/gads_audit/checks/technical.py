"""Poprawność techniczna RSA: limity znaków, liczba elementów, ścieżki, URL-e."""

from __future__ import annotations

from urllib.parse import urlparse

from .. import rules
from ..model import AdAsset, Area, Finding, ResponsiveSearchAd, Severity


def _too_long(assets: list[AdAsset], limit: int) -> list[AdAsset]:
    return [a for a in assets if len(a.text) > limit]


def check_ad(ad: ResponsiveSearchAd) -> list[Finding]:
    findings: list[Finding] = []
    e = ad.label

    # --- Liczba nagłówków ---
    if len(ad.headlines) < rules.HEADLINES_REQUIRED_MIN:
        findings.append(Finding(
            Severity.ERROR, Area.TECHNICAL, e,
            f"Tylko {len(ad.headlines)} nagłówków (wymagane minimum "
            f"{rules.HEADLINES_REQUIRED_MIN}).",
            f"Dodaj nagłówki do co najmniej {rules.HEADLINES_RECOMMENDED_MIN}, "
            "aby system miał z czego optymalizować.",
        ))
    elif len(ad.headlines) < rules.HEADLINES_RECOMMENDED_MIN:
        findings.append(Finding(
            Severity.WARNING, Area.TECHNICAL, e,
            f"{len(ad.headlines)} nagłówków — poniżej rekomendowanych "
            f"{rules.HEADLINES_RECOMMENDED_MIN}-{rules.HEADLINES_MAX}.",
            "Dodaj więcej unikalnych nagłówków — to bezpośrednio poprawia "
            "Ad Strength i zasięg aukcji.",
        ))

    # --- Liczba opisów ---
    if len(ad.descriptions) < rules.DESCRIPTIONS_REQUIRED_MIN:
        findings.append(Finding(
            Severity.ERROR, Area.TECHNICAL, e,
            f"Tylko {len(ad.descriptions)} opisów (wymagane minimum "
            f"{rules.DESCRIPTIONS_REQUIRED_MIN}).",
            "Uzupełnij opisy do 3-4, różnicując korzyści i CTA.",
        ))
    elif len(ad.descriptions) < rules.DESCRIPTIONS_RECOMMENDED_MIN:
        findings.append(Finding(
            Severity.WARNING, Area.TECHNICAL, e,
            f"{len(ad.descriptions)} opisy — rekomendowane "
            f"{rules.DESCRIPTIONS_RECOMMENDED_MIN}-{rules.DESCRIPTIONS_MAX}.",
            "Dodaj kolejny opis z inną korzyścią lub dowodem (social proof).",
        ))

    # --- Limity długości ---
    for a in _too_long(ad.headlines, rules.HEADLINE_MAX_CHARS):
        findings.append(Finding(
            Severity.ERROR, Area.TECHNICAL, e,
            f"Nagłówek przekracza {rules.HEADLINE_MAX_CHARS} zn. "
            f"({len(a.text)}): „{a.text}”.",
            "Skróć nagłówek — nadmiar nie wyświetli się i blokuje zapis.",
        ))
    for a in _too_long(ad.descriptions, rules.DESCRIPTION_MAX_CHARS):
        findings.append(Finding(
            Severity.ERROR, Area.TECHNICAL, e,
            f"Opis przekracza {rules.DESCRIPTION_MAX_CHARS} zn. "
            f"({len(a.text)}): „{a.text[:60]}…”.",
            "Skróć opis do limitu.",
        ))

    # --- Ścieżki wyświetlane (paths) ---
    for name, path in (("Path1", ad.path1), ("Path2", ad.path2)):
        if path and len(path) > rules.PATH_MAX_CHARS:
            findings.append(Finding(
                Severity.ERROR, Area.TECHNICAL, e,
                f"{name} przekracza {rules.PATH_MAX_CHARS} zn. ({len(path)}): "
                f"„{path}”.",
                "Skróć ścieżkę wyświetlaną.",
            ))

    # --- Finalny URL ---
    if not ad.final_urls:
        findings.append(Finding(
            Severity.ERROR, Area.TECHNICAL, e,
            "Brak finalnego URL-a.",
            "Ustaw poprawny, działający final URL (https).",
        ))
    else:
        for url in ad.final_urls:
            parsed = urlparse(url)
            if parsed.scheme not in ("http", "https") or not parsed.netloc:
                findings.append(Finding(
                    Severity.ERROR, Area.TECHNICAL, e,
                    f"Niepoprawny finalny URL: „{url}”.",
                    "Podaj pełny adres z http(s):// i domeną.",
                ))
            elif parsed.scheme == "http":
                findings.append(Finding(
                    Severity.WARNING, Area.TECHNICAL, e,
                    f"Finalny URL używa HTTP zamiast HTTPS: „{url}”.",
                    "Przełącz stronę docelową na HTTPS.",
                ))

    # --- Duplikaty nagłówków (zjadają miejsce w rotacji) ---
    texts = [h.text.strip().lower() for h in ad.headlines]
    dupes = {t for t in texts if texts.count(t) > 1 and t}
    if dupes:
        findings.append(Finding(
            Severity.WARNING, Area.TECHNICAL, e,
            f"Zduplikowane nagłówki: {', '.join(sorted(dupes))}.",
            "Zastąp duplikaty unikalnymi wariantami — duplikaty marnują sloty.",
        ))

    return findings
