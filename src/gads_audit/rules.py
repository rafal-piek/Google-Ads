"""Stałe i progi audytu — oparte na oficjalnych limitach Google Ads oraz
sprawdzonych dobrych praktykach (stan na 2024/2025; limity RSA bez zmian
przy weryfikacji 2026-10-12).

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

# Słowniki CTA i zakazanych sformułowań są osobno dla usług terapeutycznych
# (PL i brytyjski angielski) — patrz `therapy_vocab.py`. Ogólne słowniki
# e-commerce („kup”, „rabat”, „sale”) celowo usunięto: nie pasują do żadnego
# z kont Yellow Scarf.
