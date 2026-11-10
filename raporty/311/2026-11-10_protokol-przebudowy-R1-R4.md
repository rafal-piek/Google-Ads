# Mental 311 — protokół przebudowy reklam (R1–R4), 10.11.2026

Konto: Mental 311-878-5541 (yellowscarftherapy.co.uk, YELLOW SCARF CIC). Kampania 23815171848 „Private Online Therapy UK”, grupa 196547957415.
Podstawa: decyzja Rafała 10.11 („bardziej przebudowa reklam niż zlikwidowanie”, „dzialaj”). Wykonanie: panel przez Chrome Rafała (authuser=3). Weryfikacja: odczyt API po zmianach 10.11.

| Krok | Zakres | Stan po API |
|---|---|---|
| R1 | Wstrzymanie wszystkich słów PHRASE (w tym „find a private counsellor” = 64% kosztu z 60 dni) | WYKONANE — 0 aktywnych phrase |
| R2 | Exact z „online/private/video”, końcowy URL /therapists | WYKONANE — 22 exact ENABLED, wszystkie APPROVED, URL /therapists |
| R3 | Wykluczenia kampanii (infolinie, numery, NHS, 24/7, „right now”, „contact number” itd.) | WYKONANE — widoczne w campaign_criterion |
| R4 | Nowa RSA „Private Service, Not NHS / Online Only”, stare RSA wstrzymane | NIEWYKONANE — edytor reklam blokowany: „Turn off ad blockers” (bloker reklam w Chrome) |
| R5 | Max clicks, limit CPC £3 | Nie robione — poza zakresem „dzialaj” |
| R6 | Harmonogram rozszerzenia połączeń | Zrobione wcześniej jako P3 (pn–pt 9–17) |

Wstrzymane exact (nie dało się włączyć w zwirtualizowanej tabeli; do decyzji): counselling by video call, private talking therapy uk, counselling for burnout, burnout treatment, loss counselling online.

Aktywne reklamy teraz: RSA 807816379345 i 807896903510 (APPROVED, URL /book-a-session; słowa exact mają nadpisanie URL na /therapists).

Do zrobienia R4 po wyłączeniu blokera dla ads.google.com: teksty, przypięcia i URL — patrz 2026-11-10_311-przebudowa-reklam-propozycja.md. Po dodaniu: wstrzymać obie stare RSA, odczyt API.
