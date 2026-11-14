# Fundacja (798-577-2656) — propozycja przebudowy kampanii Google Ad Grants (plan F4)

Data: 2.11.2026 · Konto: Fundacja, Google Ad Grants, waluta USD · Strona: https://www.yellowscarf.org · Podmiot: Yellow Scarf CIO (charity 1190615) · Status dokumentu: **do akceptacji Rafała, nic nie zostało zmienione**.
Dane: odczyt panelu 2.11.2026 (`raporty/dane/2026-11-02_odczyt-798.md`), strony yellowscarf.org (2.11), zasady Ad Grants sprawdzone 2.11 (`raporty/2026-11-02_zrodla-ad-grants.md`), audyty 24.10 i 31.10.
To konto nie jest mieszane z Ośrodkiem (733, CIC) ani Mentalem (311, CIC). Budżet grantu nie jest gotówką CIC.

---

## 0. W skrócie

Grant $10 000 miesięcznie jest praktycznie nieużywany: od 1 sierpnia konto wydało $9,16, zebrało 5 kliknięć i 0 konwersji. Nie dlatego, że Google blokuje konto, tylko dlatego, że obie kampanie stoją na strategiach z limitem $2 za kliknięcie, 44 z 95 słów nie ma wolumenu, a jedyne mierzone zdarzenie to kliknięcie w darowiznę. Formularz „Potrzebuję pomocy” nie jest liczony w ogóle.

Proponuję przebudowę w trzech krokach, bez API (w panelu, przez Chrome, jedną partią po Twoim „tak”):
1. **Porządki i pomiar** (tydzień 1): nazwa konta, odpięcie GA4 Ośrodka, usunięcie objaśnień Ośrodka, wyłączenie Customer Match i rozszerzonych konwersji, zdarzenia GA4 dla formularza i zapisu na grupę (Selten).
2. **Nowa struktura** (tydzień 1–2): 3 kampanie Search na Maksymalizacji konwersji, 7 grup reklam, słowa 2–4-wyrazowe, wspólna lista wykluczeń, nowe RSA bez odrzuconych treści, sitelinki z poprawnymi adresami.
3. **Ocena** 2.12.2026 (30 dni) i 5.01.2027 (60 dni): CTR ≥ 5%, ≥ 1 konwersja miesięcznie, liczba zgłoszeń PL, pierwsze zapisy na grupy.

Cel biznesowy, do którego to prowadzi: 4 grupy po 6–8 płacących uczestników w 2026/27. Realistycznie w pierwszym kwartale emisji: 5–15 zgłoszeń PL miesięcznie i 1–3 zapisy na grupy. Ad Grants nie da więcej niż pozwala wolumen polskich zapytań o pomoc w UK; to jest kanał tani, ale wąski.

Potrzebuję od Ciebie 9 decyzji (§13). Najważniejsze trzy: czy pierwszy kontakt i infolinia są bezpłatne (od tego zależą słowa „bezpłatna pomoc”), czy mogę zdjąć z reklam EN twierdzenia o 200 osobach na liście oczekujących i infolinii, oraz czy wstrzymujemy kampanię EN Donations.

---

## 1. Co się dzieje (fakty z odczytu 2.11)

| Obszar | Stan | Co to znaczy |
|---|---|---|
| Kampanie | 2 aktywne: [PL] Boczne drzwi – Społeczność ($100/dz, Maximise clicks, limit $2, „Bid setting limited”), [EN] Donations ($329,60/dz, Manual CPC) | Obie strategie są poza wymogiem Smart Bidding Ad Grants; EN od 30 dni ma 0 wyświetleń |
| Wyniki 1.08–2.11 | 11 wyśw., 5 klik., $9,16, 0 konw.; ostatnie 30 dni: 4 wyśw., 3 klik., $5,31 | Wydatek ok. $0,18 dziennie z $429,60 zaplanowanych |
| Słowa | 95; 44 Low search volume, 3 poniżej stawki 1. strony ($8,90–15,58), 48 Eligible; klika tylko „wsparcie dla polaków” | Lista jest za długa i za „życzeniowa”; realny wolumen mają 2–3-wyrazowe frazy o pomocy po polsku |
| Reklamy | 10 RSA; EN „Excellent”, PL „Average/Good”; #3 „Addiction services – Not allowed in UK” (4 nagłówki odrzucone) | Treści o uzależnieniach ograniczają emisję w UK; reszta OK |
| Konwersje | donate_click (Primary, GA4), Połączenia (Primary, telefon odrzucony), 4 działania śmieciowe Secondary; 0 konwersji | Formularz „Potrzebuję pomocy” i zapis na grupę nie są mierzone; Smart Bidding nie ma na czym się uczyć |
| GA4 | 538419573 (Fundacja) + **277882249 (stara usługa Ośrodka, import odbiorców ON)** | Mieszanie podmiotów na koncie charity |
| Zasoby | Objaśnienia kontowe „Polski Terapeuta w UK”, „Osrodek Terapeutyczny”, „Terapia Przez Internet” nadal Eligible; sitelinki „Jak Pomagamy”/„Grupy Wsparcia” ograniczone (Health); telefon 01905570235 odrzucony (niezweryfikowany) | Oferta komercyjna Ośrodka na koncie CIO; brak działającego telefonu |
| Ustawienia | Customer Match ON, Conversion-based lists ON, Enhanced conversions Recording, 1 segment w Customer lifecycle | Dane osób szukających pomocy psychologicznej — do wyłączenia (UK GDPR, kategoria wrażliwa) |
| Admin | Nazwa „YELLOW SCARF CIC”; 3 adminów Gmail; link MCC „Pending admin review” od 24.10 | Do poprawy nazwa; link czeka na Setlena |
| Szkic | „Draft: Leads-Performance Max- Strona Fundacjii” (PMax, autor nieznany) | Do usunięcia, chyba że to Twój szkic |
| Auto-apply | 0/21 od 24.10 | OK |
| Alerty Ad Grants | brak | Zapasu nie ma: 0 konwersji przez cały okres |

Strony docelowe (sprawdzone 2.11): `/pl/potrzebuje-pomocy.html` (formularz: imię*, nazwisko*, e-mail*, telefon*, opis sytuacji, zgoda; brak numeru telefonu, brak informacji, czy kontakt jest bezpłatny), `/pl/jak-pomagamy.html` (Grupy Wstępne £50/mies., Grupy Terapeutyczne £120/mies., Terapia indywidualna £50/h; wzmianki o nałogu), `/pl/nasze-projekty.html`, `/pl/chce-pomoc.html`, `/pl/donate.html`, `/en-gb/i-need-help.html`, `/en-gb/our-projects.html` (Gambling Support – grupy co tydzień w Worcester i Evesham; Yellow CAT; Ukrainian Walkie Talkie), infolinia +44 7340 634326 pn–pt 10–16 (strona główna EN).

---

## 2. Cel, mierniki, bramki

| Co mierzymy | Skąd | Próg Ad Grants | Nasz cel na 30 dni | Nasz cel na 60 dni |
|---|---|---|---|---|
| CTR konta | panel | ≥ 5% miesięcznie | ≥ 8% | ≥ 8% |
| Konwersje | GA4 → Ads | ≥ 1 miesięcznie | ≥ 5 zgłoszeń PL | ≥ 10 zgłoszeń PL, ≥ 1 zapis na grupę |
| Wydatek | panel | brak minimum | $150–400 | $400–900 |
| Zgłoszenia realne | skrzynka info@ / log Fundacji | — | prowadzić log jak u Gośki: data, źródło, czy zapis | j.w. |
| Zapisy na grupy | log | — | 1–3 | 3–6 |

Decyzje o rozwoju (więcej grup, PMax z Maps) podejmujemy po logu zgłoszeń, nie po konwersjach Ads.

---

## 3. Zasady, które wiążą (sprawdzone 2.11.2026)

Pełna notatka: `raporty/2026-11-02_zrodla-ad-grants.md`. W skrócie: CTR ≥ 5%/mies. (dwa miesiące poniżej → dezaktywacja); ≥ 1 znacząca konwersja/mies.; konwersyjne Smart Bidding (Maksymalizacja konwersji znosi limit $2); zakaz słów jednowyrazowych i zbyt ogólnych; Wynik Jakości 1–2 → pauza; ≥ 2 grupy na kampanię, ≥ 2 RSA na grupę, ≥ 2 sitelinki; kierowanie geograficzne; logowanie co miesiąc; coroczna ankieta; strona z misją, adresem, numerem rejestrowym, bez dominującej sprzedaży i z wyjaśnieniem, jak wpływy wspierają misję. Addiction services: w UK treści o leczeniu uzależnień od alkoholu i narkotyków są ograniczane (reklama #3 to pokazuje); hazard jako uzależnienie behawioralne jest poza tą polityką, ale panel może flagować ręcznie.

Dla komunikacji: żadnych obietnic efektów, żadnego „bezpłatnie”, jeśli usługa jest płatna, żadnego diagnozowania odbiorcy, spokojny ton.

---

## 4. Proponowana struktura

| # | Kampania | Cel | Geo / język | Strategia | Budżet $/dz | Grupy reklam | Strona docelowa |
|---|---|---|---|---|---|---|---|
| K1 | **[PL] Pomoc po polsku w UK** (nowa; obecna PL przebudowana, nie usuwana) | zgłoszenia z formularza, zapisy na grupy | UK, „Presence” (nie „presence or interest”); języki polski + angielski | Maksymalizacja konwersji, bez tCPA | 120 | A. Pomoc psychologiczna po polsku · B. Grupy wsparcia po polsku · C. Emigracja: samotność, stres, kryzys | A, C → /pl/potrzebuje-pomocy.html · B → /pl/jak-pomagamy.html |
| K2 | **[PL] Fundacja Yellow Scarf** | marka, wolontariat, darowizny PL | UK, Presence; PL + EN | Maksymalizacja konwersji | 30 | D. Marka · E. Chcę pomóc (wolontariat, darowizna) | D → /pl/ · E → /pl/chce-pomoc.html, /pl/donate.html |
| K3 | **[EN] Midlands – Support groups** | zapisy do grup lokalnych | Worcestershire + Birmingham (promień 40 km od Evesham i Worcester), Presence; EN + PL | Maksymalizacja konwersji | 80 | F. Gambling support groups Worcester/Evesham · G. Eastern European community support | F → /en-gb/our-projects.html (docelowo osobna strona) · G → /en-gb/i-need-help.html |
| K4 | [EN] Donations – Yellow Scarf (istniejąca) | darczyńcy | UK | **propozycja: PAUZA** do 5.01.2027; wariant B: Maksymalizacja konwersji, $49 | 0 (B: 49) | istniejące 2 grupy, bez 3 drogich fraz | /en-gb/donate.html |
| | **Razem** | | | | **230 (B: 279)** z 329 | | |

Dlaczego tak: trzy kampanie to minimum, które rozdziela trzy różne zamiary (szukam pomocy po polsku / chcę pomóc lub znam markę / szukam lokalnej grupy po angielsku) i trzy różne strony. Więcej kampanii nie pomoże przy tym wolumenie, a utrudni prowadzenie. Budżety są wysokie celowo: w grancie nie ryzykujemy gotówki, a wysoki budżet nie ogranicza Smart Biddingu. Realny wydatek w pierwszym miesiącu to raczej $5–20 dziennie.

Ustawienia wspólne: tylko sieć wyszukiwania, bez partnerów i bez sieci reklamowej; AI Max wyłączony; rozszerzenie końcowego URL wyłączone; automatyczne komponenty wyłączone; rotacja „Optymalizuj”; cele konwersji ustawione na poziomie kampanii (K1–K3: formularz + zapis na grupę; K4: donate_click); brak list odbiorców.

---

## 5. Słowa kluczowe (dopasowanie do wyrażenia + ścisłe; bez słów jednowyrazowych)

Zasada: każda fraza ma 2–4 wyrazy i wyraża zamiar; frazy z „psycholog/psychoterapeuta/terapeuta” zostawiamy Ośrodkowi (733), żeby dwa konta nie licytowały przeciw sobie. Frazy „za darmo/bezpłatny” wchodzą tylko, jeśli potwierdzisz, że pierwszy kontakt i infolinia są bezpłatne (decyzja D1); inaczej idą do wykluczeń.

**A. Pomoc psychologiczna po polsku (K1)** — 14 fraz
"pomoc psychologiczna po polsku", "pomoc psychologiczna po polsku uk", "pomoc psychologiczna dla polaków w uk", "pomoc psychologiczna dla polaków w anglii", "wsparcie psychologiczne po polsku", "wsparcie psychologiczne dla polaków", "wsparcie emocjonalne po polsku", "potrzebuję pomocy psychologicznej", "gdzie szukać pomocy psychologicznej w uk", "pomoc psychologiczna online po polsku", "polska fundacja pomoc psychologiczna", "pomoc dla polaków w uk", "wsparcie dla polaków w uk" (dziś jedyne klikane), "pomoc psychologiczna emigracja"
Warunkowo (D1): "bezpłatna pomoc psychologiczna uk", "darmowa pomoc psychologiczna po polsku", "polski psycholog uk za darmo" (GSC Ośrodka: pozycja 1,6 i 209 wyśw./mies. — to zapytanie dziś trafia na stronę komercyjną).

**B. Grupy wsparcia po polsku (K1)** — 12 fraz
"grupa wsparcia po polsku", "grupy wsparcia po polsku", "grupy wsparcia dla polaków", "grupa wsparcia online po polsku", "polskie grupy wsparcia w uk", "polska grupa wsparcia w anglii", "grupa terapeutyczna po polsku", "terapia grupowa po polsku", "terapia grupowa online po polsku", "grupa wsparcia dla emigrantów", "grupa wsparcia zdrowie psychiczne po polsku", "tania pomoc psychologiczna uk"
Uwaga: „terapia grupowa” wymaga zdjęcia z kampanii PL wykluczeń „terapia / terapii / terapię” (decyzja D5); zostają „terapeuta”, „psychoterapeuta”, „psychoterapia”, „psycholog” jako frazy Ośrodka.

**C. Emigracja: samotność, stres, kryzys (K1)** — 12 fraz
"samotność na emigracji", "samotność w uk", "stres na emigracji", "trudności na emigracji", "nie radzę sobie na emigracji", "depresja na emigracji", "depresja po polsku uk", "lęk na emigracji", "kryzys psychiczny pomoc po polsku", "wypalenie na emigracji", "jak poradzić sobie z samotnością w uk", "pomoc w kryzysie po polsku"
Bez: haseł o myślach samobójczych, przemocy, uzależnieniach (idą do wykluczeń; Fundacja nie jest służbą kryzysową).

**D. Marka (K2)** — 6 fraz
"yellow scarf", "yellow scarf fundacja", "fundacja yellow scarf", "yellow scarf evesham", "yellow scarf charity", "yellowscarf org" — marka to dozwolony wyjątek od zakazu słów jednowyrazowych; na wszelki wypadek wszystkie są dwuwyrazowe.

**E. Chcę pomóc (K2)** — 8 fraz
"wolontariat polska organizacja uk", "wolontariat dla polaków w uk", "jak pomóc polakom w uk", "darowizna polska fundacja uk", "wesprzyj polską fundację w uk", "polska organizacja charytatywna uk", "polska fundacja w anglii", "wsparcie polskiej społeczności uk"
Uwaga: „wolontariat” jest dziś wykluczony w kampanii PL — w K2 go nie wykluczamy.

**F. Gambling support groups (K3)** — 10 fraz
"gambling support group worcester", "gambling support group evesham", "gambling support worcestershire", "help with gambling worcester", "gambling addiction support group near me", "support for families of gamblers worcester", "problem gambling help worcestershire", "gambling recovery group worcester", "polish gambling support uk", "gamblers support group midlands"
Ryzyko: panel może sklasyfikować pod „Addiction services” mimo że hazard jest poza polityką; monitorować status po 48 h, w razie flagi przenieść słowa na „problem gambling support” i zgłosić odwołanie.

**G. Eastern European community support (K3)** — 8 fraz
"polish community support worcester", "eastern european support group midlands", "polish speaking support group uk", "mental health support polish community", "support for polish people in worcestershire", "ukrainian support group worcestershire", "walk and talk group worcestershire", "community support group evesham"

**Istniejące słowa:** 44 fraz Low search volume do usunięcia (nie szkodzą, ale zaciemniają), 3 drogie frazy o darowiznach do usunięcia; reszta EN zostaje w K4 (jeśli wariant B). Słowa z dopasowaniem przybliżonym (10 w PL) zamieniamy na wyrażenie.

### Wykluczenia — nowa lista współdzielona „Spoza oferty – 798”, podpięta do K1–K4

Przenosimy obecne 97 wykluczeń z poziomu kampanii i dodajemy:
- **komercyjne / Ośrodek i Mental:** "prywatny psycholog", "psycholog prywatnie", "cennik psycholog", "psychoterapeuta online", "psycholog dziecięcy", "terapia par", "terapia małżeńska", "osrodek", "ośrodek terapii", "yellow scarf therapy", "yellowscarftherapy"
- **kryzysowe (nie jesteśmy służbą kryzysową):** "myśli samobójcze", "samobójstwo", "chcę umrzeć", "nie chcę żyć", "samookaleczenia", "przemoc domowa pomoc", "999", "111", "samaritans", "szpital psychiatryczny"
- **uzależnienia (UK, Addiction services):** "leczenie uzależnień", "terapia uzależnień", "odwyk", "detoks", "wszywka", "esperal", "narkotyki pomoc", "alkohol pomoc" (oprócz już wykluczonych form „alkoholik/uzależnienia/współuzależnienie/aa/dda”)
- **leki i diagnozy:** "leki", "antydepresanty", "psychiatra", "diagnoza adhd", "recepta"
- **inne organizacje:** "mind", "samaritans", "nhs talking therapies", "iapt", "polish psychologists association", "pca", "caritas" (już), "opoka", "centrum pomocy rodzinie"
- **praca/nauka/forma:** "praca", "kurs", "szkolenie", "studia", "staż", "książka", "pdf", "forum", "test", "quiz", "definicja", "co to jest" (część już jest)
- **angielskie ogólne w kampaniach PL (tylko K1, K2):** "therapist", "counsellor", "psychologist", "therapy near me", "counselling near me"
- **EN K3/K4:** "casino", "betting", "odds", "free bets", "bookmaker", "gambling app", "jobs", "volunteer jobs", "charity shop", "donate clothes" (już), "free counselling", "nhs"

Odpowiedzi „bezpłatny/darmowy/za darmo” dodajemy do wykluczeń **tylko** gdy D1 = „nie”.

---

## 6. Reklamy (RSA; każda grupa ≥ 2; nagłówki ≤ 30 znaków, opisy ≤ 90; bez przypinania poza H1 w grupie D)

Zasady treści: zero obietnic efektu, zero „bezpłatnie” (do czasu D1), zero słów o uzależnieniach w PL (Addiction services), numer charity w każdej reklamie, spokojny ton. Twierdzenia „Działamy od 2011” i „ponad 200 osób na liście” wchodzą tylko po D3.

### A1 — Pomoc psychologiczna po polsku → /pl/potrzebuje-pomocy.html (ścieżka: /pomoc/po-polsku)
Nagłówki:
- `Pomoc psychologiczna po polsku`
- `Wsparcie dla Polaków w UK`
- `Fundacja Yellow Scarf`
- `Zarejestrowana charity 1190615`
- `Napisz, odezwiemy się`
- `Rozmowa w Twoim języku`
- `Nie musisz być z tym sam`
- `Pierwszy krok jest prosty`
- `Wsparcie online w całym UK`
- `Grupy wsparcia po polsku`
- `Poufnie i bez oceniania`
- `Organizacja non-profit w UK`
- `Krótki formularz kontaktowy`
- `Wsparcie emocjonalne po polsku`
- `Pomoc dla Polaków w Anglii`
Opisy:
- `Jeśli jest Ci trudno, napisz do nas. Odpowiemy po polsku i wspólnie zobaczymy, co dalej.`
- `Yellow Scarf CIO, zarejestrowana charity 1190615. Wspieramy Polaków w UK po polsku.`
- `Grupy wsparcia online po polsku. Poufna rozmowa z ludźmi, którzy rozumieją emigrację.`
- `Nie musisz mieć wszystkiego poukładanego, żeby się odezwać. Wypełnij krótki formularz.`

### A2 — Pomoc psychologiczna po polsku (wariant: pierwszy kontakt)
Nagłówki:
- `Potrzebujesz pomocy po polsku?`
- `Napisz do Yellow Scarf`
- `Odpowiadamy po polsku`
- `Polska organizacja w UK`
- `Charity nr 1190615`
- `Wsparcie psychologiczne w UK`
- `Zacznij od jednej wiadomości`
- `Spokojnie, krok po kroku`
- `Bez skierowania i kolejki`
- `Spotkania online po polsku`
- `Dla Polaków w całym UK`
- `Z siedzibą w Evesham`
- `Możesz napisać anonimowo`
- `Wsparcie w trudnym czasie`
- `Jesteśmy po to, by słuchać`
Opisy:
- `Opisz w kilku zdaniach, co się dzieje. Odezwiemy się i podpowiemy, co może pomóc.`
- `Polska charity w UK. Grupy wsparcia, spotkania online i pomoc w Twoim języku.`
- `Nie oceniamy i nie diagnozujemy. Pomagamy znaleźć wsparcie dopasowane do Twojej sytuacji.`
- `Charity nr 1190615 z siedzibą w Evesham. Działamy online dla Polaków w całym UK.`
Uwaga: „Możesz napisać anonimowo” tylko jeśli formularz przestanie wymagać nazwiska (zadanie dla Seltena, §9).

### B1 — Grupy wsparcia po polsku → /pl/jak-pomagamy.html (ścieżka: /grupy/wsparcia)
Nagłówki:
- `Grupy wsparcia po polsku`
- `Spotkania online po polsku`
- `Grupa wstępna od £50/mies.`
- `Grupa terapeutyczna £120/mies.`
- `Prowadzone przez specjalistów`
- `Fundacja Yellow Scarf`
- `Charity nr 1190615`
- `Dla Polaków w całym UK`
- `Razem łatwiej niż w pojedynkę`
- `Małe, zamknięte grupy`
- `Zapisz się na grupę`
- `Pierwszy krok bez presji`
- `Wsparcie w Twoim języku`
- `Niska opłata, pełne wsparcie`
- `Nowe grupy ruszają cyklicznie`
Opisy:
- `Grupa wstępna £50/mies. stabilizuje sytuację. Grupa terapeutyczna £120/mies. idzie dalej.`
- `Spotkania online po polsku w małych grupach. Opłaty wspierają misję charity nr 1190615.`
- `Zobacz, jak działają nasze grupy, i zapisz się. Odezwiemy się i dobierzemy grupę razem.`
- `Yellow Scarf to polska charity w UK. Grupy prowadzą doświadczeni specjaliści.`
Uwagi: „Małe, zamknięte grupy”, „Nowe grupy ruszają cyklicznie” i „Prowadzone przez specjalistów” — potwierdź, że to prawda (D4). Ceny muszą zgadzać się ze stroną w dniu startu.

### B2 — Grupy wsparcia po polsku (wariant: dlaczego grupa)
Nagłówki:
- `Polskie grupy wsparcia w UK`
- `Grupa terapeutyczna online`
- `Grupa wstępna po polsku`
- `Yellow Scarf CIO`
- `Charity nr 1190615`
- `Ludzie, którzy rozumieją`
- `Rozmowa, która pomaga`
- `Regularne spotkania online`
- `Dołącz do grupy po polsku`
- `Od £50 miesięcznie`
- `Dla osób na emigracji`
- `Bez oceniania, z uwagą`
- `Sprawdź, jak to działa`
- `Wsparcie grupowe po polsku`
- `Zapisy przez stronę`
Opisy:
- `W grupie słyszysz, że nie tylko Ty tak masz. Spotkania online po polsku ze specjalistą.`
- `Grupa wstępna £50/mies., terapeutyczna £120/mies. Opłaty wspierają misję charity 1190615.`
- `Sprawdź opisy grup i zapisz się przez stronę. Odpowiemy po polsku i pomożemy wybrać grupę.`
- `Yellow Scarf CIO wspiera Polaków w UK. Grupy online dla osób, którym jest trudno.`

### C1 — Emigracja: samotność, stres, kryzys → /pl/potrzebuje-pomocy.html (ścieżka: /emigracja/wsparcie)
Nagłówki:
- `Samotność na emigracji?`
- `Trudno Ci w UK? Napisz`
- `Wsparcie po polsku w UK`
- `Fundacja Yellow Scarf`
- `Charity nr 1190615`
- `Rozumiemy życie na emigracji`
- `Nie musisz radzić sobie sam`
- `Spotkania online po polsku`
- `Spokojna rozmowa po polsku`
- `Pomoc w trudnym momencie`
- `Krótki formularz, odpowiemy`
- `Dla Polaków w całym UK`
- `Poufnie i z szacunkiem`
- `Pierwszy krok może być mały`
- `Grupy dla osób na emigracji`
Opisy:
- `Stres, samotność, zmęczenie emigracją. Napisz, odpowiemy po polsku i podpowiemy, co dalej.`
- `Polska charity w UK (1190615). Grupy wsparcia i spotkania online dla osób na emigracji.`
- `Nie oceniamy i nie spieszymy. Wspólnie zobaczymy, jaka forma wsparcia ma dla Ciebie sens.`
- `Wiele osób na emigracji zna to uczucie. Rozmowa po polsku może być pierwszym krokiem.`

### C2 — Emigracja (wariant: codzienność)
Nagłówki:
- `Życie w UK Cię przerosło?`
- `Porozmawiaj po polsku`
- `Wsparcie emocjonalne w UK`
- `Yellow Scarf CIO`
- `Charity nr 1190615`
- `Grupy wsparcia online`
- `Dla Polaków za granicą`
- `Napisz, kiedy będziesz gotów`
- `Bez skierowania`
- `Odpowiadamy w dni robocze`
- `Zmęczenie, stres, samotność`
- `Słuchamy bez oceniania`
- `Wsparcie, nie presja`
- `Siedziba: Evesham, UK`
- `Wypełnij krótki formularz`
Opisy:
- `Praca, dzieci, tęsknota za domem. Jeśli brakuje Ci sił, napisz. Odpowiemy po polsku.`
- `Yellow Scarf CIO: polska charity w UK. Spotkania i grupy wsparcia online po polsku.`
- `Nie musisz nazywać tego, co czujesz. Opisz sytuację własnymi słowami, reszta razem.`
- `Wsparcie dla Polaków w UK od charity nr 1190615. Krótki formularz na stronie, odpowiemy.`

### D1 — Marka → /pl/ (ścieżka: /fundacja)
Nagłówki (H1 przypięty: „Yellow Scarf: oficjalna strona”):
- `Yellow Scarf: oficjalna strona`
- `Polska fundacja w UK`
- `Charity nr 1190615`
- `Grupy wsparcia po polsku`
- `Potrzebuję pomocy`
- `Chcę pomóc`
- `Nasze projekty`
- `Siedziba w Evesham`
- `Spotkania online po polsku`
- `Zobacz, jak pomagamy`
- `Kontakt z fundacją`
- `Wsparcie dla Polaków w UK`
Opisy:
- `Yellow Scarf CIO, charity nr 1190615. Grupy wsparcia, projekty społeczne, pomoc po polsku.`
- `Potrzebujesz wsparcia albo chcesz pomóc? Zobacz, jak działamy i jak się skontaktować.`
- `Polska charity z siedzibą w Evesham. Działania online dla Polaków w całym UK.`
- `Projekty, grupy wsparcia i społeczność. Poznaj Yellow Scarf i dołącz do nas.`

### D2 — Marka (wariant krótki)
Nagłówki:
- `Yellow Scarf CIO`
- `Fundacja Yellow Scarf UK`
- `Oficjalna strona fundacji`
- `Charity nr 1190615`
- `Pomoc po polsku w UK`
- `Grupy i projekty społeczne`
- `Dołącz lub wesprzyj`
- `Kontakt i zapisy`
- `Evesham, Worcestershire`
- `Dla Polaków w całym UK`
Opisy:
- `Oficjalna strona Yellow Scarf CIO. Sprawdź aktualne grupy, projekty i możliwości wsparcia.`
- `Zarejestrowana organizacja charytatywna (1190615). Wspieramy Polaków w UK od lat.`
- `Potrzebujesz pomocy lub chcesz pomóc? Wszystkie informacje i kontakt w jednym miejscu.`

### E1 — Chcę pomóc → /pl/chce-pomoc.html (ścieżka: /chce/pomoc)
Nagłówki:
- `Chcesz pomóc Polakom w UK?`
- `Wolontariat w Yellow Scarf`
- `Wesprzyj polską fundację`
- `Charity nr 1190615`
- `Darowizna od £5 miesięcznie`
- `Twoje wsparcie ma znaczenie`
- `Pomagaj razem z nami`
- `Polska organizacja w UK`
- `Zobacz, jak możesz pomóc`
- `Wolontariat online i lokalnie`
- `Wspieramy Polaków na emigracji`
- `Każda kwota się liczy`
- `Dołącz do zespołu`
- `Przejrzyste finanse`
- `Siedziba w Evesham`
Opisy:
- `Wolontariat, darowizna albo Twój czas i wiedza. Zobacz, jak możesz wesprzeć Yellow Scarf.`
- `Darowizny finansują grupy wsparcia i projekty dla Polaków w UK. Charity nr 1190615.`
- `Szukamy wolontariuszy do działań online i lokalnych w Worcestershire. Napisz do nas.`
- `Każda regularna darowizna pomaga planować kolejne grupy. Wesprzyj nas od £5 miesięcznie.`
Uwaga: „Przejrzyste finanse” tylko, jeśli na stronie są sprawozdania (Charity Commission) — inaczej pomijamy.

### E2 — Chcę pomóc (wariant: darowizna)
Nagłówki:
- `Wesprzyj Polaków w UK`
- `Darowizna dla Yellow Scarf`
- `Charity nr 1190615`
- `Od £5 miesięcznie`
- `Finansujemy grupy wsparcia`
- `Polska fundacja w UK`
- `Jednorazowo lub co miesiąc`
- `Bezpieczna płatność online`
- `Zobacz, na co idą darowizny`
- `Pomóż nam pomagać`
Opisy:
- `Darowizna finansuje grupy wsparcia i spotkania online po polsku. Charity nr 1190615.`
- `Wpłać jednorazowo lub ustaw stałe zlecenie od £5. Każda kwota wspiera Polaków w UK.`
- `Zobacz, na co idą darowizny, i wesprzyj nasze działania w Worcestershire i online.`

### F1 — Gambling support groups → /en-gb/our-projects.html (docelowo /en-gb/gambling-support.html; ścieżka: /gambling/support)
Nagłówki:
- `Gambling Support Groups`
- `Weekly Groups in Worcester`
- `Weekly Groups in Evesham`
- `For You or Your Family`
- `Registered Charity 1190615`
- `Led by Qualified Therapists`
- `Confidential and Local`
- `Yellow Scarf CIO`
- `A First Step, at Your Pace`
- `1:1 Sessions When Needed`
- `Support in English or Polish`
- `Get in Touch Today`
- `Worcestershire Charity`
- `You Are Not Alone in This`
- `Small, Supportive Groups`
Opisy:
- `Weekly groups in Worcester and Evesham for people affected by gambling and their families.`
- `Led by a therapist and a psychologist. 1:1 sessions and workshops available when needed.`
- `Yellow Scarf CIO is a registered charity (1190615) in Evesham. Get in touch to learn more.`
- `A confidential space to talk about gambling and its impact, in English or Polish.`

### F2 — Gambling support (wariant: rodzina)
Nagłówki:
- `Worried About Their Gambling?`
- `Support for Families`
- `Groups in Worcester & Evesham`
- `Registered Charity 1190615`
- `Confidential Weekly Meetings`
- `Talk to People Who Understand`
- `Yellow Scarf CIO`
- `Local Worcestershire Support`
- `No Referral Needed`
- `Contact Us to Join`
Opisy:
- `Partners, parents and relatives affected by gambling meet weekly in Worcester and Evesham.`
- `Confidential groups led by professionals. Yellow Scarf CIO, registered charity 1190615.`
- `No referral needed. Send a short form or call us. We will tell you about the next group.`

### G1 — Eastern European community support → /en-gb/i-need-help.html (ścieżka: /support/community)
Nagłówki:
- `Support for Eastern Europeans`
- `Polish-Speaking Support in UK`
- `Mental Health Support Groups`
- `Registered Charity 1190615`
- `Worcestershire and Online`
- `Yellow Scarf CIO`
- `Talk in Your Own Language`
- `Confidential Support Groups`
- `Support for Ukrainians`
- `Walk and Talk Groups`
- `Reach Out Today`
- `Community, Not Judgement`
- `Based in Evesham`
- `Help in English and Polish`
- `A Short Form to Get Started`
Opisy:
- `Support groups and projects for Eastern Europeans in the Midlands, in your own language.`
- `Registered charity 1190615, Evesham. Describe your situation and we will reply.`
- `Walk and talk groups, support groups and events in Worcestershire. Online support UK-wide.`
- `You do not need everything figured out before reaching out. A short form is enough.`

### G2 — Eastern European community support (wariant: Ukrainian & local)
Nagłówki:
- `Ukrainian Walkie Talkie Group`
- `Walk and Talk, Worcestershire`
- `Support for Ukrainian Refugees`
- `Registered Charity 1190615`
- `Twice a Month, Outdoors`
- `Community Support in Evesham`
- `Yellow Scarf CIO`
- `Free to Join`
- `Meet People Who Understand`
- `Get in Touch`
Opisy:
- `Outdoor walk and talk sessions for Ukrainian refugees in Worcestershire, twice a month.`
- `Funded by Worcestershire Community Foundation. Yellow Scarf CIO, charity 1190615.`
- `Join a friendly group, talk in your language and get to know the local community.`
Uwaga: „Free to Join” tylko jeśli udział w grupie ukraińskiej jest bezpłatny (D1b).

### K4 (EN Donations, jeśli wariant B)
Zostają reklamy #1, #4–#8 z usuniętymi nagłówkami „Over 200 on Our Waiting List”, „Over 200 People Waiting”, „Help Clear the Waiting List”, „Reduce the Waiting List”, „Support Our Helpline” oraz opisami o liście oczekujących i infolinii, dopóki nie dostarczysz dowodu (D3). „Free and low-cost therapy groups” → „low-cost support groups”.

---

## 7. Zasoby (komponenty)

| Typ | Poziom | Treść | URL |
|---|---|---|---|
| Sitelink | konto | Potrzebuję pomocy / Krótki formularz po polsku / Odpowiadamy w dni robocze | https://yellowscarf.org/pl/potrzebuje-pomocy.html |
| Sitelink | konto | Grupy wsparcia / Spotkania online po polsku / Od £50 miesięcznie | https://yellowscarf.org/pl/jak-pomagamy.html |
| Sitelink | konto | Nasz zespół / Kto prowadzi grupy / Doświadczeni specjaliści | https://yellowscarf.org/pl/nasz-zespol.html |
| Sitelink | konto | Nasze projekty / Co robimy dla Polaków / Lokalnie i online | https://yellowscarf.org/pl/nasze-projekty.html |
| Sitelink | K2, K3, K4 | Donate / Support our groups / From £5 a month | https://yellowscarf.org/en-gb/donate.html (K2: /pl/donate.html) |
| Sitelink | K3 | Our Projects / Gambling Support, Walkie Talkie / Worcester and Evesham | https://yellowscarf.org/en-gb/our-projects.html |
| Sitelink | K3 | I Need Help / Short form, we reply / English or Polish | https://yellowscarf.org/en-gb/i-need-help.html |
| Objaśnienia | konto | Charity nr 1190615 · Spotkania online · Po polsku i po angielsku · Siedziba w Evesham · Członek ACCPH (zostaje) | — |
| Snippet | K1 | Usługi: grupy wsparcia, wsparcie emocjonalne, spotkania online, projekty społeczne | — |
| Telefon | K1, K3 | +44 7340 634326 (infolinia pn–pt 10–16) — **po weryfikacji numeru w Google**; 01905570235 usunąć | — |
| Logo, nazwa | konto | Logo istniejące; Business name „Yellow Scarf CIO” | — |

Do usunięcia: objaśnienia kontowe „Polski Terapeuta w UK”, „Psycholog Po Polsku w UK”, „Terapia Przez Internet”, „Osrodek Terapeutyczny”, „Osrodek Terapii i Rozwoju”, „Jesteśmy Dla Ciebie w UK” (ta ostatnia może zostać); sitelink PL „Jak Pomagamy / Infolinia, grupy, terapia dzieci”; duplikaty objaśnień z 15.09; sitelink kontowy „Jak Pomagamy / Bezpłatne Wsparcie i Grupy” (słowo „bezpłatne” przy płatnych grupach). Twierdzenie „Działamy od 2011” — tylko po D3.

---

## 8. Konwersje i GA4 (zadanie dla Seltena; właściwość GA4 538419573)

| Zdarzenie GA4 | Gdzie | W Ads jako | Cel kampanii |
|---|---|---|---|
| `generate_lead` | udane wysłanie formularza /pl/potrzebuje-pomocy.html i /en-gb/i-need-help.html (po stronie potwierdzenia, nie po kliknięciu „Wyślij”) | Primary, „Submit lead form”, liczenie „One” | K1, K3 |
| `sign_up_group` | kliknięcie „Zapisz się na Grupę” + wysłanie formularza #umow-sie-z-nami | Primary, „Sign-up”, „One” | K1 |
| `click_to_call` | kliknięcie tel: (infolinia) | Secondary | — |
| `click_email` | kliknięcie mailto: | Secondary | — |
| `donate_click` (istnieje) | przycisk darowizny | Primary tylko dla K2/K4, Secondary dla K1/K3 (cele na poziomie kampanii) | K2, K4 |

Porządki w konwersjach: „Połączenia z reklam” → Secondary do czasu zweryfikowanego numeru; „Website traffic”, „Thank you page”, „Thank you”, „Landing page yellow scarf” → usunąć (dwa są Misconfigured). Odpiąć GA4 Ośrodka 277882249 od 798 (import odbiorców ON). Wyłączyć: Customer Match („Smart Bidding and optimised targeting”, „Conversion-based lists”), Enhanced conversions (Recording), Enhanced conversions for leads (nie konfigurować). Sprawdzić etykietę URGENT na tagu Google (Tag Manager) i Consent Mode v2.

Prywatność (UK GDPR, dane szczególnej kategorii): formularz PL — nazwisko i telefon jako pola opcjonalne, „opis sytuacji” opcjonalny z dopiskiem „nie musisz podawać szczegółów”; zdarzenia GA4 bez treści formularza, bez parametrów o powodzie kontaktu; brak remarketingu i list odbiorców; polityka prywatności po polsku (dziś link prowadzi do wersji EN).

---

## 9. Porządki na koncie (jedna partia, po akceptacji)

1. Nazwa konta: „YELLOW SCARF CIC” → „Yellow Scarf CIO” (Admin → ustawienia konta).
2. Odpięcie GA4 277882249 (Ośrodek) od 798.
3. Usunięcie objaśnień kontowych promujących Ośrodek (§7) i duplikatów z 15.09.
4. Customer Match off, Conversion-based lists off, Enhanced conversions off, segment w Customer lifecycle usunięty.
5. Zadanie „healthcare ads – mentalhealth.org.uk” → **Dismiss** (nie Start); to nie nasza domena.
6. Szkic „Draft: Leads-Performance Max- Strona Fundacjii” → usunąć (jeśli nie Twój).
7. Telefon 01905570235 → usunąć; dodać +44 7340 634326 po weryfikacji.
8. Reklama #3 (Addiction services) → usunąć, zastąpić B1/B2.
9. Dzwonek: „Confirm your EU political ads status” → potwierdzić „brak reklam politycznych” (jak 9.02.2026); passkeys dla konta → włączyć; alert „Protect your account” → przejrzeć.
10. Dostępy: po akceptacji linku MCC przez Setlena — decyzja o biimediaworkspace (D7) i passkey na setlen.net.

---

## 10. Kolejność wdrożenia

| Krok | Co | Kto | Kiedy |
|---|---|---|---|
| 0 | Decyzje D1–D9 | Rafał | dziś/jutro |
| 1 | Zdarzenia GA4 i poprawki formularza (§8), strona /en-gb/gambling-support.html (opcjonalnie), polityka prywatności PL | Selten | do 9.11 |
| 2 | Porządki na koncie (§9) + lista wykluczeń + import konwersji z GA4 | ja, w panelu przez Chrome, jedną partią; odczyt przed/po | po kroku 1 |
| 3 | K1–K3: kampanie, grupy, słowa, RSA, sitelinki; K4 pauza lub wariant B; stara PL przebudowana w K1 (zachowuje historię) | ja, w panelu | ten sam dzień co krok 2 |
| 4 | Kontrola po 48 h: statusy reklam (Addiction services?), wyświetlenia, hasła, CTR | ja | +2 dni |
| 5 | Tygodniowo: hasła → wykluczenia, QS, CTR; log zgłoszeń od Ciebie/zespołu | ja + Rafał | co tydzień |
| 6 | Ocena 30 dni | ja | 2.12.2026 (jeśli start do 10.11) |
| 7 | Ocena 60 dni, decyzja o PMax Search+Maps (wymaga Google Business Profile Fundacji w Evesham) | ja + Rafał | 5.01.2027 |

Jeśli Setlen zatwierdzi link MCC wcześniej, kroki 2–3 robię przez API z pełnym protokołem, tak jak na 733/311.

---

## 11. Ryzyka

| Ryzyko | Prawdopodobieństwo | Co robimy |
|---|---|---|
| CTR < 5% po starcie (szerokie dopasowania, hasła spoza intencji) | średnie | tylko wyrażenie/ścisłe, lista wykluczeń od dnia 1, kontrola haseł co tydzień; pauza fraz z CTR < 3% po 100 wyśw. |
| Addiction services na nowych reklamach PL/EN (strona wspomina nałóg) | średnie | zero słów o uzależnieniach w reklamach; prośba do Seltena o złagodzenie meta description i tekstu na /pl/jak-pomagamy.html (zdrowie psychiczne, kryzys, emigracja); odwołanie, gdy flaga |
| 0 konwersji przez 30 dni mimo kliknięć | średnie | zdarzenia GA4 przed startem; jeśli brak zgłoszeń, test strony: numer telefonu i krótsza forma na /pl/potrzebuje-pomocy.html |
| Niska skala: polskich zapytań o pomoc w UK jest mało | wysokie | to nie jest ryzyko zgodności, tylko oczekiwań: grant uzupełnia, nie zastępuje innych kanałów (grupy FB, parafie, GBP) |
| Twierdzenia w reklamach bez dowodu (2011, 200 osób, infolinia, BACP) | niskie po D3 | wchodzą tylko z dokumentem; BACP na 798 wymaga potwierdzenia, że członkostwo dotyczy CIO, nie tylko CIC |
| Kanibalizacja z Ośrodkiem (733) | niskie | frazy z „psycholog/terapeuta” zostają w 733; w 798 „pomoc/wsparcie/grupa”; wykluczenia krzyżowe |
| Ad Grants: automatyczna zmiana strategii lub dezaktywacja przed startem | niskie, rośnie z czasem | wdrożyć w listopadzie, nie w grudniu |

---

## 12. Czego potrzebuję od Ciebie — decyzje (odpowiedz numerami: „D1 tak”, „D3 nie” itd.)

- **D1.** Czy pierwszy kontakt (formularz, odpowiedź, rozmowa wstępna) i infolinia +44 7340 634326 są bezpłatne? Jeśli tak, wchodzą frazy „bezpłatna pomoc psychologiczna uk”, „polski psycholog uk za darmo” → strona /pl/potrzebuje-pomocy.html, a sitelink „Bezpłatne wsparcie” zostaje z poprawką „bezpłatny pierwszy kontakt”. **D1b.** Czy grupa ukraińska jest bezpłatna?
- **D2.** Kampania EN Donations: pauza do 5.01.2027 (moja rekomendacja) czy wariant B ($49, Max Conversions, bez twierdzeń o liście oczekujących)?
- **D3.** Dowody na twierdzenia: „Działamy od 2011” (jako co: grupa społeczna / CIC / CIO?), „ponad 200 osób na liście oczekujących” (skąd liczba, z jakiej daty), „infolinia” (czy +44 7340 634326 to infolinia Fundacji). Bez dowodu zdejmuję.
- **D4.** Grupy: czy są „małe, zamknięte”, „prowadzone przez specjalistów” i czy „nowe grupy ruszają cyklicznie”? Jaki jest realny termin najbliższej grupy PL online? Bez terminu reklamy B kierują na stronę opisową, a konwersją jest zgłoszenie, nie zapis.
- **D5.** Zgoda na zdjęcie z kampanii PL wykluczeń „terapia / terapii / terapię” (zostają „terapeuta”, „psychoterapeuta”, „psychoterapia”, „psycholog”), żeby móc używać „terapia grupowa po polsku”?
- **D6.** Zgoda na: odpięcie GA4 Ośrodka od 798, usunięcie objaśnień o Ośrodku, wyłączenie Customer Match / Enhanced conversions, usunięcie 4 działań konwersji, usunięcie reklamy #3, usunięcie szkicu PMax, Dismiss zadania healthcare, zmianę nazwy konta na Yellow Scarf CIO?
- **D7.** Kto obsługuje biimediaworkspace@gmail.com (logował się 1–2.11, bez zmian w logu)? Po linku MCC: zostaje czy usuwamy?
- **D8.** Gambling Support po angielsku lokalnie (K3) — wchodzi teraz czy po grupach PL? Czy grupy w Worcester i Evesham faktycznie działają co tydzień (strona tak mówi)?
- **D9.** Zlecenie dla Seltena (§8 + §9 pkt 7 + strona /en-gb/gambling-support.html + polityka prywatności PL + złagodzenie treści o nałogu): wysyłasz Ty czy przygotować gotową wiadomość?

Po Twoich odpowiedziach przygotuję finalną listę zmian w kolejności wdrożenia i wykonam ją jedną partią w panelu, z odczytem przed i po, bez żadnych zmian poza zaakceptowanymi.

---

## 13. Kontrola końcowa

Konto: Fundacja 798-577-2656 = yellowscarf.org = Yellow Scarf CIO = Google Ad Grants (nie komercyjne; budżet w USD z grantu, nie gotówka CIC). Ośrodek (733) i Mental (311) nietknięte; frazy „psycholog/terapeuta” zostają w 733. Żadna reklama nie obiecuje efektów, nie diagnozuje, nie używa „bezpłatnie” bez potwierdzenia, nie mówi o uzależnieniach od alkoholu/narkotyków. Strategie: Maksymalizacja konwersji; brak tCPA, broad match, Demand Gen, Display, PMax, auto-apply, AI Max, Customer Match, EC for leads, importu offline. Dane: minimalizacja, brak danych wrażliwych w tagach. Propozycja służy celowi 2026: 4 grupy × 6–8 uczestników.
