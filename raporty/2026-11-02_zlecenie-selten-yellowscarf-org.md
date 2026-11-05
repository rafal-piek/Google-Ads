# Zlecenie dla Seltena — yellowscarf.org (Fundacja, Yellow Scarf CIO) — 2.11.2026

Cel: żeby kampanie Google Ad Grants (konto 798-577-2656) mogły mierzyć zgłoszenia i zapisy na grupy, a strony spełniały zasady Ad Grants i ochrony danych. Właściwość GA4: 538419573 („Yellow Scarf CIO – www.yellowscarf.org”). Google Ads konta Fundacji NIE łączyć z GA4 Ośrodka (277882249).

## 1. Zdarzenia GA4 (przez Google Tag Manager, Consent Mode v2)
| Zdarzenie | Kiedy | Uwagi |
|---|---|---|
| `generate_lead` | po UDANYM wysłaniu formularza na /pl/potrzebuje-pomocy.html i /en-gb/i-need-help.html (strona lub komunikat potwierdzenia, nie kliknięcie „Wyślij”) | parametry: tylko `form_id` i `page_location`; ŻADNYCH treści pól |
| `sign_up_group` | kliknięcie „Zapisz się na Grupę” na /pl/jak-pomagamy.html oraz udane wysłanie formularza #umow-sie-z-nami | parametr `group_type` (wstepna / terapeutyczna / indywidualna) jest OK |
| `click_to_call` | kliknięcie linku tel: | — |
| `click_email` | kliknięcie mailto: | — |
| `donate_click` (istnieje) | bez zmian | — |
W GA4 oznaczyć `generate_lead` i `sign_up_group` jako zdarzenia kluczowe. Import do Google Ads zrobimy po stronie konta.

## 2. Formularze (minimalizacja danych, UK GDPR — dane o zdrowiu)
- /pl/potrzebuje-pomocy.html i /en-gb/i-need-help.html: pola obowiązkowe tylko imię + e-mail LUB telefon (jedno z dwóch); nazwisko i telefon opcjonalne; „Opis sytuacji” opcjonalny z dopiskiem „Nie musisz podawać szczegółów. Wystarczy, że napiszesz, że chcesz porozmawiać.”
- Treść zgody po polsku z linkiem do polskiej polityki prywatności (dziś link prowadzi do wersji EN).
- Po wysłaniu: strona/komunikat potwierdzenia („Dziękujemy, odezwiemy się w dni robocze”) — to na nim odpala się `generate_lead`.
- Dane z formularzy nie trafiają do GA4 ani do Google Ads.

## 3. Treści (zgodność z Google: Addiction services w UK)
- /pl/jak-pomagamy.html i meta description stron PL: zamiast „nałóg / uzależnienie” używać „zdrowie psychiczne, kryzys, trudności na emigracji”; o uzależnieniach tylko w sekcjach projektowych, nie w opisie grup ani w meta description.
- /pl/jak-pomagamy.html: dopisać zdanie, jak opłaty za grupy wspierają misję organizacji charytatywnej (wymóg Ad Grants dla działalności odpłatnej), i numer charity 1190615 w stopce każdej strony.
- Numer infolinii +44 7340 634326 i godziny (pn–pt 10–16) widoczne na /pl/potrzebuje-pomocy.html i /pl/kontakt-z-nami.html.

## 4. Nowa podstrona (opcjonalnie, dla kampanii EN lokalnej)
/en-gb/gambling-support.html: opis grup w Worcester i Evesham (dzień, godzina, dla kogo, prowadzący, koszt/bezpłatnie, jak dołączyć), formularz lub przycisk do /en-gb/i-need-help.html, numer telefonu. Bez słów o leczeniu uzależnień od alkoholu/narkotyków.

## 5. Techniczne
- Sprawdzić etykietę „URGENT” przy tagu Google „YELLOW SCARF CIO” w Google Ads / Tag Manager i Consent Mode v2.
- hreflang PL/EN na stronach z wersjami językowymi.
- Sprawdzić, czy /pl/ ma własne linki nawigacji PL na wszystkich podstronach (na stronie głównej część linków prowadzi do /en-gb/).

Termin: do 9.11.2026, żeby kampanie mogły uczyć się na konwersjach od połowy listopada.
