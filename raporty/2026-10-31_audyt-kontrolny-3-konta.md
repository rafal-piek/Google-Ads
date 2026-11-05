# Audyt kontrolny trzech kont Google Ads — 31.10.2026

Zakres: Ośrodek (733-094-4080, osrodek.uk, Yellow Scarf Support CIC), Mental (311-878-5541, yellowscarftherapy.co.uk, CIC), Fundacja (798-577-2656, yellowscarf.org, Yellow Scarf CIO, Ad Grants). Dane: Google Ads API przez MCC (733, 311), panel 798 w Chrome (tylko odczyt), GA4, Search Console; odczyt 31.10.2026 08:23–08:45 UTC. Surowe dane: `raporty/dane/2026-10-31_odczyt-733-311_czesc1-3.md` w repo oraz `~/Desktop/audyt-kontrola-2026-10-31.md` i `~/Desktop/798-kontrola-2026-10-30.md` na Macu.

Okresy: **P1** = 24–30.10 (7 dni po partiach zmian z 24–25.10), **P0** = 17–23.10, **M1** = 1–30.10, **M0** = 1–30.09. Każde konto osobno, bez sumowania.

Na żadnym koncie nic nie zmieniono. Wszystkie rekomendacje poniżej wymagają Twojego „tak”.

---

## 0. Odpowiedź w jednym akapicie

Konta są technicznie w porządku: zero odrzuconych reklam, zero naruszeń zasad, automigracja Google na AI Max (1.09) nie dotknęła żadnej kampanii, auto-apply wyłączone wszędzie, po naszych zmianach z 24–25.10 nic nie wróciło i nic nie zmieniło się samo. Ośrodek ma dobry miesiąc (£92,60 za zgłoszenie w Ads przy 57 zgłoszeniach, lepiej niż we wrześniu), ale pierwszy tydzień po zmianach wygląda gorzej (9 zgłoszeń, £141) i trzeba dać mu jeszcze 2 tygodnie zanim cokolwiek ocenimy; są za to konkretne przecieki budżetu do zamknięcia (Pary 0 zgłoszeń za £539, Londyn £224 za zgłoszenie, nazwiska cudzych psychologów i angielskie hasła). Mental jest 3–8× powyżej Twojego progu kosztu zapytania (£250 za zapytanie w październiku, 2 zapytania) i test strony /therapists wystartował poprawnie, ale GA4 tego konta nie ma zdarzeń kluczowych, więc bez naprawy pomiaru nie ocenimy testu 22.11. Fundacja jest zablokowana organizacyjnie: link MCC czeka na innego administratora, grant wydaje 0,8% budżetu, a październik ma 0 konwersji, co jest formalnym ryzykiem Ad Grants.

---

## 1. Kontrola zasad i źródeł (31.10.2026)

Sprawdzone: oficjalne strony Google (Limited ad serving – update VIII.2026; AI Max for Search; Addiction services; Ad Grants account management policy en-GB; Healthcare & medicines; Personalised advertising I.2026; Child Safety X.2026) i 12 źródeł branżowych z ostatnich 12 miesięcy (lista i notatki: `raporty/2026-10-31_zrodla-kontrola-zasad.md`).

Najważniejsze ustalenia:
- **Nic nowego od 24.10, co zmieniałoby zasady dla naszych kont.** UK nadal bez programu Addiction services (lista: AU, CA, FR, IE, NZ, US). Dla psychoterapii/counsellingu w UK brak wymogu certyfikacji.
- **Automigracja na AI Max od 1.09.2026** objęła kampanie Search z Automatically Created Assets lub ustawieniem broad match na poziomie kampanii. Sprawdziłem: na 733 i 311 żadna kampania ich nie miała; AI Max wyłączony we wszystkich aktywnych kampaniach, daty migracji puste. Włączony AI Max jest tylko we WSTRZYMANEJ kampanii 311 „Google AI Test” (nie wznawiać bez przeglądu).
- **Limited ad serving** rozszerzony na Search od 12.06.2026 i na wszystkie produkty od sierpnia (pełne wdrożenie do 2028). Kryteria: dojrzałość konta, weryfikacja, jasność marki, zgłoszenia użytkowników. Zalecenie Google: marka w reklamie i na stronie, konkretny tekst, przypięcie domeny/marki na 1. pozycji nagłówka dla nowych marek. Dotyczy to głównie **Mental (nowa marka, generyczne hasła)**.
- **Ad Grants** bez zmian: CTR ≥5%/mies. na poziomie konta, ≥1 konwersja/mies., obowiązkowy Smart Bidding oparty na konwersjach (Max Conversions/Max Conv Value/tCPA/tROAS), ≥2 sitelinki, geotargeting tylko tam, gdzie usługi, ankieta roczna. Naruszenia = automatyczne zawieszenie bez powiadomienia.
- **Egzekwowanie** (źródła agencyjne, nie oficjalne): od wiosny 2026 więcej retroaktywnych odrzuceń; absolutne sformułowania („100%”, „guaranteed”) traktowane jako clickbait; reklamy w wstrzymanych kampaniach nadal mogą zbierać naruszenia final URL. U nas: skan tekstów reklam i komponentów pod BACP/NCPS/ACCPH/UKCP/„free”/„bezpłatn”/„najlepsz”/„akredyt”/„skuteczn” — **0 trafień na obu kontach**.
- **Benchmarki UK** (koszt/zgłoszenie z Search): £21,74 (Medico Digital, mental health 2025) · £51,80 (Ridley, healthcare 2026) · £72 (Weir, healthcare SME 2026) · £96,74 (Visionary, healthcare 2026). CPC: £1,02 (mental health) – £4,20–6,94 (healthcare). CTR 4,2–6,3%.

---

## 2. Co się dzieje — per konto

### 2.1 Ośrodek (733)

| Okres | Koszt | Klik. | CTR | CPC | Zgłoszenia (Ads) | Koszt/zgł. | Leads 1: utrata IS budżet / ranking |
|---|---|---|---|---|---|---|---|
| P1 24–30.10 | £1 272 | 435 | 7,4% | £2,92 | 9 | £141 | 32% / 33% |
| P0 17–23.10 | £1 211 | 407 | 5,7% | £2,98 | 13 | £93 | 42% / 15% |
| M1 październik | £5 278 | 1 894 | 6,3% | £2,79 | 57 | £92,60 | 34% / 30% |
| M0 wrzesień | £4 989 | 2 028 | 6,3% | £2,46 | 51 | £97,85 | 32% / 31% |

Kampanie, październik: Leads 1 £3 019 / 42 zgł. / **£71,87** (wrzesień £109) · PMax-1 £1 034 / 10 / £103 (wrzesień £61) · Londyn £448 / 2 / **£224** · Pary £539 / **0** (wrzesień 5 / £127) · Kryzysowa £209 / 3 / £70 · Wsparcie Rodzin £29 / 0.

Co z tego wynika:
1. **Miesiąc jest dobry, tydzień po zmianach słabszy.** Leads 1 w P1 ma wyższy CTR (13,3% vs 8,1%, bo wypadły słabe słowa i komputery), ale o 32% mniej wyświetleń, 7 zgłoszeń zamiast 11 i skok utraty udziału przez ranking z 15% do 33%. To typowy obraz tygodnia po zmianie 19 słów i stawek urządzeń: Max Conversions uczy się od nowa. Siedem dni i 9 zgłoszeń to za mało, żeby cokolwiek orzekać. Ocena partii z 24.10: **ok. 14.11** (3 tygodnie).
2. **Pary: £539 w październiku i 0 zgłoszeń**, w P1 CPC spadł do £3,79, ale strona docelowa dalej nie konwertuje (GA4: 55,6% zaangażowania, 42 s). Wrzesień dał 5 zgłoszeń, więc to nie jest trwale martwa kampania, ale do czasu przebudowy strony to najdroższy punkt konta.
3. **Londyn: £224 za zgłoszenie**; cztery z pięciu grup (Pary, Depresja, Rodziny, Trauma) wydały £133 bez zgłoszenia. Konwertuje tylko G1 „Psycholog po polsku – Londyn” (2 zgł., £158). Kampania jest na Max clicks z partnerami wyszukiwania.
4. **Przecieki w hasłach (P1, tylko widoczna część, 41% kosztu Search):** nazwiska cudzych psychologów i organizacji ok. £46/tydz. („dagmara glapa psycholog” 2 klik. £25,68, „dominik waszek”, „fundacja tvn”, „wojewódzki ośrodek… charcice”, „wielkopolskie centrum par”), hasła angielskie ok. £32/tydz. („emdr therapy”, „psychologist hull”, „cbt therapy”, „mental disorder”), formaty spoza oferty ok. £30/tydz. („książka”, „mitingi”, „anticol”, „wyjazdy terapeutyczne”, „logoterapeuta”). Po ekstrapolacji to rzędu **£400–500 miesięcznie**.
5. **Hasło kryzysowe:** „myśli samobójcze co robić” (1 klik). Ośrodek nie jest usługą kryzysową, więc takie zapytania nie powinny trafiać na reklamę — to kwestia etyczna, nie kosztowa.
6. **Grupa UZALEŻNIENIA** (Twoja decyzja: zostaje): październik £695 / 11 zgł. / £63 — ekonomicznie najlepsza po OGÓLNY. W P1 hasła alkoholowe £58 / 26 klik. / 0 zgł. Zasady: jeden nagłówek PMax („Profesjonalna Terapia Online”, grupa Competitors) ma flagę Addiction services ze statusem „ograniczone”, bez odrzucenia. Bez zmian wobec 24.10; monitorować.
7. **Test strony docelowej (eksperyment 23.10–3.12):** po 8 dniach psychologia-i-psychoterapia 5 zgł. za £320 (£64) vs umow-wizyte 2 za £265 (£133). Sygnał na korzyść strony „psychologia”, ale to 8 dni z 41. Nie ruszać.
8. **PMax-1 drożeje**: £103 za zgłoszenie w październiku vs £61 we wrześniu; utrata udziału przez ranking 60%. Pojedyncze hasło „terapia psychologiczna online” kosztowało £20,21 za 1 klik. Obserwować; przy £35/dz to nie priorytet.
9. **Pomiar:** `form_submit` w GA4 nadal odpala się 2× (2,20 zdarzenia na użytkownika). Konwersja w Ads liczy jedną na kliknięcie, więc liczby Ads są poprawne, ale GA4 zawyża. Poprawka dla Selten nadal otwarta. Logi Gośki nie mają wpisów po 17.10 — **nie znam liczby nowych pacjentów za 24–30.10**, a bramka 20.11 jest liczona z kalendarza, nie z Ads.
10. **Organic (GSC)** 28 dni: 310 klik. vs 329 (−6%), 7 dni −14%. Najczęściej klikane zapytanie nie-brandowe to **„wszywka alkoholowa uk”** (4 klik., pozycja 4,7) — usługa, której nie oferujemy (i którą wykluczamy w Ads). „polski psycholog uk za darmo” pozycja 2,4. „polski psycholog uk” pozycja 12,2 (była 10,2). Temat dla SEO, nie dla Ads.
11. Drobne: reklamy w czterech wstrzymanych kampaniach są włączone (wszystkie zatwierdzone, więc ryzyko małe); sitelinki do wpisów blogowych z 2024 w Leads 1 i PMax (£9,74/5 klik./0 zgł.); partnerzy wyszukiwania wyłączeni tylko w Leads 1, w Londyn/Pary/WR nadal włączeni; Google podsuwa ponowne włączenie partnerów w Leads 1 (odrzucić); obraz 432970087663 dodany 24.10 z „INTERNAL_TOOL” — nie wiem, kto go dodał.

### 2.2 Mental (311)

| Okres | Koszt | Klik. | CTR | CPC | Zapytania (Ads) | Koszt/zap. | Utrata IS budżet / ranking |
|---|---|---|---|---|---|---|---|
| P1 24–30.10 | £110 | 40 | 5,3% | £2,74 | 1 (telefon 28.10) | £110 | 36% / 58% |
| P0 17–23.10 | £111 | 35 | 5,2% | £3,17 | 0 | — | 20% / 72% |
| M1 październik | £501 | 163 | 5,4% | £3,07 | 2 | **£251** | 33% / 59% |
| M0 wrzesień | £491 | 159 | 5,8% | £3,09 | 4 | £123 | 39% / 52% |

Co z tego wynika:
1. **Ekonomia nadal nie działa:** £251 za zapytanie wobec Twojego progu £31–78. Wrzesień £123. Udział w wyświetleniach poniżej 10%.
2. **Test /therapists wystartował poprawnie:** 42/42 słowa mają nowy adres, status zatwierdzone, przegląd skończony; reklamy bez zmian. Pierwsze 5 dni: GA4 /therapists 15 płatnych sesji, 73% zaangażowania, 55 s (poprzedni tydzień /book-a-session: 8 sesji, 62%, 83 s); `form_start` 2 vs 0. Wynik jakości strony docelowej nadal „poniżej średniej” (5 słów z QS 2–3) — za wcześnie na zmianę. Ocena 22.11 bez zmian.
3. **Krytyczna luka pomiaru:** GA4 Mentala ma **0 zdarzeń kluczowych we wszystkich okresach** (`form_submit` nie jest oznaczony jako kluczowe), nie ma zdarzenia kliknięcia telefonu, a Ads widzi 40 kliknięć tam, gdzie GA4 widzi 24 sesje. **Bez naprawy GA4 test 22.11 ocenimy tylko po logu Nikoli i dwóch konwersjach Ads.** Log Nikoli nie ma wpisów po 22.10 — czy telefon z 28.10 (hasło „private therapist uk”) był realnym zapytaniem?
4. **Jedno słowo zjada konto:** „find a private counsellor” (dopasowanie do wyrażenia) = 84% wyświetleń i 80% kosztu w P1, 0 zapytań w P1, 1 w całym październiku za £334. Ściąga zapytania o inne ośrodki („life link glasgow”, „aisling centre enniskillen”, „willow therapy tring”) i lokalne („counselling chester/glasgow/kilmarnock/swindon”, „psychotherapist swansea”, „therapist london”) — wszystkie z 0 zapytań. 70% kosztu jest pod progiem prywatności, więc widzimy tylko wierzchołek.
5. **Limited ad serving:** Mental to młoda marka z generycznymi hasłami, czyli dokładnie profil, który Google opisuje jako ryzyko ograniczenia emisji. Reklamy mają komponent „nazwa firmy”, ale nie wiem, czy marka jest w nagłówku i przypięta. Do sprawdzenia przy przeglądzie reklam 22.11 (nie zmieniać reklam w trakcie testu strony).
6. **Organic (GSC):** 26 klik. w 28 dni vs 11 wcześniej, CTR 7,2%, pozycja 7,3 — rośnie z bardzo niskiej bazy, prawie wyłącznie brand. Zapytania o burnout na pozycjach 43–49. Jedno ciekawe: „i feel overwhelmed all the time, where can i get cheap therapy in the uk” pozycja 6.
7. Porządki: duplikat sitelinku „Therapy Fees” na poziomie konta; cztery niepodpięte listy wykluczeń („2”, „3”, „4”, „Testowa” 332 słów); wstrzymane kampanie z włączonym AI Max / rozszerzaniem URL (AI Test, PMax 2, PMax testowa) — nie wznawiać bez przeglądu.

### 2.3 Fundacja (798, Ad Grants)

| Okres | Koszt | Wyśw. | Klik. | Konw. | Uwagi |
|---|---|---|---|---|---|
| 27.09–24.10 | $0 | 0 | 0 | 0 | brak emisji |
| 24–30.10 | $5,31 | 4 | 3 | 0 | tylko [PL] Boczne drzwi (Max clicks, „Bid setting limited”); [EN] Donations (ręczny CPC) 0 wyśw. |

Co z tego wynika:
1. **Link MCC nadal „Pending”** i to nie jest kwestia kolejnego kliknięcia: konto ma zatwierdzanie wieloosobowe, wniosek z 24.10 złożył infoyellowscarf, więc zatwierdzić musi **inny administrator** — biimediaworkspace@gmail.com (dodany 8.01.2025, aktywny 31.10) albo setlen.net@gmail.com (ostatnie logowanie 29.11.2024, passkey wyłączony). Bez tego API nie odczyta konta i nie przygotuję przebudowy na danych.
2. **Bezpieczeństwo konta charytatywnego:** 4.10 wysłano wniosek o usunięcie administratora biimediaworkspace, wniosek wygasł, konto ma nadal pełne uprawnienia. Kolejność: najpierw zatwierdzenie linku, potem porządkowanie dostępów.
3. **Zgodność z Ad Grants (ryzyko formalne):** październik = 0 konwersji (wymóg ≥1/mies.) i obie kampanie na strategiach niezgodnych z wymogiem Smart Bidding (Max clicks, ręczny CPC). Google może automatycznie zmienić strategię lub zawiesić konto. Auto-apply 0/21, brak ostrzeżeń w panelu, ankieta — bez alertu.
4. Panel podsuwa zadanie „healthcare ads” z domeną **mentalhealth.org.uk** — obca domena, nie uruchamiać. Nazwa konta w nagłówku to „YELLOW SCARF CIC” (ujawnienie finansowania poprawne: CIO) — do poprawienia na nazwę CIO, żeby podmioty się nie myliły. „Drafts in progress: 1” — jest niedokończony szkic, nie wiem czyj.

---

## 3. Nasze liczby na tle rynku (październik)

| | Ośrodek Leads 1 | Mental | Benchmark UK |
|---|---|---|---|
| CTR Search | 9,2% | 5,4% | 4,2–6,3% |
| CPC | £2,76 | £3,07 | £1,02 (mental health) – £4,20–6,94 (healthcare) |
| CVR (zgł./klik.) | 3,8% | 1,2% | 4,7–5,8% |
| Koszt/zgłoszenie w Ads | £72 (konto £93) | £251 | £22 / £52 / £72 / £97 |
| Twój próg kosztu zgłoszenia | £32–63 | £31–78 | — |

Ośrodek jest w widełkach rynku healthcare, ale powyżej Twojego progu liczonego po zgłoszeniu; pamiętaj, że Ads widzi ok. 40% zgłoszeń (zgody cookies, telefony), więc rzeczywisty koszt zgłoszenia jest niższy — stąd liczymy po pacjentach z kalendarza. Mental jest poza widełkami w każdej metryce poza CTR.

---

## 4. Rekomendacje (priorytet · ryzyko · czy wymaga „tak”)

### Ośrodek (733)

| # | Rekomendacja | Priorytet | Ryzyko | Efekt |
|---|---|---|---|---|
| K1 | **Nie oceniać partii z 24.10 przed 14.11**; budżet 195 £/dz bez zmian do bramki 20.11. | wysoki | — | brak pochopnych cofnięć |
| K2 | **Wykluczenia (lista „Spoza oferty – 733”)**: hasła kryzysowe („samobójcze”, „samobójstwo”, „myśli samobójcze”); nazwiska/organizacje („dagmara glapa”, „dominik waszek”, „anita krakowiak”, „karlińska nehrebecka”, „michał brzegowy”, „fundacja tvn”, „charcice”, „nasz zapał”, „wielkopolskie centrum”, „polish psychologists association”, „centrum pomocy rodzinie”); formaty („książka”, „mitingi”, „anticol”, „wyjazdy”, „logoterapeuta”); angielskie („therapy”, „therapist”, „counselling”, „psychologist”, „psychotherapy”). | wysoki | niskie; angielskie wykluczenia zablokują też „polish psychologist” (PMax £3,57/tydz.) | ok. £400–500/mies. z powrotem w polskich hasłach |
| K3 | **Pary: wstrzymać kampanię do przebudowy strony terapia-par** i przenieść £12/dz do Leads 1 (£110→£122, +11%, bez resetu uczenia). | wysoki | średnie: utrata ewentualnych zgłoszeń par (wrzesień 5, październik 0); hasła par nadal łapie OGÓLNY | −£370/mies. zerowego wydatku; +11% budżetu tam, gdzie tracimy 34% udziału przez budżet |
| K4 | **Londyn: wstrzymać grupy G2, G3, G5, G6** (0 zgł., £133/mies.), zostawić G1; budżet £30→£20; wyłączyć partnerów wyszukiwania. | średni | niskie | koszt zgłoszenia z Londynu z £224 w stronę £150 |
| K5 | Wsparcie Rodzin (£1/dz, 0 zgł. od 2 mies.): wstrzymać. | niski | brak | porządek |
| K6 | Partnerzy wyszukiwania: wyłączyć także w Londyn/Pary/WR (spójnie z Leads 1); odrzucić podpowiedź SEARCH_PARTNERS_OPT_IN. | niski | brak | spójność |
| K7 | Sitelinki do wpisów blogowych (Leads 1 „Terapia CBT”, PMax „Blog psychologiczny”, „Blog Yellow Scarf”) zamienić na /pl/zespol.html i /pl/oferta.html. | niski | brak | lepsze dopasowanie |
| K8 | Selten: podwójny `form_submit` w GA4 (nadal); przy okazji sprawdzić, czy strona o uzależnieniach rankuje na „wszywka alkoholowa” celowo. | średni | — | czysty pomiar |
| K9 | Gośka: uzupełnić log sprzedaży od 18.10; potrzebna liczba nowych pacjentów 24–31.10 i dalej tygodniowo do bramki 20.11. | wysoki | — | bez tego bramka 20.11 nie ma danych |

Nie rekomenduję: zmian w PMax-1 (obserwacja do 14.11), zmian w UZALEŻNIENIA (Twoja decyzja), zmian w teście strony (eksperyment biegnie do 3.12), podnoszenia budżetu przed bramką.

### Mental (311)

| # | Rekomendacja | Priorytet | Ryzyko | Efekt |
|---|---|---|---|---|
| M1 | **Naprawić pomiar w GA4 311 przed 22.11**: oznaczyć `form_submit` jako zdarzenie kluczowe, dodać zdarzenie kliknięcia numeru telefonu (click_to_call) i zaimportować je do Ads jako działanie pomocnicze (secondary). Zadanie dla Selten/Ciebie, nie zmiana w kampanii. | wysoki | brak | test /therapists da się ocenić |
| M2 | **„find a private counsellor”: wariant B (mniejszy krok)** — dodać do listy „YST – Therapy Negatives Master List” wykluczenia: „life link”, „aisling”, „willow therapy”, „phone therapy” (jeśli nie oferujecie sesji telefonicznych), „near me”, oraz 15–20 nazw miast/regionów z zapytań o 0 zapytaniach (glasgow, chester, kilmarnock, swindon, swansea, london, enniskillen, tring…). Wariant A (większy krok): wstrzymać wyrażenie, dodać [find a private counsellor] w dopasowaniu ścisłym + [private counsellor online] + [find a therapist online]. Rekomenduję B teraz, A rozważyć 22.11 razem z wynikiem strony. | wysoki | B: niskie (lokalne zapytania mogą czasem konwertować, ale dotąd 0); A: spadek wolumenu o ~80% | mniej £ w zapytaniach o cudze ośrodki i miasta |
| M3 | Budżet £16,45/dz bez zmian do pierwszego płacącego klienta (Twoja decyzja z 23.10). Na 22.11 przygotować decyzję: kontynuacja vs wariant A z audytu (pauza Ads, £350–400/mies. w katalogi/GBP/SEO). | wysoki | — | — |
| M4 | Nikola: log telefonów/formularzy od 23.10, w tym czy telefon z 28.10 był realnym zapytaniem. | wysoki | — | jedyne realne źródło oceny |
| M5 | Przy przeglądzie reklam 22.11 (nie wcześniej, żeby nie zaburzać testu): sprawdzić, czy „Yellow Scarf Therapy” jest w nagłówku i rozważyć przypięcie na pozycji 1 (zalecenie Google wobec Limited ad serving). | średni | niskie | ochrona przed ograniczeniem emisji |
| M6 | Porządki: usunąć duplikat sitelinku „Therapy Fees” (konto); przejrzeć i usunąć/odpiąć listy „2”, „3”, „4”, „Testowa”; w wstrzymanej „Google AI Test” wyłączyć AI Max, żeby przypadkowe wznowienie nie włączyło automatyki. | niski | brak | higiena |

### Fundacja (798)

| # | Rekomendacja | Priorytet | Ryzyko | Efekt |
|---|---|---|---|---|
| F1 | **Zatwierdzenie linku MCC przez biimediaworkspace lub setlen.net** (Admin → Access and security → Multi-party approvals). Ty ustalasz, kto ma te konta. | wysoki | — | odblokowanie API i przebudowy |
| F2 | **Plan B, jeśli do 7.11 nie będzie akceptacji:** odczyt słów, reklam, konwersji i stawek z panelu w Chrome (tylko odczyt, Remote Control, ~20 min) i przygotowanie propozycji przebudowy (plan F4: polskie hasła „potrzebuję pomocy”, grupy wsparcia, 3 kampanie Search × 2–3 grupy, Max Conversions, UK, konwersje formularz/zapis, strony /pl/potrzebuje-pomocy i /pl/grupy-wsparcia). Wdrożenie też da się zrobić w panelu bez API. | wysoki | niskie | przestajemy czekać na Google |
| F3 | Dostępy: po zatwierdzeniu linku zdecydować o usunięciu biimediaworkspace (lub potwierdzić, że to zaufana osoba) i włączyć passkey na setlen.net lub usunąć ten login. | wysoki | — | bezpieczeństwo konta CIO |
| F4 | Nie uruchamiać zadania „healthcare ads – mentalhealth.org.uk”. Poprawić nazwę konta na „Yellow Scarf CIO” (Admin → ustawienia konta). | średni | brak | rozdział podmiotów |
| F5 | Ryzyko Ad Grants (0 konwersji w X, strategie niezgodne): zostawić do przebudowy, ale przebudowa powinna wejść w listopadzie, nie w grudniu. | wysoki | średnie: automatyczne działanie Google | — |

---

## 5. Ile i gdzie inwestować — stan na 31.10

- **Ośrodek:** 195 £/dz bez zmian do 20.11. Dźwignią nie jest więcej pieniędzy, tylko przesunięcie wewnątrz konta: Pary (£12) i część Londynu (£10) do Leads 1, które traci 34% udziału przez budżet przy £72 za zgłoszenie. Po bramce 20.11 (koszt pacjenta < £150 i ≥ 44 nowych pacjentów w listopadzie) 215 £/dz od 1.01.2027 — tak jak ustalone.
- **Mental:** £500/mies. bez zmian. Decyzja 22.11 na podstawie logu Nikoli, konwersji Ads i (po naprawie) GA4.
- **Fundacja:** $0 wydane z $10 000/mies. Odblokowanie linku lub plan B to jedyna inwestycja, która ma sens — czas, nie pieniądze.

---

## 6. Czego potrzebuję od Ciebie

1. **„Tak” lub „nie” osobno** dla: K2, K3, K4, K5, K6, K7 (Ośrodek) oraz M2 wariant B, M6 (Mental). Wykonam jedną partią przez Chrome z odczytem API przed i po.
2. **Fundacja:** kto ma dostęp do biimediaworkspace@gmail.com i setlen.net@gmail.com, i czy mogę uruchomić plan B (F2), jeśli do 7.11 nie będzie akceptacji.
3. **Dane z kalendarza:** nowi pacjenci Ośrodka 24–31.10 (Gośka) i zapytania Mentala 23–31.10 (Nikola), oraz uzupełnienie logów co tydzień do 20.11.
4. **Dwa pytania:** czy Mental oferuje sesje telefoniczne (decyduje o wykluczeniu „phone therapy”); kto dodał obraz do konta 733 w dniu 24.10 (narzędzie wewnętrzne, obraz bez tekstu).
5. **Selten:** zlecenie GA4 733 (podwójny form_submit) i GA4 311 (zdarzenia kluczowe + telefon) — treść zadania mogę przygotować.

Następne kontrole: **14.11** (ocena partii z 24.10 na 733, 3 tygodnie danych), **20.11** (bramka 733), **22.11** (test /therapists na 311). Fundacja: po Twoim sygnale lub plan B od 7.11.
