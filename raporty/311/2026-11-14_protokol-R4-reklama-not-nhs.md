# Mental 311 — protokół R4 + M1: reklama „Not NHS / Online Only” i 4 słowa exact, 14.11.2026

Konto: Mental 311-878-5541 (yellowscarftherapy.co.uk, YELLOW SCARF CIC). Kampania 23815171848, Grupa reklam 1 (196547957415).
Podstawa: Rafał 14.11 „ok to dzialaj” (dokończenie R4 z przebudowy 10.11). Wykonanie: panel w Chrome Rafała (Claude in Chrome). Weryfikacja: odczyt API przed i po.

## Przed (API)
- RSA 807816379345 i 807896903510: ENABLED, APPROVED, URL /book-a-session.

## Zmiana (jedna partia)
1. Nowa RSA **831626407411**, URL https://yellowscarftherapy.co.uk/therapists, ścieżka /online/therapy.
   - 15 nagłówków (en-GB) wg propozycji z 10.11; przypięte do pozycji 2: „Private Service, Not NHS” i „Online Only, Not Face to Face” (rotują w poz. 2).
   - 4 opisy; opis 1 przypięty do pozycji 1: „Private online therapy by video across the UK. Not an NHS or crisis service.”
   - Bez „free”, bez obietnic efektów, bez BACP. Komponenty kampanii (sitelinki, obrazy, logo, nazwa firmy) bez zmian — edytor pokazał istniejące.
2. Wstrzymane stare RSA 807816379345 i 807896903510.

## Po (API, 14.11 ok. 18:30 UTC)
| Reklama | Status | Zatwierdzenie | URL |
|---|---|---|---|
| 831626407411 (nowa) | ENABLED | APPROVED / REVIEWED | /therapists |
| 807816379345 | PAUSED | APPROVED | /book-a-session |
| 807896903510 | PAUSED | APPROVED | /book-a-session |

Siła reklamy w edytorze: „Average/Good” (przypięcia obniżają ocenę — świadomy wybór, priorytetem jest jasny komunikat „not NHS / online only”).

## Uzupełnienie M1 (audyt rezerw 14.11, Rafał „ok to dzialaj”)
3. Dodane słowa exact w Grupie reklam 1: [online therapy], [online counselling], [online therapist], [online counsellor].
   API po zmianie: wszystkie 4 ENABLED, EXACT, UNDER_REVIEW (zwykła weryfikacja), bez nadpisania URL → używają URL reklamy /therapists.

Nie ruszano: stawek, strategii (R5), budżetu ani istniejących słów kluczowych.

Do sprawdzenia ok. 21.11: wyświetlenia i CTR nowej reklamy, Wynik Jakości słów exact, odsetek telefonów-pomyłek (log Nikoli).
