# Pakiet kontekstowy dla drugiego agenta (Codex / ChatGPT)

> Cel tego dokumentu: dać drugiemu agentowi AI pełny kontekst projektu **Google-Ads**,
> aby mógł pracować równolegle z Claude Code jako „druga para oczu" — wychwytywać
> pomysły na reklamy i dawać niezależną drugą opinię o kontach Google Ads.
>
> Dokument jest samowystarczalny: zawiera opis projektu, pełny kod źródłowy
> i zasady współpracy. Można go wkleić w całości jako kontekst startowy.

---

## 1. Stan faktyczny — co ten projekt zawiera, a czego NIE zawiera

**Zawiera:**
- Szkielet narzędzia audytowego w Pythonie (`gads_audit`) do sprawdzania reklam
  RSA (Responsive Search Ads) pod kątem poprawności technicznej, polityk Google
  i skuteczności copywritingu.
- Zestaw reguł i progów audytu (limity znaków, liczba nagłówków, heurystyki
  polityk, sygnały CTA itd.) — sekcja 4.
- Przykładowy plik konfiguracyjny `google-ads.yaml.example` (bez prawdziwych danych).

**NIE zawiera (stan na 2026-07-13):**
- Żadnych identyfikatorów rzeczywistych kont Google Ads (customer ID, MCC).
- Żadnych danych kampanii, grup reklam ani reklam z prawdziwych kont.
- Żadnych poświadczeń: developer token, OAuth client, refresh token — te są
  celowo poza repozytorium (`.gitignore`).
- Kodu pobierającego dane z Google Ads API (fetcher jeszcze nie powstał).

**⚠️ Zasada bezpieczeństwa (obowiązuje też drugiego agenta):** poświadczeń
(google-ads.yaml, client_secret*.json, refresh tokeny, .env) nigdy nie wkleja się
do czatów, promptów ani repozytorium. Drugi agent nie potrzebuje dostępu do API —
pracuje na eksportach/raportach (sekcja 6).

## 2. Właściciel i konwencje

- Właściciel: Rafał (rafal@yellowscarf.org), komunikacja **po polsku**.
- Kod, nazwy zmiennych: po angielsku; komentarze i komunikaty audytu: po polsku.
- Repozytorium: `rafal-piek/Google-Ads` (GitHub). Wszystko warte zachowania musi
  być zacommitowane i wypchnięte (sesje działają w tymczasowych kontenerach).
- Python 3.11+, zależność: `google-ads>=25.0.0`.

## 3. Struktura repozytorium

```
Google-Ads/
├── CLAUDE.md                  # kontekst projektu dla Claude Code
├── google-ads.yaml.example    # szablon konfiguracji API (bez sekretów)
├── requirements.txt           # google-ads>=25.0.0
├── src/gads_audit/
│   ├── __init__.py
│   ├── model.py               # modele danych: ResponsiveSearchAd, Finding, ...
│   ├── rules.py               # stałe i progi audytu
│   └── checks/
│       ├── __init__.py
│       └── technical.py       # kontrole techniczne RSA
├── docs/EXPORT-DLA-CODEX.md   # ten dokument
└── dieta/                     # prywatne pliki właściciela, poza zakresem projektu
```

## 4. Wiedza domenowa zakodowana w projekcie (progi audytu)

Twarde limity RSA (łamią zapis/wyświetlanie reklamy):

| Parametr | Limit |
|---|---|
| Długość nagłówka | 30 znaków |
| Długość opisu | 90 znaków |
| Długość ścieżki (path1/path2) | 15 znaków |
| Nagłówki min–max | 3–15 |
| Opisy min–max | 2–4 |

Dobre praktyki (WARNING/INFO w audycie):

| Praktyka | Próg |
|---|---|
| Rekomendowana liczba nagłówków | ≥8 (cel: mocny Ad Strength) |
| Rekomendowana liczba opisów | ≥3 |
| Maks. przypięte nagłówki | 2 (nadmiar obniża Ad Strength) |
| Maks. przypięte opisy | 1 |
| Min. aktywnych RSA w grupie reklam | 1 (rekomendowane 2) |
| Maks. słów kluczowych w grupie | 20 (powyżej — podzielić grupę) |

Heurystyki jakości/polityk:
- Nadmierna interpunkcja: `!!`, `??`, `?!`, `!?`, `...`
- „Krzykliwe" symbole: ™ ® © ★ ✓ ✔ » « • → ▶
- Numer telefonu w treści reklamy = naruszenie polityk (od tego są rozszerzenia).
- Superlatywy wymagające dowodu na stronie: najlepszy, nr 1, #1, lider,
  najtańszy, gwarantowany / best, number one, cheapest, guaranteed.
- Reklama powinna zawierać CTA (kup, zamów, sprawdź, zobacz… / buy, order,
  shop, get, try…) oraz „konkret" (cena, %, rabat, promocja, free/gratis).

Obszary audytu (enum `Area`): Poprawność techniczna, Zgodność z politykami,
Skuteczność/copywriting, Struktura konta.
Poziomy (enum `Severity`): ERROR (blokuje), WARNING (zła praktyka), INFO (sugestia).

## 5. Pełny kod źródłowy

### 5.1 `google-ads.yaml.example`

```yaml
# Skopiuj ten plik do `google-ads.yaml` i uzupełnij swoimi danymi.
# UWAGA: `google-ads.yaml` jest w .gitignore — NIGDY nie commituj prawdziwych poświadczeń.
#
# Skąd wziąć poszczególne wartości:
#   developer_token   -> Google Ads (konto MCC) > Tools > API Center
#   client_id         -> Google Cloud Console > APIs & Services > Credentials (OAuth client)
#   client_secret     -> jw.
#   refresh_token     -> wygeneruj raz lokalnie (patrz README, sekcja "Refresh token")
#   login_customer_id -> ID konta MCC (bez myślników), jeśli logujesz się przez managera

developer_token: "INSERT_DEVELOPER_TOKEN"
client_id: "INSERT_OAUTH_CLIENT_ID"
client_secret: "INSERT_OAUTH_CLIENT_SECRET"
refresh_token: "INSERT_REFRESH_TOKEN"

# Tylko jeśli korzystasz z konta menedżerskiego (MCC). Bez myślników, np. 1234567890
# login_customer_id: "1234567890"

use_proto_plus: True
```

### 5.2 `src/gads_audit/model.py`

```python
"""Modele danych: ujednolicony kształt reklam/grup oraz wynik audytu (Finding).

Dzięki temu reguły audytu działają na zwykłych obiektach Pythona i są w pełni
testowalne bez połączenia z API.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Severity(str, Enum):
    ERROR = "ERROR"      # łamie wymóg / blokuje wyświetlanie
    WARNING = "WARNING"  # niezgodne z dobrą praktyką, ogranicza skuteczność
    INFO = "INFO"        # sugestia optymalizacyjna


class Area(str, Enum):
    TECHNICAL = "Poprawność techniczna"
    POLICY = "Zgodność z politykami"
    COPYWRITING = "Skuteczność / copywriting"
    STRUCTURE = "Struktura konta"


@dataclass
class Finding:
    severity: Severity
    area: Area
    entity: str            # np. "Kampania > Grupa > Reklama #123"
    message: str           # co jest nie tak
    recommendation: str    # co z tym zrobić

    def to_dict(self) -> dict:
        return {
            "severity": self.severity.value,
            "area": self.area.value,
            "entity": self.entity,
            "message": self.message,
            "recommendation": self.recommendation,
        }


@dataclass
class AdAsset:
    """Pojedynczy nagłówek lub opis RSA (z opcjonalnym przypięciem)."""
    text: str
    pinned_field: Optional[str] = None  # np. HEADLINE_1, DESCRIPTION_1 lub None


@dataclass
class ResponsiveSearchAd:
    ad_id: int
    campaign: str
    ad_group: str
    status: str                         # ENABLED / PAUSED / REMOVED
    headlines: list[AdAsset] = field(default_factory=list)
    descriptions: list[AdAsset] = field(default_factory=list)
    path1: str = ""
    path2: str = ""
    final_urls: list[str] = field(default_factory=list)
    ad_strength: str = "UNKNOWN"        # POOR / AVERAGE / GOOD / EXCELLENT
    approval_status: str = "UNKNOWN"    # APPROVED / DISAPPROVED / ...
    policy_topics: list[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        return f"{self.campaign} > {self.ad_group} > Reklama #{self.ad_id}"


@dataclass
class AdGroupInfo:
    campaign: str
    ad_group: str
    status: str
    rsa_count: int = 0
    keyword_count: int = 0
    broad_keyword_count: int = 0

    @property
    def label(self) -> str:
        return f"{self.campaign} > {self.ad_group}"
```

### 5.3 `src/gads_audit/rules.py`

```python
"""Stałe i progi audytu — oparte na oficjalnych limitach Google Ads oraz
sprawdzonych dobrych praktykach (stan na 2024/2025).

Trzymamy je w jednym miejscu, żeby łatwo aktualizować, gdy Google zmieni limity.
"""

# --- Twarde limity RSA (Responsive Search Ads) ---
HEADLINE_MAX_CHARS = 30
DESCRIPTION_MAX_CHARS = 90
PATH_MAX_CHARS = 15

HEADLINES_REQUIRED_MIN = 3      # mniej = reklama nie zostanie utworzona
HEADLINES_MAX = 15
DESCRIPTIONS_REQUIRED_MIN = 2
DESCRIPTIONS_MAX = 4

# --- Progi dobrych praktyk (rekomendacje, nie twarde wymogi) ---
HEADLINES_RECOMMENDED_MIN = 8  # do mocnego Ad Strength Google rekomenduje ~8-15
DESCRIPTIONS_RECOMMENDED_MIN = 3
MAX_PINNED_HEADLINES = 2       # nadmierne przypinanie obniża Ad Strength
MAX_PINNED_DESCRIPTIONS = 1

# Struktura konta
MIN_RSA_PER_AD_GROUP = 1       # przynajmniej 1 aktywna RSA w grupie
RECOMMENDED_RSA_PER_AD_GROUP = 2
MAX_KEYWORDS_PER_AD_GROUP = 20  # powyżej rozważ podział grupy (lepsza trafność)

# --- Heurystyki polityk / jakości tekstu ---
# Powtórzona interpunkcja (np. "!!!", "???", "...!") i „krzykliwe" symbole.
EXCESSIVE_PUNCTUATION = ["!!", "??", "?!", "!?", "..."]
GIMMICKY_SYMBOLS = ["™", "®", "©", "★", "✓", "✔", "»", "«", "•", "→", "▶"]

# Numer telefonu w treści reklamy jest niezgodny z politykami (od tego są
# rozszerzenia połączeń / lokalizacji).
PHONE_PATTERN = r"(?:(?:\+?\d[\s\-]?){9,})"

# Superlatywy/roszczenia, które Google ogranicza, jeśli nie są poparte
# niezależnym, widocznym na stronie źródłem (np. ranking).
SUPERLATIVES = [
    # PL
    "najlepszy", "najlepsza", "najlepsze", "numer 1", "nr 1", "nr.1",
    "#1", "lider", "najtańszy", "najtańsza", "najtańsze", "gwarantowany",
    # EN
    "best", "number one", "#1", "cheapest", "guaranteed",
]

# Sygnały wezwania do działania (CTA) — sprawdzamy, czy reklama je zawiera.
CTA_SIGNALS = [
    # PL
    "kup", "zamów", "sprawdź", "zobacz", "odkryj", "wypróbuj", "pobierz",
    "zapisz się", "zarezerwuj", "umów", "skorzystaj", "dołącz", "zadzwoń",
    "poznaj", "wybierz", "zacznij",
    # EN
    "buy", "order", "shop", "get", "try", "discover", "download",
    "sign up", "book", "start", "learn more", "subscribe", "join", "save",
]

# Sygnały „konkretu" (liczby, ceny, promocje) — podnoszą skuteczność.
import re  # noqa: E402

OFFER_PATTERN = re.compile(
    r"(\d+\s?%|\d+\s?(zł|pln|eur|usd|\$|€)|promocj|rabat|zniżk|gratis|"
    r"darmow|sale|discount|free|off\b)",
    re.IGNORECASE,
)
```

### 5.4 `src/gads_audit/checks/technical.py`

```python
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
```

## 6. Proponowany model współpracy dwóch agentów

Rola drugiego agenta (Codex): **niezależny recenzent i generator pomysłów** —
świadomie NIE ma dostępu do API ani poświadczeń.

1. **Wejście dla Codexa:** eksporty przygotowane przez Claude/właściciela —
   np. lista reklam w formacie JSON zgodnym z modelem `ResponsiveSearchAd`
   (sekcja 5.2) albo raporty `Finding[]` (`to_dict()` → JSON). Eksporty NIE
   zawierają poświadczeń; identyfikatory kont można zanonimizować.
2. **Zadania Codexa:**
   - druga opinia o wynikach audytu (czy rekomendacje są trafne, czego brakuje),
   - propozycje nowych nagłówków/opisów RSA (limity: 30/90 znaków!),
   - pomysły na kampanie, słowa kluczowe, rozszerzenia, testy A/B,
   - wychwytywanie problemów, których reguły z sekcji 4 nie łapią.
3. **Wyjście Codexa:** uwagi w formacie zgodnym z `Finding`
   (severity / area / entity / message / recommendation) — dzięki temu obie
   „pary oczu" mówią tym samym językiem i wyniki da się scalić.
4. **Kanał wymiany:** pliki markdown/JSON w repozytorium (np. katalog
   `reviews/` — do utworzenia), commitowane przez właściciela.

## 7. Czego drugiemu agentowi NIE wolno

- Prosić o poświadczenia API, refresh tokeny, client secret — i ich przechowywać.
- Wprowadzać zmian bezpośrednio na kontach Google Ads (rola jest wyłącznie
  doradcza; zmiany wdraża właściciel lub Claude po akceptacji właściciela).
- Zakładać, że dane, których nie widzi, nie istnieją — jeśli czegoś brakuje
  w eksporcie, ma o to poprosić właściciela.
