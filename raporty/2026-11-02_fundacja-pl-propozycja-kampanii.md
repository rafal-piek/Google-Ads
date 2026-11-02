# Fundacja Yellow Scarf (Polska) — propozycja nowego konta i kampanii Google Ads na Polskę i UE

**Data:** 2.11.2026. **Status:** propozycja do akceptacji; nic nie zostało założone ani uruchomione.
**Podmiot:** Fundacja Yellow Scarf, KRS 0001274628, NIP 9542917449, REGON 546020497, ul. Warszawska 40 lok. 2A, 40-008 Katowice. Fundator: Yellow Scarf CIO (UK).
**Strona:** https://yellowscarf.eu (PL; wersja EN pod /en/). Kontakt: +48 453 088 111, info@yellowscarf.eu.
**Konto Google Ads:** jeszcze nie istnieje. To **czwarty, osobny podmiot** — dostaje **własne konto** („Fundacja PL”). Nie wolno użyć konta Ad Grants 798 (Yellow Scarf CIO, tylko yellowscarf.org) ani kont CIC 733/311. W MCC 700-738-5800 może być podpięte jako kolejne konto klienckie, z osobnym profilem płatności.

Na czym się opieram: prośba Rafała z 2.11.2026 11:39 („nowa kampania reklamowa dla Fundacji Yellow Scarf w Polsce i Unii Europejskiej”), treść strony yellowscarf.eu (strona główna, /potrzebuje-wsparcia/, /co-robimy/, /kontakt/), kontrola zasad z 2.11.2026 (§3) oraz dzisiejsza kontrola zasad Ad Grants (`raporty/2026-11-02_zrodla-ad-grants.md`).

## 0. W skrócie

1. Potrzebne jest **nowe konto Google Ads** dla polskiej fundacji, w PLN, z profilem płatności „organizacja” na dane z KRS. Wariant grantowy (Ad Grants PL) jest możliwy, ale wymaga najpierw rejestracji w Google dla Organizacji Non-Profit i zdjęcia `noindex` ze strony; realny start to 2–4 tygodnie.
2. Najważniejsze ograniczenie: **reklamy usług dla uzależnień od alkoholu i narkotyków są w Polsce i w całej UE poza FR/IE niedozwolone** (polityka „Addiction services”). Kampania omija ten temat w słowach kluczowych i tekstach, a reklamy kierują na stronę bez sekcji o uzależnieniach (do zbudowania: `/pomoc-online/`). Do czasu jej powstania — na `/potrzebuje-wsparcia/` z ryzykiem statusu „ograniczone”.
3. Proponuję dwie kampanie Search po polsku: **K1 „[PL] Pomoc psychologiczna online – Polska”** (grupy: Psychoterapia online, Psycholog online, Grupy wsparcia, Wsparcie dla bliskich, Marka) i **K2 „[PL] Polacy w Europie”** (DE, NL, IE, NO, BE, SE, DK, AT, CZ; bez UK, które obsługuje grant 798). Budżet startowy przy wariancie płatnym: 50 PLN/dz (≈1 500 PLN/mies.), podział 35/15.
4. Konwersja główna: wysłanie formularza z /potrzebuje-wsparcia/ (zdarzenie `generate_lead`), drugorzędne: kliknięcie telefonu i e‑maila. Potrzebne: GA4 dla yellowscarf.eu, Google Tag, **Consent Mode v2 z banerem zgody** (wymóg Google w EOG).
5. Start na „Maksymalizacja kliknięć” z limitem CPC 6 PLN przez 2–3 tygodnie, potem „Maksymalizacja konwersji” po ≥15 konwersjach. Bez tCPA, bez dopasowania przybliżonego, bez Display/Demand Gen/PMax, bez remarketingu i list własnych (zdrowie = kategoria wrażliwa).

## 1. Co wiemy o fundacji i stronie (odczyt 2.11.2026)

- Oferta: konsultacje i rozmowy, psychoterapia (indywidualna, par, rodzin; głównie online), grupy wsparcia i terapeutyczne, wsparcie dla bliskich osób w kryzysie lub uzależnieniu, pomoc w sprawach praktycznych, szkolenia i superwizje dla specjalistów. Rozmowy po polsku, także dla osób mieszkających za granicą.
- Proces: kontakt → krótka rozmowa o potrzebach → wspólny wybór formy wsparcia. Odpowiedź w dni robocze, zwykle do ok. 2 dni. Bez skierowania i diagnozy. Część działań bezpłatna (granty, darowizny), część płatna; koszt podawany przed startem.
- Fundacja nie jest służbą ratunkową (odsyła na 112 i 800 70 2222). Formularz: imię, e‑mail, kraj (PL/UK/IE/DE/NL/NO/inny), opcjonalnie telefon i kilka słów, dla kogo, czego szuka, preferowany kontakt, zgoda na przetwarzanie. Prośba, by nie opisywać zdrowia w formularzu — dobra praktyka, zgodna z minimalizacją danych.
- Techniczne: strona ma `meta robots noindex, nofollow`. Dla reklam Search nie blokuje to emisji, ale blokuje SEO i jest przeszkodą dla Ad Grants (strona musi być indeksowalna i spełniać politykę witryny). Brak widocznego baneru zgody i GA4 (do potwierdzenia u Seltena / osoby prowadzącej stronę).
- Konto Google Workspace w domenie yellowscarf.eu istnieje od ok. 27–29.10.2026 (rafal@yellowscarf.eu).

## 2. Cel, mierniki, bramki

- **Cel:** pierwsze kontakty osób dorosłych szukających pomocy psychologicznej po polsku (Polska i Polacy w UE). Drugi plan (po 60 dniach): grupy wsparcia, oddzielna kampania dla specjalistów (szkolenia/superwizje) tylko na wyraźną decyzję.
- **Mierniki:** liczba wysłanych formularzy, kliknięcia telefon/e‑mail, koszt za kontakt, odsetek kontaktów, które przeszły w pierwszą rozmowę (z kalendarza fundacji, nie z Ads).
- **Założenia liczbowe (do zweryfikowania w Planerze słów kluczowych po założeniu konta):** CPC w PL dla fraz „psychoterapia/psycholog online” ok. 3–8 PLN; przy 1 500 PLN/mies. ≈ 200–350 kliknięć; przy 2–4% konwersji ≈ 5–12 formularzy miesięcznie. To szacunek, nie obietnica.
- **Bramki:** 14 dni — kontrola wyszukiwanych haseł i wykluczeń; 30 dni — koszt/kontakt i decyzja o Max Conversions; 60 dni — decyzja o kampanii dla grup i o Ad Grants PL.

## 3. Zasady, które wiążą (sprawdzone 2.11.2026, 11:45–12:10 UTC)

Źródła oficjalne (Google):
1. Healthcare and medicines: Addiction services — https://support.google.com/adspolicy/answer/15598649
2. Healthcare and medicines (polityka główna) — https://support.google.com/adspolicy/answer/176031
3. Health in personalized advertising — https://support.google.com/adspolicy/answer/16701855
4. Update to Personalized advertising policy (wrzesień 2026, alkohol/YouTube) — https://support.google.com/adspolicy/answer/17598957
5. Update to Healthcare and Medicines policy (październik 2025, leki na receptę) — https://support.google.com/adspolicy/answer/16606361
6. Tasks required for Advertiser verification — https://support.google.com/adspolicy/answer/15577076
7. Understanding Google Ads country restrictions — https://support.google.com/google-ads/answer/6163740
8. Google dla Organizacji Non-Profit: kwalifikacja — https://www.google.com/intl/pl/nonprofits/eligibility/
9. Google dla Organizacji Non-Profit: FAQ (PL) — https://www.google.com/intl/pl/nonprofits/resources/faq
10. Ad Grants: aktywacja — https://support.google.com/nonprofits/answer/3367461
11. Google for Nonprofits: kraje i partner weryfikacji — https://support.google.com/nonprofits/answer/1614602
Branżowe, niezależne:
12. Accelerated Digital Media, 2026 Search Advertising Rules for Health Brands — https://www.accelerateddigitalmedia.com/insights/health-policies-and-restrictions-guide-for-google-ads-microsoft-ads-2026/
13. OuterBox, Health and Wellness Advertising Restrictions on Google Ads — https://www.outerboxdesign.com/articles/digital-marketing/health-and-wellness-advertising-restrictions-on-google-ads-keeping-your-campaigns-compliant/
14. StubGroup, Healthcare and Medicines Policy (akt. 11.11.2025) — https://stubgroup.com/glossary/healthcare-and-medicines-policy/
15. eSEOspace, Google Ads for therapists — https://eseospace.com/blog/google-ads-for-therapists/
16. PPC Land, Advertiser verification — https://ppc.land/advertiser-verification/
17. Delante (PL), Advertiser verification in Google Ads — https://delante.co/advertiser-verification-in-google-ads/
18. Measure Minds, Is Consent Mode v2 mandatory in 2026 — https://measuremindsgroup.com/is-consent-mode-v2-mandatory
19. CookieYes, Google-certified CMP for Consent Mode v2 — https://www.cookieyes.com/google-consent-mode-certified-cmp/
20. Kontrola Ad Grants z 2.11.2026 (12 źródeł) — `raporty/2026-11-02_zrodla-ad-grants.md`

Najważniejsze zasady:
- **Addiction services (źr. 1):** „recovery-oriented drug and alcohol addiction services” (leczenie, ośrodki, grupy samopomocowe, infolinie, pośrednicy) mogą reklamować tylko zatwierdzeni reklamodawcy i tylko w AU, CA, FR, IE, NZ, US. Polska, Niemcy, Holandia, Norwegia, Belgia itd. — brak możliwości. Poza zakresem: uzależnienia behawioralne (hazard, gry), nikotyna. Naruszenie → ostrzeżenie min. 7 dni przed zawieszeniem.
- **Zdrowie w reklamach spersonalizowanych (źr. 3):** poradnictwo w depresji, lęku i uzależnieniach jest wprost kategorią wrażliwą → zakaz Customer Match, list własnych, rozszerzania odbiorców, lookalike; dozwolone kierowanie geograficzne, językowe, słowa kluczowe. Brak personalizacji dla osób <18 lat.
- **Healthcare (źr. 2, 5, 12–14):** bez obietnic wyleczenia, bez terminów leków na receptę w słowach i tekstach, reklama i strona docelowa oceniane razem; zmiana strony = ponowna ocena.
- **Weryfikacja reklamodawcy (źr. 6, 16, 17):** profil płatności typu „organizacja”, nazwa i adres identyczne z dokumentem (odpis KRS), pytania o organizację i finansującego, deklaracja braku reklam politycznych w UE, potwierdzenie przynależności kodem; przegląd do 5 dni roboczych (rzadko do 30). Nazwa „Fundacja Yellow Scarf” pojawi się w ujawnieniach „Płatne przez”.
- **Google dla Organizacji Non-Profit / Ad Grants PL (źr. 8–11):** Polska jest na liście krajów; weryfikację prowadzi Goodstack (wcześniej Percent), zwykle 3–5 dni roboczych; wykluczone m.in. placówki ochrony zdrowia (fundacja prowadząca wsparcie psychologiczne zwykle przechodzi, ale „placówka zdrowotna” to ryzyko do sprawdzenia); **nie wolno zakładać konta Ads samodzielnie** — konto grantowe przydziela aktywacja; strona HTTPS i zgodna z polityką witryny (indeksowalna, misja, dane rejestrowe, wyjaśnienie płatnych usług).
- **Consent Mode v2 (źr. 18, 19):** dla ruchu z EOG Google wymaga sygnałów zgody (ad_user_data, ad_personalization) do pomiaru konwersji i funkcji reklamowych; bez tego pomiar jest ograniczony. Potrzebny baner zgody (najlepiej certyfikowany CMP) na yellowscarf.eu. Informacja o wymaganiach może się zmieniać — sprawdzić ponownie przy wdrożeniu.
- **Pozostałe (źr. 7):** Google Ads dostępny w Polsce w PLN; kierowanie na UE bez przeszkód; VAT — faktury od Google Ireland, rozliczenie importu usług po stronie fundacji (do potwierdzenia z księgową; poza moim zakresem).

Najważniejsze ryzyka:
1. Strona docelowa /potrzebuje-wsparcia/ zawiera sekcję „wsparcie dla bliskich osoby z uzależnieniem” i wzmiankę o własnym piciu/używkach → reklamy mogą dostać status „Eligible (limited)” lub odrzucenie z powodu Addiction services, mimo że słowa kluczowe tego nie dotykają. Rozwiązanie: dedykowana strona `/pomoc-online/` bez tej sekcji (§7).
2. Brak GA4, tagu i zgody → brak konwersji → ślepa optymalizacja. Rozwiązanie: wdrożyć przed startem (§6).
3. `noindex` — nie blokuje Ads, ale blokuje Ad Grants i SEO; do zdjęcia, gdy strona jest gotowa.
4. Mieszanie podmiotów: Polacy w UK szukają po polsku i trafią na obie fundacje (798 i PL). Rozwiązanie: K2 bez UK; 798 bez Polski.
5. Nowe konto bez historii → wyższe CPC na start; ryzyko kliknięć informacyjnych („co to jest psychoterapia”). Rozwiązanie: dopasowanie do wyrażenia/ścisłe, wykluczenia od pierwszego dnia, przegląd haseł po 7 i 14 dniach.

## 4. Dwa warianty finansowania

| | A. Konto płatne (rekomendowane na start) | B. Ad Grants PL (równolegle do przygotowania) |
|---|---|---|
| Kto zakłada | Rafał, konto Google rafal@yellowscarf.eu (lub info@) | Rafał, to samo konto Google; najpierw Google dla Organizacji Non-Profit |
| Czas do startu | 2–5 dni (konto, płatność, weryfikacja, tag) | 2–4 tygodnie (weryfikacja Goodstack 3–5 dni + aktywacja Ad Grants + poprawki strony) |
| Budżet | ok. 1 500 PLN/mies. na start (50 PLN/dz) | do 10 000 USD/mies., ale realnie wydatek zależy od ruchu; reguły CTR ≥5%, konwersje, Smart Bidding |
| Kto płaci | Fundacja Yellow Scarf (PL), karta lub przelew; faktury na KRS/NIP | Google |
| Wymagania strony | baner zgody + GA4 | jak A + brak `noindex`, misja, dane rejestrowe, wyjaśnienie płatnych usług |
| Ryzyko | koszt; CPC bez historii | odrzucenie kwalifikacji („placówka zdrowotna”), dezaktywacja przy CTR <5% |

Rekomendacja: **A teraz, B w tle**. Konto płatne i grantowe mogą istnieć obok siebie (różne konta, ten sam podmiot), ale w grantowym nie wolno powielać kampanii komercyjnych bez wyjaśnienia misji.

## 5. Proponowana struktura (wariant A)

**Ustawienia konta:** waluta PLN, strefa Europe/Warsaw, profil płatności „organizacja” (Fundacja Yellow Scarf, ul. Warszawska 40/2A, 40-008 Katowice, NIP 9542917449), auto-apply wyłączone, śledzenie konwersji włączone, Customer Match i rozszerzone konwersje dla leadów wyłączone, brak list remarketingowych. Dostęp administracyjny: rafal@yellowscarf.eu; MCC 700-738-5800 jako menedżer (osobne rozliczenie).

**K1 — „[PL] Pomoc psychologiczna online – Polska”** — Search, tylko sieć wyszukiwania (bez partnerów, bez Display), lokalizacja: Polska (obecność), język: polski, budżet 35 PLN/dz, stawki: Maksymalizacja kliknięć z limitem 6 PLN → po ≥15 konwersjach Maksymalizacja konwersji. Harmonogram: całą dobę (formularz działa zawsze), rozszerzenie telefonu tylko 9–18 w dni robocze.
- Grupa A — Psychoterapia online
- Grupa B — Psycholog / konsultacja online
- Grupa C — Grupy wsparcia online
- Grupa D — Wsparcie dla bliskich (bez tematu uzależnień)
- Grupa E — Marka (Fundacja Yellow Scarf)

**K2 — „[PL] Polacy w Europie”** — Search, lokalizacje: Niemcy, Holandia, Irlandia, Norwegia, Belgia, Szwecja, Dania, Austria, Czechy (obecność; **bez Wielkiej Brytanii** — to obszar grantu 798), język: polski, budżet 15 PLN/dz, stawki jak K1 (limit 5 PLN).
- Grupa F — Polski psycholog / psychoterapeuta za granicą
- Grupa G — Grupy wsparcia dla Polaków za granicą

Nie teraz: kampania dla specjalistów (szkolenia, superwizje), kampania darowizn, PMax, Demand Gen, Display, wideo, AI Max.

## 6. Słowa kluczowe (dopasowanie do wyrażenia „…” i ścisłe […]; bez słów jednowyrazowych)

**A — Psychoterapia online:** "psychoterapia online", "psychoterapeuta online", "terapia online", "psychoterapia przez internet", "psychoterapia online dla dorosłych", "terapia indywidualna online", "psychoterapia par online", "terapia par online", "terapia rodzinna online", "psychoterapia online cena", [psychoterapia online], [psychoterapeuta online], [terapia online].

**B — Psycholog / konsultacja online:** "psycholog online", "konsultacja psychologiczna online", "rozmowa z psychologiem online", "pomoc psychologiczna online", "wsparcie psychologiczne online", "psycholog online konsultacja", "pierwsza wizyta u psychologa online", "psycholog przez internet", "pomoc psychologiczna dla dorosłych", [psycholog online], [konsultacja psychologiczna online], [pomoc psychologiczna online].

**C — Grupy wsparcia online:** "grupa wsparcia online", "grupy wsparcia online", "grupa wsparcia dla dorosłych", "grupa terapeutyczna online", "grupa wsparcia dla kobiet online", "grupa wsparcia dla mężczyzn online", "grupa wsparcia dla rodziców", "grupa wsparcia depresja online", "grupa wsparcia lęk online", [grupa wsparcia online], [grupa terapeutyczna online].

**D — Wsparcie dla bliskich (bez uzależnień):** "wsparcie dla bliskich osoby w kryzysie", "pomoc dla rodziny osoby w depresji", "jak pomóc bliskiej osobie w kryzysie", "wsparcie dla partnera osoby w depresji", "grupa wsparcia dla bliskich", "konsultacja dla rodziny psycholog", "pomoc psychologiczna dla rodziny", [wsparcie dla bliskich], [grupa wsparcia dla bliskich].

**E — Marka:** [fundacja yellow scarf], [yellow scarf], "yellow scarf fundacja", "yellow scarf katowice", "fundacja yellow scarf opinie", "fundacja pomoc psychologiczna online", "fundacja wsparcie psychologiczne".

**F — Polski psycholog za granicą (K2):** "psycholog po polsku", "psychoterapeuta po polsku", "polski psycholog online", "polski psychoterapeuta online", "psycholog polski za granicą", "terapia po polsku online", "pomoc psychologiczna dla polaków za granicą", "psycholog po polsku niemcy", "polski psycholog holandia", "polski psycholog irlandia", "polski psycholog norwegia", "polski psycholog belgia", [psycholog po polsku], [polski psycholog online], [polski psychoterapeuta online].

**G — Grupy wsparcia dla Polaków za granicą (K2):** "grupa wsparcia po polsku online", "grupa wsparcia dla polaków za granicą", "grupa wsparcia emigracja", "wsparcie psychologiczne emigracja", "samotność na emigracji pomoc", "stres emigracja psycholog", [grupa wsparcia po polsku], [grupa wsparcia emigracja].

### Wykluczenia — lista współdzielona „Spoza oferty – Fundacja PL” (podpięta do K1 i K2)
- **Uzależnienia (zgodność, polityka Addiction services):** uzależnienie, uzależnienia, uzależnień, uzależniony, odwyk, detoks, alkoholizm, alkoholik, alkohol, picie, narkotyki, narkomania, dopalacze, leczenie uzależnień, ośrodek leczenia, ośrodek terapii uzależnień, terapia uzależnień, mityng, mityngi, anonimowi alkoholicy, al-anon, dda, ddd, hazard, hazardzista, uzależnienie od gier.
- **Poza ofertą:** psychiatra, psychiatra online, leki, tabletki, recepta, e-recepta, l4, zwolnienie, zus, orzeczenie, nfz, na nfz, skierowanie, znanylekarz, dla dzieci, dziecięcy, nastolatek, młodzież, szkoła, przedszkole, seksuolog, dietetyk, coaching, coach, hipnoza, ustawienia, astrolog, tarot, kryzysowy telefon, telefon zaufania, 116 123.
- **Informacyjne:** co to jest, definicja, objawy, test, quiz, czy mam, jak rozpoznać, pdf, książka, film, serial, memy, wikipedia.
- **Praca i edukacja:** praca, oferty pracy, zarobki, studia, kierunek, kurs, szkolenie, certyfikat, egzamin, rekrutacja, staż, wolontariat (do czasu osobnej kampanii), superwizja (do czasu kampanii dla specjalistów).
- **Cenowe/konkurencyjne:** za darmo, darmowy, bezpłatny psycholog (nie obiecujemy bezpłatności w reklamach), najtańszy, tani, promocja, ranking, najlepszy psycholog.
- **Kryzys (nie jesteśmy służbą ratunkową):** samobój*, samobójstwo, samobójcze, chcę umrzeć, interwencja kryzysowa 24h, pogotowie.
- **Geo (K2):** anglia, londyn, uk, wielka brytania, szkocja (kierują na 798). **(K1):** niemcy, holandia, irlandia, norwegia (kierują na K2).

## 7. Strony docelowe

- **Teraz:** A, B, D → `/potrzebuje-wsparcia/`; C, G → `/co-robimy/` (jeśli ma sekcję o grupach) lub `/potrzebuje-wsparcia/`; E → `/`; F → `/potrzebuje-wsparcia/`.
- **Do zbudowania przed startem (zadanie dla Seltena / osoby od strony, 1 strona):** `/pomoc-online/` — „Pomoc psychologiczna online po polsku” — proces w 3 krokach, formy wsparcia (konsultacja, psychoterapia, grupy, wsparcie dla bliskich osoby w kryzysie) **bez słów o uzależnieniach**, informacja o kosztach („koszt podajemy przed startem; część działań finansują granty”), poufność, dane rejestrowe, numery 112 i 800 70 2222, ten sam formularz. Druga, lekka wersja `/pomoc-online/polacy-w-europie/` z akapitem o różnicy czasu i pracy online z zagranicy (dla K2).
- **Strona i pomiar:** GA4 dla yellowscarf.eu (nowa właściwość, strefa Warszawa, PLN), Google Tag przez GTM, baner zgody z Consent Mode v2 (certyfikowany CMP, np. CookieYes/Cookiebot/Complianz — wybór po stronie Seltena), zdarzenia: `generate_lead` (udane wysłanie formularza, bez treści pól), `click_to_call`, `click_email`. Import do Ads jako konwersje: formularz — główna; telefon/e‑mail — drugorzędne. Żadnych danych o stanie zdrowia w parametrach zdarzeń, w URL ani w nazwach konwersji.
- **Formularz:** zostaje jak jest (imię, e‑mail, kraj; telefon i opis opcjonalne; zgoda). Sugestia: pod polem „kilka słów” zostawić obecną prośbę, by nie opisywać zdrowia; strona podziękowania `/dziekujemy/` z `noindex` jako cel zdarzenia.
- `noindex, nofollow` na całej witrynie: zdjąć, gdy Rafał uzna stronę za gotową (konieczne przed Ad Grants).

## 8. Reklamy (RSA; po 2 na grupę; nagłówki ≤30 znaków, opisy ≤90; bez przypinania poza nagłówkiem marki w grupie E)

Zasady tekstów: spokojnie, bez obietnic efektu, bez diagnozowania, bez „bezpłatne”, bez „najlepsi”, bez presji czasu. Każda reklama ma nagłówek z nazwą fundacji i jedno zdanie o procesie (rozmowa → wybór formy wsparcia).

### A1 — Psychoterapia online → /pomoc-online/ (ścieżka: /psychoterapia/online)
Nagłówki:
  - N: Psychoterapia online po polsku
  - N: Fundacja Yellow Scarf
  - N: Terapia indywidualna online
  - N: Terapia par i rodzin online
  - N: Spokojny pierwszy kontakt
  - N: Odpowiedź w ok. 2 dni robocze
  - N: Bez skierowania i diagnozy
  - N: Rozmowa o Twoich potrzebach
  - N: Koszt znasz przed startem
  - N: Spotkania online z domu
  - N: Poufność i kodeks etyki
  - N: Nie wiesz, od czego zacząć?
Opisy:
  - O: Psychoterapia online po polsku dla dorosłych. Zaczynamy od krótkiej rozmowy o potrzebach.
  - O: Razem wybieramy formę wsparcia: terapia indywidualna, par lub rodzinna. Decydujesz Ty.
  - O: Fundacja Yellow Scarf z Katowic. Spotkania online, poufność, koszt podany przed startem.
  - O: Bez skierowania i diagnozy. Napisz przez formularz lub zadzwoń w dni robocze.

### A2 — Psychoterapia online (wariant: trudniejszy moment)
Nagłówki:
  - N: Psychoterapeuta online
  - N: Fundacja Yellow Scarf
  - N: Gdy trudno sobie poradzić
  - N: Przestrzeń na rozmowę
  - N: Psychoterapia online, PL
  - N: Terapeuta mówiący po polsku
  - N: Pierwsza rozmowa bez presji
  - N: Dogodne godziny, także wieczór
  - N: Bez skierowania
  - N: Koszt znasz przed startem
  - N: Poufność i kodeks etyki
  - N: Napisz lub zadzwoń
Opisy:
  - O: Możesz czuć przeciążenie, niepokój, smutek albo utknięcie. Terapia to miejsce na rozmowę.
  - O: Nie musisz mieć wszystkiego poukładanego, zanim napiszesz. Wystarczy krótka rozmowa.
  - O: Psychoterapia online po polsku, prowadzona przez specjalistów fundacji. Poufność.
  - O: Odpowiadamy w dni robocze, zwykle do 2 dni. Koszt i zasady poznasz przed spotkaniem.

### B1 — Psycholog / konsultacja online → /pomoc-online/ (ścieżka: /psycholog/online)
Nagłówki:
  - N: Psycholog online po polsku
  - N: Konsultacja psychologiczna
  - N: Fundacja Yellow Scarf
  - N: Rozmowa z psychologiem online
  - N: Pomoc psychologiczna online
  - N: Pierwsza rozmowa bez presji
  - N: Bez skierowania
  - N: Odpowiedź w ok. 2 dni robocze
  - N: Wybierz formę wsparcia
  - N: Online z Polski i zagranicy
  - N: Poufność i kodeks etyki
  - N: Napisz lub zadzwoń
Opisy:
  - O: Konsultacja psychologiczna online. Krótka rozmowa o tym, co się dzieje i co może pomóc.
  - O: Nie musisz wiedzieć, czego szukasz. Wspólnie ustalimy: konsultacja, terapia czy grupa.
  - O: Fundacja Yellow Scarf, Katowice. Spotkania online po polsku, poufność, jasne koszty.
  - O: Bez skierowania i diagnozy. Napisz przez formularz lub zadzwoń w dni robocze, oddzwonimy.

### B2 — Psycholog online (wariant: pierwszy krok)
Nagłówki:
  - N: Porozmawiaj z psychologiem
  - N: Fundacja Yellow Scarf
  - N: Psycholog online dla dorosłych
  - N: Pierwszy krok może być mały
  - N: Konsultacja online po polsku
  - N: Jedna rozmowa, bez zobowiązań
  - N: Odpowiedź do 2 dni roboczych
  - N: Bez skierowania i diagnozy
  - N: Koszt znasz przed startem
  - N: Poufność i kodeks etyki
  - N: Spotkania online z domu
  - N: Formularz lub telefon
Opisy:
  - O: Jeśli od jakiegoś czasu jest Ci trudno, rozmowa z psychologiem może pomóc zobaczyć więcej.
  - O: Rozmowa wstępna to nie zobowiązanie. Po niej decydujesz, czy i jak chcesz kontynuować.
  - O: Pomoc psychologiczna online po polsku, prowadzona przez fundację z Katowic. Poufność.
  - O: Napisz kilka słów przez formularz albo zadzwoń w dni robocze. Odpowiemy zwykle do 2 dni.

### C1 — Grupy wsparcia online → /co-robimy/ (ścieżka: /grupy/wsparcia)
Nagłówki:
  - N: Grupa wsparcia online
  - N: Grupy wsparcia po polsku
  - N: Fundacja Yellow Scarf
  - N: Mała grupa, prowadzenie
  - N: Prowadzone przez specjalistów
  - N: Rozmowa wstępna przed grupą
  - N: Dla dorosłych, online
  - N: Zapytaj o najbliższą grupę
  - N: Koszt znasz przed startem
  - N: Bez skierowania i diagnozy
  - N: Poufność i kodeks etyki
  - N: Spotkania w stałym gronie
Opisy:
  - O: Grupy wsparcia online po polsku dla dorosłych. Małe, stałe grono, prowadzą specjaliści.
  - O: Przed dołączeniem krótka rozmowa wstępna, by sprawdzić, czy grupa odpowiada potrzebom.
  - O: Fundacja Yellow Scarf. Spotkania online, poufność, jasne koszty przed startem grupy.
  - O: Napisz przez formularz lub zadzwoń w dni robocze. Podpowiemy, która grupa rusza najbliżej.

### C2 — Grupy wsparcia (wariant: dlaczego grupa)
Nagłówki:
  - N: Grupa terapeutyczna online
  - N: Fundacja Yellow Scarf
  - N: Nie musisz być z tym sam(a)
  - N: Wsparcie innych w podobnym
  - N: Grupy wsparcia online, PL
  - N: Prowadzone przez specjalistów
  - N: Rozmowa wstępna przed grupą
  - N: Dla dorosłych, po polsku
  - N: Koszt znasz przed startem
  - N: Poufność i kodeks etyki
  - N: Zapytaj o wolne miejsca
  - N: Online, z dowolnego miejsca
Opisy:
  - O: W grupie można usłyszeć, że inni mierzą się z podobnym, i spróbować czegoś nowego.
  - O: Grupy prowadzą specjaliści fundacji. Zasady, terminy i koszt poznasz na rozmowie wstępnej.
  - O: Grupy wsparcia i terapeutyczne online po polsku, dla dorosłych z Polski i z zagranicy.
  - O: Napisz, czego szukasz, a podpowiemy, czy lepszym startem będzie grupa czy rozmowa.

### D1 — Wsparcie dla bliskich → /pomoc-online/ (ścieżka: /wsparcie/dla-bliskich)
Nagłówki:
  - N: Wsparcie dla bliskich
  - N: Martwisz się o bliską osobę?
  - N: Fundacja Yellow Scarf
  - N: Konsultacja i grupa dla bliskich
  - N: Pomoc także dla Ciebie
  - N: Rozmowa online po polsku
  - N: Dla partnerów i rodziców
  - N: Nie musisz czekać na innych
  - N: Bez skierowania
  - N: Odpowiedź w ok. 2 dni robocze
  - N: Poufność i kodeks etyki
  - N: Koszt znasz przed startem
Opisy:
  - O: Gdy bliska osoba przechodzi kryzys, Ty też potrzebujesz wsparcia. Konsultacje i grupa.
  - O: Pomoc dotyczy Twoich trudności, nawet jeśli bliska osoba nie jest gotowa szukać pomocy.
  - O: Partnerzy, rodzice, dorosłe dzieci. Rozmowy online po polsku, poufność, jasne koszty.
  - O: Fundacja Yellow Scarf. Napisz przez formularz lub zadzwoń w dni robocze. Odpowiemy.

### D2 — Wsparcie dla bliskich (wariant: pierwsza rozmowa)
Nagłówki:
  - N: Pomoc dla rodziny i bliskich
  - N: Fundacja Yellow Scarf
  - N: Gdy trudno patrzeć z boku
  - N: Rozmowa o tym, co możesz
  - N: Konsultacja online po polsku
  - N: Grupa dla bliskich online
  - N: Bez skierowania i diagnozy
  - N: Poufność i kodeks etyki
  - N: Koszt znasz przed startem
  - N: Odpowiedź do 2 dni roboczych
  - N: Zadbaj też o siebie
  - N: Formularz lub telefon
Opisy:
  - O: Bycie blisko osoby w kryzysie bywa wyczerpujące. Rozmowa z psychologiem może pomóc.
  - O: Konsultacje indywidualne i grupa dla bliskich online. Wspólnie ustalimy, co pomoże.
  - O: Fundacja Yellow Scarf, Katowice. Spotkania online po polsku, poufność i kodeks etyki.
  - O: Napisz kilka słów przez formularz lub zadzwoń w dni robocze. Oddzwonimy, zwykle do 2 dni.

### E1 — Marka → / (ścieżka: /fundacja) — nagłówek 1 przypięty: „Fundacja Yellow Scarf”
Nagłówki:
  - N: Fundacja Yellow Scarf
  - N: Pomoc psychologiczna po polsku
  - N: Fundacja z Katowic, online
  - N: Terapia, grupy, konsultacje
  - N: Wsparcie w Polsce i w Europie
  - N: KRS 0001274628
  - N: Siostrzana organizacja z UK
  - N: Jak pomagamy
  - N: Kontakt: telefon lub formularz
  - N: Poufność i kodeks etyki
Opisy:
  - O: Fundacja Yellow Scarf z Katowic. Psychoterapia, konsultacje i grupy wsparcia online.
  - O: Pomagamy osobom w Polsce i Polakom w Europie. Zaczynamy od rozmowy o potrzebach.
  - O: Założona przez brytyjską organizację Yellow Scarf CIO. Dane rejestrowe na stronie.
  - O: Napisz przez formularz lub zadzwoń w dni robocze. Odpowiadamy zwykle do 2 dni.

### E2 — Marka (wariant krótki)
Nagłówki:
  - N: Fundacja Yellow Scarf
  - N: Oficjalna strona fundacji
  - N: Yellow Scarf – pomoc po polsku
  - N: Katowice, działania online
  - N: Co robimy
  - N: Potrzebuję wsparcia
  - N: Kontakt z fundacją
  - N: Poufność i kodeks etyki
Opisy:
  - O: Oficjalna strona Fundacji Yellow Scarf. Sprawdź, jak pomagamy i jak się skontaktować.
  - O: Psychoterapia, konsultacje psychologiczne i grupy wsparcia online po polsku.
  - O: Fundacja zarejestrowana w Polsce, KRS 0001274628. Kontakt przez formularz lub telefon.

### F1 — Polski psycholog za granicą → /pomoc-online/polacy-w-europie/ (ścieżka: /po-polsku/europa)
Nagłówki:
  - N: Psycholog po polsku online
  - N: Polski psychoterapeuta online
  - N: Fundacja Yellow Scarf
  - N: Terapia po polsku za granicą
  - N: Dla Polaków w Europie
  - N: Rozmowa w Twoim języku
  - N: Online, w dogodnej porze
  - N: Bez skierowania i diagnozy
  - N: Odpowiedź w ok. 2 dni robocze
  - N: Terapia, grupy, konsultacje
  - N: Poufność i kodeks etyki
  - N: Z Niemiec, Holandii, Norwegii
Opisy:
  - O: Mieszkasz za granicą i szukasz pomocy po polsku? Psycholog i psychoterapeuta online.
  - O: Spotkania online z dowolnego kraju w Europie, w porze dopasowanej do Twojej strefy.
  - O: Fundacja Yellow Scarf z Polski. Zaczynamy od krótkiej rozmowy, bez skierowania.
  - O: Koszt podajemy przed startem. Napisz przez formularz lub zadzwoń, odpowiemy w dni robocze.

### F2 — Polski psycholog za granicą (wariant: emigracja)
Nagłówki:
  - N: Pomoc psychologiczna po polsku
  - N: Fundacja Yellow Scarf
  - N: Emigracja bywa trudna
  - N: Psycholog online dla Polaków
  - N: Rozmowa bez bariery języka
  - N: Terapia online z zagranicy
  - N: Pierwsza rozmowa bez presji
  - N: Bez skierowania
  - N: Koszt znasz przed startem
  - N: Poufność i kodeks etyki
  - N: Odpowiedź do 2 dni roboczych
  - N: Formularz lub telefon
Opisy:
  - O: Samotność, stres, tęsknota, napięcie w rodzinie. Rozmowa po polsku z psychologiem, online.
  - O: Nie musisz tłumaczyć siebie w obcym języku. Specjaliści fundacji pracują po polsku.
  - O: Fundacja Yellow Scarf. Konsultacje, psychoterapia i grupy online dla Polaków w Europie.
  - O: Napisz, gdzie mieszkasz i czego szukasz. Odpowiemy w dni robocze, zwykle do 2 dni.

### G1 — Grupy wsparcia dla Polaków za granicą → /pomoc-online/polacy-w-europie/ (ścieżka: /grupy/po-polsku)
Nagłówki:
  - N: Grupa wsparcia po polsku
  - N: Polacy za granicą – grupy
  - N: Fundacja Yellow Scarf
  - N: Emigracja: stres, samotność
  - N: Mała grupa, prowadzenie
  - N: Rozmowa wstępna przed grupą
  - N: Prowadzone przez specjalistów
  - N: Bez skierowania
  - N: Koszt znasz przed startem
  - N: Poufność i kodeks etyki
  - N: Online, z każdego kraju
  - N: Zapytaj o najbliższą grupę
Opisy:
  - O: Grupy wsparcia online po polsku dla osób mieszkających za granicą. Małe, stałe grono.
  - O: Inni w grupie też znają emigrację. Przed dołączeniem krótka rozmowa wstępna.
  - O: Fundacja Yellow Scarf z Polski. Spotkania online, poufność, koszt podany przed startem.
  - O: Napisz przez formularz lub zadzwoń w dni robocze. Podpowiemy, która grupa rusza najbliżej.

### G2 — Grupy wsparcia za granicą (wariant: rodzice i pary)
Nagłówki:
  - N: Grupy online dla Polaków
  - N: Fundacja Yellow Scarf
  - N: Dla rodziców na emigracji
  - N: Dla par i rodzin za granicą
  - N: Spotkania po polsku, online
  - N: Prowadzone przez specjalistów
  - N: Rozmowa wstępna przed grupą
  - N: Bez skierowania i diagnozy
  - N: Poufność i kodeks etyki
  - N: Koszt znasz przed startem
  - N: Odpowiedź do 2 dni roboczych
  - N: Formularz lub telefon
Opisy:
  - O: Grupy wsparcia online po polsku, także dla rodziców i par mieszkających poza Polską.
  - O: Stałe grono i prowadzenie specjalistów. Zasady i koszt poznasz na rozmowie wstępnej.
  - O: Fundacja Yellow Scarf. Jeśli grupa nie pasuje, podpowiemy konsultację indywidualną online.
  - O: Napisz kilka słów przez formularz lub zadzwoń w dni robocze. Odpowiemy zwykle do 2 dni.

## 9. Zasoby (komponenty) na poziomie konta

- **Sitelinki (4):** „Potrzebuję wsparcia” → /potrzebuje-wsparcia/ („Formularz lub telefon” / „Odpowiedź do 2 dni roboczych”); „Co robimy” → /co-robimy/ („Terapia, grupy, konsultacje” / „Online, po polsku”); „Jak to działa” → /pomoc-online/ („Trzy proste kroki” / „Bez skierowania i diagnozy”); „O fundacji” → / („Katowice, KRS 0001274628” / „Założona przez Yellow Scarf CIO”).
- **Objaśnienia:** Spotkania online · Po polsku · Bez skierowania · Poufność · Dla dorosłych · Polska i Europa.
- **Fragmenty rozszerzone (Usługi):** Konsultacja psychologiczna, Psychoterapia indywidualna, Terapia par, Grupy wsparcia, Wsparcie dla bliskich.
- **Telefon:** +48 453 088 111, harmonogram dni robocze 9–18 (do potwierdzenia godzin dyżuru).
- **Nazwa firmy / logo:** „Fundacja Yellow Scarf” — dopiero po weryfikacji reklamodawcy.
- Nie dodajemy: formularzy kontaktowych w reklamie (lead form), promocji, cen.

## 10. Kolejność wdrożenia (po akceptacji; nic nie dzieje się bez Twojego „tak”)

1. **Rafał (10 min):** zaloguj się na rafal@yellowscarf.eu → ads.google.com → „Nowe konto Google Ads” w trybie eksperta (pomiń kreator kampanii), waluta PLN, strefa Warszawa. Profil płatności: typ **organizacja**, dane dokładnie jak w KRS. Dodaj MCC 700-738-5800 jako menedżera (Admin → Dostęp i zabezpieczenia → Menedżerowie) albo przyjmij zaproszenie z MCC. Weryfikacja reklamodawcy: odpis KRS (PDF z ekrs.ms.gov.pl), odpowiedzi „organizacja, sami płacimy, bez reklam politycznych w UE”.
2. **Selten / strona (1–3 dni):** GA4 + GTM + baner zgody z Consent Mode v2, zdarzenia generate_lead / click_to_call / click_email, strona /pomoc-online/ (+ wersja dla Polaków w Europie), strona podziękowania. Zdjęcie `noindex` po Twojej decyzji.
3. **Ja (odczyt zero + jedna partia, z protokołem przed/po):** ustawienia konta (auto-apply off, Customer Match off, EC for leads off), import konwersji z GA4, lista wykluczeń, K1 i K2 w stanie **wstrzymanym**, reklamy do oceny Google, zasoby. Weryfikacja przez API przed/po.
4. **Start** po Twoim „tak”: włączenie K1 i K2, kontrola po 24 h (status reklam, wyszukiwane hasła), po 7 i 14 dniach przegląd haseł i wykluczeń.
5. **Równolegle (Rafał, 15 min):** wniosek do Google dla Organizacji Non-Profit na rafal@yellowscarf.eu (KRS, statut, cel statutowy, strona), bez zakładania konta Ads pod grant. Po weryfikacji: aktywacja Ad Grants dopiero, gdy strona jest indeksowalna.

## 11. Ryzyka i jak je ograniczamy

| Ryzyko | Skutek | Ograniczenie |
|---|---|---|
| Treści o uzależnieniach na stronie docelowej | reklamy „ograniczone”/odrzucone, groźba zawieszenia po ostrzeżeniu | osobna strona /pomoc-online/ bez tych treści; wykluczenia; przegląd statusów po 24 h |
| Brak zgody/Consent Mode | brak lub ułamkowe konwersje, słaba optymalizacja | CMP przed startem; start na Max clicks z limitem |
| Mieszanie z 798 (Polacy w UK) | podwójne koszty, chaos w danych | K2 bez UK; w 798 bez Polski; osobne konta i profile płatności |
| Odrzucenie kwalifikacji non-profit („placówka zdrowotna”) | brak Ad Grants | opisać fundację jako organizację wsparcia społecznego i edukacji; odwołanie |
| Weryfikacja reklamodawcy przeciąga się | konto wstrzymane po terminie | zacząć od razu, dokumenty zgodne z profilem płatności |
| Niski budżet rozproszony na 9 krajów | mało danych w K2 | K2 na 3–4 kraje z największą Polonią (DE, NL, IE, NO) jeśli po 30 dniach brak danych |
| Zapytania informacyjne i kryzysowe | koszt bez kontaktu, ryzyko etyczne | wykluczenia + numery alarmowe na stronie; brak reklam 24 h na hasła kryzysowe |

## 12. Czego potrzebuję od Ciebie — decyzje (odpowiedz numerami, np. „P1 A”, „P4 tak”)

- **P1.** Finansowanie: **A** konto płatne teraz (rekomenduję) / **B** tylko Ad Grants / **A+B** równolegle.
- **P2.** Budżet startowy: 1 500 PLN/mies. (50 PLN/dz) — tak / inna kwota. Kto płaci (karta fundacji? przelew?).
- **P3.** Kraje K2: DE, NL, IE, NO, BE, SE, DK, AT, CZ — tak / krótsza lista. UK zostaje wyłącznie w 798 — tak?
- **P4.** Zgoda na brak tematu uzależnień w reklamach i na osobną stronę /pomoc-online/ bez tych treści — tak?
- **P5.** Czy fundacja pracuje tylko z dorosłymi (wykluczam „dzieci/młodzież”) — tak?
- **P6.** Godziny dyżuru telefonicznego +48 453 088 111 (proponuję dni robocze 9–18).
- **P7.** GA4 / GTM / baner zgody — kto wdraża (Selten?) i czy jest już GA4 dla yellowscarf.eu.
- **P8.** Czy zdejmujemy `noindex` ze strony teraz, czy po poprawkach treści.
- **P9.** Czy mam przygotować wniosek do Google dla Organizacji Non-Profit (treść opisu misji) — tak / później.

## 13. Kontrola końcowa

- Konto: nowe, osobne dla Fundacji Yellow Scarf (PL); nie dotyka 733, 311 ani 798. ✔
- Domena: yellowscarf.eu ↔ podmiot KRS 0001274628. ✔
- Typ konta: komercyjne/płatne (wariant A); grantowe opisane osobno, bez mieszania budżetów. ✔
- Zgodność: brak uzależnień w słowach i tekstach; brak obietnic efektu, superlatyw, „bezpłatne”; brak list własnych/remarketingu; dane wrażliwe poza tagami. ✔
- Język: polski, spokojny; limity 30/90 sprawdzone skryptem (patrz niżej). ✔
- Cel: pierwszy kontakt przez formularz; mierniki i bramki ustalone. ✔
