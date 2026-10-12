"""Profile trzech kont Google Ads Yellow Scarf.

Zasada nadrzędna: konta, domeny, podmioty i zasady zgodności NIGDY się nie
mieszają. Każdy audyt działa na dokładnie jednym profilu, a kontrole sprawdzają,
czy reklamy i dane rzeczywiście należą do tego konta.

Plik zawiera wyłącznie dane identyfikacyjne kont (nie są poświadczeniami).
Tokeny, sekrety OAuth i adresy e-mail logowania trzymamy poza repo.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from . import therapy_vocab as vocab


class AccountType(str, Enum):
    COMMERCIAL = "komercyjne"
    AD_GRANTS = "Google Ad Grants"


@dataclass(frozen=True)
class AccountProfile:
    key: str                     # nazwa potoczna: osrodek / fundacja / mental
    name: str
    customer_id: str             # format 123-456-7890
    domain: str                  # domena docelowa reklam (bez www)
    account_type: AccountType
    legal_entity: str
    language: str                # "pl" lub "en-GB"
    goal: str
    cta_phrases: tuple[str, ...]
    forbidden_rules: tuple[vocab.PhraseRule, ...]
    # Słowa marki dopuszczone jako jednowyrazowe słowa kluczowe (Ad Grants).
    brand_terms: tuple[str, ...] = field(default_factory=tuple)

    @property
    def customer_id_digits(self) -> str:
        return self.customer_id.replace("-", "")

    @property
    def is_ad_grants(self) -> bool:
        return self.account_type is AccountType.AD_GRANTS


OSRODEK = AccountProfile(
    key="osrodek",
    name="Osrodek",
    customer_id="733-094-4080",
    domain="osrodek.uk",
    account_type=AccountType.COMMERCIAL,
    legal_entity="YELLOW SCARF CIC",
    language="pl",
    goal="Więcej płacących klientów terapii i usług ośrodka (online, "
         "osoby polskojęzyczne w UK).",
    cta_phrases=tuple(vocab.CTA_PL_THERAPY),
    forbidden_rules=tuple(vocab.FORBIDDEN_PL),
    brand_terms=("osrodek", "ośrodek", "yellowscarf"),
)

FUNDACJA = AccountProfile(
    key="fundacja",
    name="Fundacja",
    customer_id="798-577-2656",
    domain="yellowscarf.org",
    account_type=AccountType.AD_GRANTS,
    legal_entity="Yellow Scarf CIO",
    language="pl",
    goal="Działania społeczne, edukacyjne, pomocowe i grupowe; cel 2026: "
         "4 grupy po 6-8 płacących uczestników.",
    cta_phrases=tuple(vocab.CTA_PL_THERAPY + vocab.CTA_PL_COMMUNITY
                      + vocab.CTA_EN_GB_THERAPY),
    forbidden_rules=tuple(vocab.FORBIDDEN_PL + vocab.FORBIDDEN_EN),
    brand_terms=("yellowscarf", "yellow scarf"),
)

MENTAL = AccountProfile(
    key="mental",
    name="Mental",
    customer_id="311-878-5541",
    domain="yellowscarftherapy.co.uk",
    account_type=AccountType.COMMERCIAL,
    legal_entity="YELLOW SCARF CIC",
    language="en-GB",
    goal="Rozwój anglojęzycznej terapii online w UK (klienci brytyjscy).",
    cta_phrases=tuple(vocab.CTA_EN_GB_THERAPY),
    forbidden_rules=tuple(vocab.FORBIDDEN_EN),
    brand_terms=("yellowscarf", "yellowscarftherapy"),
)

PROFILES: dict[str, AccountProfile] = {
    p.key: p for p in (OSRODEK, FUNDACJA, MENTAL)
}


def get_profile(key_or_id: str) -> AccountProfile:
    """Zwraca profil po nazwie potocznej albo customer ID (z myślnikami lub bez)."""
    needle = key_or_id.strip().lower()
    if needle in PROFILES:
        return PROFILES[needle]
    digits = needle.replace("-", "")
    for p in PROFILES.values():
        if p.customer_id_digits == digits:
            return p
    known = ", ".join(f"{p.name} ({p.customer_id})" for p in PROFILES.values())
    raise KeyError(f"Nieznane konto „{key_or_id}”. Dostępne: {known}.")


def profile_for_domain(host: str) -> AccountProfile | None:
    """Który profil jest właścicielem danej domeny (do wykrywania pomyłek)."""
    host = host.lower().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    for p in PROFILES.values():
        if host == p.domain or host.endswith("." + p.domain):
            return p
    return None
