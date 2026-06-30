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
