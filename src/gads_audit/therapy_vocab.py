"""Słowniki dla reklam usług terapeutycznych (zamiast słowników e-commerce).

Dwa rodzaje list:

* CTA — spokojne wezwania do pierwszego kroku (konsultacja, kontakt, grupa),
  bez presji sprzedażowej.
* Zakazane / ryzykowne sformułowania — obietnice leczenia, gwarancje efektów,
  presja czasu, język zawstydzający i diagnozowanie odbiorcy.

Uzasadnienie: polityki Google Ads dot. treści wprowadzających w błąd
i usług zdrowotnych (stan sprawdzony 2026-10-12) oraz zasady komunikacji
terapeutycznej Yellow Scarf. Wzorce są wyrażeniami regularnymi dopasowywanymi
od początku słowa, bez rozróżniania wielkości liter — dzięki temu łapią polską
odmianę („gwarant” → gwarancja, gwarantujemy, gwarantowany).
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .model import Severity


@dataclass(frozen=True)
class PhraseRule:
    pattern: str        # regex dopasowywany od początku słowa
    severity: Severity
    reason: str         # dlaczego to problem (do komunikatu audytu)
    suggestion: str     # czym zastąpić

    def compiled(self) -> re.Pattern[str]:
        return re.compile(r"(?<!\w)" + self.pattern, re.IGNORECASE)


# --- Kategorie powodów (wspólne komunikaty) ---
_PROMISE = "Obietnica efektu terapii lub wyleczenia — ryzyko odrzucenia " \
           "(treści wprowadzające w błąd) i niezgodne z etyką komunikacji."
_PRESSURE = "Presja czasu lub sprzedażowa — w usługach zdrowia psychicznego " \
            "zniechęca i podważa zaufanie."
_DIAGNOSIS = "Diagnozowanie lub zawstydzanie odbiorcy — reklama nie może " \
             "przypisywać osobie stanu psychicznego."
_SUPERLATIVE = "Niepotwierdzony superlatyw — Google wymaga niezależnego " \
               "źródła widocznego na stronie."


# ---------------------------------------------------------------------------
# PL
# ---------------------------------------------------------------------------

CTA_PL_THERAPY = [
    "umów konsultację", "umów się", "umów", "zarezerwuj", "skontaktuj się",
    "napisz do nas", "napisz", "porozmawiaj", "sprawdź terminy",
    "sprawdź dostępne terminy", "poznaj terapeutów", "poznaj zespół",
    "dowiedz się więcej", "zadzwoń", "wypełnij formularz", "zapytaj",
    "zrób pierwszy krok",
]

# Dodatkowe CTA dla działań społecznych i grupowych (Fundacja).
CTA_PL_COMMUNITY = [
    "dołącz do grupy", "dołącz", "zapisz się", "zgłoś się", "weź udział",
    "sprawdź grupy", "sprawdź warsztaty", "przyjdź", "wesprzyj",
]

FORBIDDEN_PL = [
    # Obietnice / gwarancje
    PhraseRule(r"gwarant", Severity.ERROR, _PROMISE,
               "Opisz, co oferujecie („bezpieczna przestrzeń do rozmowy”), "
               "a nie jaki będzie efekt."),
    PhraseRule(r"(wylecz|ulecz|wyleczeni)", Severity.ERROR, _PROMISE,
               "Usuń obietnicę wyleczenia."),
    PhraseRule(r"100\s?%", Severity.ERROR, _PROMISE,
               "Usuń deklarację skuteczności procentowej."),
    PhraseRule(r"(pewny|pewne|pewna) (efekt|rezultat|popraw)", Severity.ERROR,
               _PROMISE, "Usuń zapewnienie o efekcie."),
    PhraseRule(r"skuteczn\w* (terapi|metod|leczeni)", Severity.WARNING,
               _PROMISE, "Zamiast „skuteczna terapia” napisz o podejściu "
               "lub kwalifikacjach terapeutów."),
    PhraseRule(r"(pozbądź|pozbadz) się", Severity.ERROR, _PROMISE,
               "Zamiast „pozbądź się lęku” — „porozmawiaj o tym, co czujesz”."),
    PhraseRule(r"napraw (swoje )?życie", Severity.ERROR, _PROMISE,
               "Usuń komunikat o „naprawianiu życia”."),
    PhraseRule(r"zmień (swoje )?życie", Severity.WARNING, _PROMISE,
               "Złagodź: „zacznij rozumieć, co się dzieje”."),
    PhraseRule(r"cud(own|em\b|ami\b)", Severity.ERROR, _PROMISE, "Usuń „cudowne” efekty."),
    PhraseRule(r"(raz na zawsze|trwale)", Severity.ERROR, _PROMISE,
               "Usuń zapewnienie o trwałym efekcie."),
    PhraseRule(r"bez leków", Severity.WARNING, _PROMISE,
               "Nie zestawiaj terapii z leczeniem farmakologicznym w reklamie."),
    # Presja
    PhraseRule(r"natychmiast", Severity.WARNING, _PRESSURE,
               "Usuń presję czasu."),
    PhraseRule(r"(tylko|wyłącznie) dziś", Severity.WARNING, _PRESSURE,
               "Usuń presję czasu."),
    PhraseRule(r"ostatni(e|a)? (miejsc|termin|szans)", Severity.WARNING,
               _PRESSURE, "Zamiast tego: „sprawdź dostępne terminy”."),
    PhraseRule(r"nie czekaj", Severity.WARNING, _PRESSURE,
               "Zamiast tego: „gdy poczujesz, że to dobry moment”."),
    PhraseRule(r"(zanim|nim) będzie za późno", Severity.ERROR, _PRESSURE,
               "Usuń straszenie konsekwencjami."),
    PhraseRule(r"już dziś", Severity.INFO, _PRESSURE,
               "Rozważ łagodniejsze sformułowanie bez presji."),
    # Diagnozowanie / zawstydzanie
    PhraseRule(r"(masz|cierpisz na|chorujesz na) (depresj|nerwic|lęk|"
               r"zaburzeni|uzależnieni|traum)", Severity.WARNING, _DIAGNOSIS,
               "Pisz o doświadczeniu, nie o diagnozie: „Możesz czuć się "
               "przytłoczony/a…”."),
    PhraseRule(r"jesteś (uzależnion|chor|zaburzon|słab)", Severity.WARNING,
               _DIAGNOSIS, "Usuń przypisywanie stanu odbiorcy."),
    PhraseRule(r"(wstyd|weź się w garść|ogarnij się)", Severity.WARNING,
               _DIAGNOSIS, "Usuń język zawstydzający."),
    # Superlatywy
    PhraseRule(r"najlepsz", Severity.WARNING, _SUPERLATIVE,
               "Usuń „najlepszy” albo podaj weryfikowalne źródło."),
    PhraseRule(r"(numer|nr\.?) ?1(?!\d)", Severity.WARNING, _SUPERLATIVE,
               "Usuń „nr 1”."),
]


# ---------------------------------------------------------------------------
# EN (brytyjski angielski)
# ---------------------------------------------------------------------------

CTA_EN_GB_THERAPY = [
    "book a consultation", "book an initial consultation", "book",
    "arrange a call", "arrange", "get in touch", "contact us", "speak to",
    "talk to", "find out more", "learn more", "meet our therapists",
    "see availability", "check availability", "request a call", "enquire",
    "make an enquiry", "reach out", "take the first step",
]

FORBIDDEN_EN = [
    # Promises / guarantees
    PhraseRule(r"guarantee", Severity.ERROR, _PROMISE,
               "Describe what you offer (a confidential space to talk), "
               "not the outcome."),
    PhraseRule(r"(cure|cured|cures)\b", Severity.ERROR, _PROMISE,
               "Remove the promise of a cure."),
    PhraseRule(r"100\s?%", Severity.ERROR, _PROMISE,
               "Remove percentage effectiveness claims."),
    PhraseRule(r"(fix|transform) (your|yourself)", Severity.ERROR, _PROMISE,
               "Avoid 'fix your life' / 'transform yourself'."),
    PhraseRule(r"miracle", Severity.ERROR, _PROMISE, "Remove 'miracle'."),
    PhraseRule(r"(proven|permanent|lasting|instant) results?", Severity.ERROR,
               _PROMISE, "Remove claims about results."),
    PhraseRule(r"get rid of", Severity.ERROR, _PROMISE,
               "Try 'talk about what you are going through' instead."),
    PhraseRule(r"(beat|overcome|end) (your )?(anxiety|depression|addiction)",
               Severity.WARNING, _PROMISE,
               "Soften: 'begin to understand what is happening'."),
    PhraseRule(r"without medication", Severity.WARNING, _PROMISE,
               "Do not contrast therapy with medication in ads."),
    # Pressure
    PhraseRule(r"instantly", Severity.WARNING, _PRESSURE,
               "Remove time pressure."),
    PhraseRule(r"(today only|only today|act now|hurry)", Severity.WARNING,
               _PRESSURE, "Remove time pressure."),
    PhraseRule(r"(last|final) (chance|spaces?|slots?)", Severity.WARNING,
               _PRESSURE, "Use 'see availability' instead."),
    PhraseRule(r"before it'?s too late|before it is too late", Severity.ERROR,
               _PRESSURE, "Remove fear-based messaging."),
    PhraseRule(r"don'?t wait|do not wait", Severity.WARNING, _PRESSURE,
               "Try 'whenever you feel ready'."),
    # Diagnosing / shaming
    PhraseRule(r"(are you|you are|you're) (depressed|an addict|mentally ill|"
               r"broken|weak)", Severity.WARNING, _DIAGNOSIS,
               "Describe experience, not diagnosis: 'You may be feeling "
               "overwhelmed…'."),
    PhraseRule(r"(do you have|you have|suffering from) (depression|anxiety|"
               r"a disorder|ptsd|ocd|an addiction)", Severity.WARNING,
               _DIAGNOSIS, "Avoid attributing a condition to the reader."),
    PhraseRule(r"(ashamed|man up|snap out of it|pull yourself together)",
               Severity.WARNING, _DIAGNOSIS, "Remove shaming language."),
    # Superlatives
    PhraseRule(r"(the )?best (therapy|therapist|counsell?ing|counsell?or)",
               Severity.WARNING, _SUPERLATIVE,
               "Remove 'best' or cite a verifiable source."),
    PhraseRule(r"(number one|no\.? ?1(?!\d)|#1)", Severity.WARNING,
               _SUPERLATIVE, "Remove 'number one'."),
]

# Pisownia amerykańska → brytyjska (Mental ma być w en-GB).
US_TO_UK_SPELLING = {
    "counseling": "counselling",
    "counselor": "counsellor",
    "behavior": "behaviour",
    "behavioral": "behavioural",
    "center": "centre",
    "program": "programme",
    "organization": "organisation",
    "personalized": "personalised",
    "specialized": "specialised",
    "recognized": "recognised",
    "color": "colour",
    "favor": "favour",
    "practicing": "practising",
}

POLISH_DIACRITICS = re.compile(r"[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]")
