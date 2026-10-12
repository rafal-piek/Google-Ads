"""Uruchomienie audytu dla jednego, jawnie wskazanego konta."""

from __future__ import annotations

from typing import Iterable, Optional

from .accounts import AccountProfile, get_profile
from .checks import ad_grants, compliance, technical
from .model import AccountSnapshot, Finding, ResponsiveSearchAd


class AccountMismatchError(ValueError):
    """Dane pochodzą z innego konta niż audytowany profil."""


def run_audit(account: str | AccountProfile,
              ads: Iterable[ResponsiveSearchAd],
              snapshot: Optional[AccountSnapshot] = None,
              medical_terms: frozenset[str] = frozenset()) -> list[Finding]:
    profile = account if isinstance(account, AccountProfile) else get_profile(account)

    if snapshot is not None:
        digits = snapshot.customer_id.replace("-", "")
        if digits != profile.customer_id_digits:
            raise AccountMismatchError(
                f"Dane konta {snapshot.customer_id} nie należą do profilu "
                f"{profile.name} ({profile.customer_id}). Audyt przerwany, "
                "żeby nie pomieszać kont."
            )

    findings: list[Finding] = []
    for ad in ads:
        if ad.status == "REMOVED":
            continue
        findings += technical.check_ad(ad)
        findings += compliance.check_ad(ad, profile)
    if snapshot is not None:
        findings += ad_grants.check_account(snapshot, profile, medical_terms)
    return findings
