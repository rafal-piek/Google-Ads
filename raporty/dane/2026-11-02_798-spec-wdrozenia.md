# SPEC WDROŻENIA — Fundacja 798-577-2656 (Google Ad Grants, yellowscarf.org, Yellow Scarf CIO) — 2.11.2026

Zgoda Rafała: 2.11.2026 10:26 UTC „ok zgadzam się działaj” na propozycję F4 (raporty/2026-11-02_798-propozycja-przebudowy.md) z założeniami: D1 bez fraz „bezpłatna/darmowa”; D2 EN Donations PAUZA; D3 bez twierdzeń „od 2011”, „200 osób na liście”, „infolinia”; D4 bez „małe, zamknięte” i „ruszają cyklicznie”; D5 zdjąć wykluczenia „terapia/terapii/terapię” w PL; D6 porządki w całości (szkic PMax na końcu); D8 K3 od razu.

## Zasady wykonania (obowiązkowe)
- Narzędzie: rozszerzenie Claude in Chrome w Chrome Rafała, profil authuser=0 (infoyellowscarf@gmail.com). Przed KAŻDĄ zmianą sprawdź, że nagłówek pokazuje konto 798-577-2656. Nie dotykaj 733-094-4080 ani 311-878-5541. Nie używaj Control_Chrome ani wbudowanej przeglądarki.
- Jeśli panel zablokuje zapis (klasyfikator uprawnień, weryfikacja tożsamości Google, passkey) — NIE obchodź tego. Zapisz, co się stało, przejdź do następnego punktu, a na końcu zgłoś listę niewykonanych.
- Nie akceptuj żadnych podpowiedzi Google, nie włączaj auto-apply, AI Max, rozszerzenia URL, automatycznych komponentów, partnerów wyszukiwania, sieci reklamowej, broad match, tCPA. Nie uruchamiaj zadania „healthcare ads – mentalhealth.org.uk” (tylko Dismiss). Nie akceptuj linku MCC.
- Protokół: przed startem zapisz krótki snapshot (kampanie, budżety, strategie, liczba słów/reklam/wykluczeń, konwersje, GA4 linki, nazwa konta). Po każdej fazie dopisz do ~/Desktop/zmiany-2026-11-02-798.md (kopia ~/claude/pamiec/) co zrobione, co nie i dlaczego. Po każdej fazie wyślij mi krótki raport (send_message), a na końcu pełny protokół w częściach ≤6000 znaków.
- Waluta konta USD. Teksty reklam dokładnie jak niżej (nagłówki ≤30, opisy ≤90 znaków, sprawdzone). Nie dopisuj własnych tekstów.

## FAZA A — porządki na koncie
A1. Admin → Account settings: nazwa konta „YELLOW SCARF CIC” → „Yellow Scarf CIO”.
A2. Tools → Data manager / Linked accounts → Google Analytics (GA4): odłącz właściwość „Ośrodek Terapeutyczno Rozwojowy” 277882249 (import odbiorców ON). Zostaje tylko 538419573 (Yellow Scarf CIO – www.yellowscarf.org).
A3. Assets (poziom konta): usuń objaśnienia „Polski Terapeuta w UK”, „Psycholog Po Polsku w UK”, „Terapia Przez Internet”, „Osrodek Terapeutyczny”, „Osrodek Terapii i Rozwoju” (zostaje „Jesteśmy Dla Ciebie w UK”). Usuń sitelink kontowy „Jak Pomagamy / Wsparcie Społeczności Polskiej / Bezpłatne Wsparcie i Grupy”. Usuń sitelink kontowy „Grupy Wsparcia / Grupy Terapeutyczne i Wsparcia / Wsparcie w Języku Polskim” (zastąpi go nowy w fazie F). Na poziomie kampanii PL usuń sitelink „Jak Pomagamy / Infolinia, grupy, terapia dzieci / Poznaj nasze działania” i duplikaty objaśnień/snippetu z 15.09 (ten komplet z 0 wyśw.). Objaśnienia „Działamy od 2011” (PL) → usuń (D3). Członek ACCPH zostaje.
A4. Goals → Conversions → Settings: Customer Match „Smart Bidding and optimised targeting” OFF, „Conversion-based lists” OFF; Enhanced conversions OFF (nie konfiguruj EC for leads). Customer lifecycle → Customer acquisition: usuń wybrany segment (bid equally bez segmentu).
A5. Goals → Conversions: „Połączenia z reklam” → Secondary (numer odrzucony). Usuń działania: „Website traffic”, „Thank you page”, „Thank you”, „Landing page yellow scarf”. donate_click zostaje Primary.
A6. Kampania [EN] Donations - Yellow Scarf (23910166739): PAUSE. Usuń z niej zasób połączenia „Call 01905570235” (Disapproved). Nic więcej w niej nie zmieniaj.
A7. Kampania PL: usuń reklamę #3 (823169976603, Addiction services).
A8. Policy → Account: zadanie „healthcare ads … mentalhealth.org.uk” → Dismiss. Dzwonek „Confirm your EU political ads status” → potwierdź, że konto NIE wyświetla reklam politycznych w UE (jak 9.02.2026).
Raport po fazie A.

## FAZA B — wykluczenia
B1. Tools → Shared library → Negative keyword lists: utwórz listę „Spoza oferty – 798 (2.11.2026)”. Dodaj do niej wszystkie obecne wykluczenia z poziomu kampanii PL i EN (97; zachowaj typ dopasowania) Z WYJĄTKIEM: „terapia”, „terapii”, „terapię” (D5) oraz „wolontariat” (potrzebne w K2). Dodaj pozycje z sekcji „Wykluczenia” poniżej (pomiń pozycje oznaczone jako tylko dla K1/K2 lub tylko K3/K4 — te idą na poziom kampanii). Podepnij listę do kampanii PL (K1) i EN Donations (K4) oraz do nowych K2 i K3 po ich utworzeniu.
B2. Po podpięciu listy usuń wykluczenia z poziomu kampanii PL i EN (duplikaty), ale w kampanii PL (K1) DODAJ z powrotem na poziomie kampanii: „wolontariat” (broad) oraz angielskie ogólne z sekcji „tylko K1, K2”. W K3/K4 dodaj na poziomie kampanii pozycje „EN K3/K4”.
Raport po fazie B.

## FAZA C — K1: przebudowa kampanii PL (24210923006), zachowuje historię
C1. Nazwa → „[PL] Pomoc po polsku w UK”. Strategia → Maksymalizacja konwersji (bez docelowego CPA). Budżet → $120/dz. Lokalizacja: United Kingdom, opcja „Presence: people in or regularly in your targeted locations”. Języki: polski + angielski. Sieci: tylko Google Search, partnerzy OFF, Display OFF. AI Max OFF, rozszerzenie końcowego URL OFF, automatyczne komponenty OFF, broad match kampanii OFF. Rotacja: Optymalizuj. Cele konwersji: na razie domyślne konta (zmiana po zdarzeniach GA4 od Seltena).
C2. Grupa „Grupa reklam 1” (199512906683) → nazwa „A. Pomoc psychologiczna po polsku”. Usuń wszystkie jej dotychczasowe słowa kluczowe. Dodaj słowa z sekcji A (phrase + exact: każdą frazę dodaj jako "fraza" i [fraza]). Usuń dotychczasowe reklamy tej grupy (#2 828414587013 — po dodaniu nowych). Dodaj RSA A1 i A2 (final URL https://yellowscarf.org/pl/potrzebuje-pomocy.html, ścieżki jak podano).
C3. Grupa „Polska fundacja – Jak pomagamy” (201333686593) → PAUSE (jej rolę przejmuje K2).
C4. Nowa grupa „B. Grupy wsparcia po polsku”: słowa z sekcji B (phrase + exact), RSA B1 i B2, final URL https://yellowscarf.org/pl/jak-pomagamy.html.
C5. Nowa grupa „C. Emigracja: samotność, stres, kryzys”: słowa z sekcji C (phrase + exact), RSA C1 i C2, final URL https://yellowscarf.org/pl/potrzebuje-pomocy.html.
C6. Zasoby kampanii K1: snippet „Usługi: grupy wsparcia, wsparcie emocjonalne, spotkania online, projekty społeczne”; sitelinki kontowe z fazy F będą dziedziczone; podepnij listę wykluczeń.
Raport po fazie C.

## FAZA D — K2: nowa kampania „[PL] Fundacja Yellow Scarf”
Search, cel: potencjalni klienci / bez celu z kreatora (wybierz „Create a campaign without a goal's guidance” jeśli dostępne), tylko sieć wyszukiwania, partnerzy OFF, Display OFF. UK, Presence. Języki PL + EN. Maksymalizacja konwersji, bez tCPA. Budżet $30/dz. AI Max OFF, rozszerzenie URL OFF, auto-komponenty OFF, broad OFF. Rotacja Optymalizuj. Bez list odbiorców. Grupy: „D. Marka” (słowa sekcja D, phrase + exact; RSA D1 z przypiętym H1 „Yellow Scarf: oficjalna strona” i D2; final URL https://yellowscarf.org/pl/), „E. Chcę pomóc” (słowa sekcja E; RSA E1 → https://yellowscarf.org/pl/chce-pomoc.html, E2 → https://yellowscarf.org/pl/donate.html). Sitelink kampanii: Donate / Wesprzyj nasze grupy / Od £5 miesięcznie → https://yellowscarf.org/pl/donate.html. Podepnij listę wykluczeń. NIE dodawaj „wolontariat” do wykluczeń tej kampanii.
Raport po fazie D.

## FAZA E — K3: nowa kampania „[EN] Midlands – Support groups”
Ustawienia jak K2, ale: lokalizacje: Worcestershire (county) + promień 40 km wokół Evesham + promień 40 km wokół Worcester + Birmingham (city); Presence. Języki EN + PL. Budżet $80/dz. Grupy: „F. Gambling support groups” (słowa sekcja F; RSA F1, F2; final URL https://yellowscarf.org/en-gb/our-projects.html), „G. Eastern European community support” (słowa sekcja G; RSA G1, G2; final URL https://yellowscarf.org/en-gb/i-need-help.html). Sitelinki kampanii: Our Projects / Gambling Support, Walkie Talkie / Worcester and Evesham → /en-gb/our-projects.html; I Need Help / Short form, we reply / English or Polish → /en-gb/i-need-help.html; Donate / Support our groups / From £5 a month → /en-gb/donate.html. Wykluczenia na poziomie kampanii: pozycje „EN K3/K4”. Podepnij listę wykluczeń.
Raport po fazie E.

## FAZA F — zasoby konta i porządki końcowe
F1. Sitelinki na poziomie konta (4): zgodnie z tabelą „Zasoby” poniżej (Potrzebuję pomocy, Grupy wsparcia, Nasz zespół, Nasze projekty) z podanymi URL-ami.
F2. Objaśnienia na poziomie konta: „Charity nr 1190615”, „Spotkania online”, „Po polsku i po angielsku”, „Siedziba w Evesham” (Członek ACCPH zostaje).
F3. Business name na koncie: „Yellow Scarf CIO”.
F4. Szkic „Draft: Leads-Performance Max- Strona Fundacjii” → usuń (Rafał nie zgłosił, że jest jego).
F5. Dzwonek: „Upgrade your account security with passkeys” — NIE klikaj (to Rafał); „Protect your account from unauthorised activity” — tylko odczytaj treść i zapisz.
Raport po fazie F.

## FAZA G — odczyt po zmianach
Spisz: kampanie (nazwa, status, strategia, budżet, lokalizacje, języki), grupy, liczby słów per grupa, reklamy (ID, status, Ad strength, ostrzeżenia polityki), lista wykluczeń (liczba), konwersje (status, primary/secondary), GA4 linki, nazwa konta, zasoby kontowe, szkice. Porównaj ze snapshotem sprzed zmian. Wyślij pełny protokół.

---

## 5. Słowa kluczowe (dopasowanie do wyrażenia + ścisłe; bez słów jednowyrazowych)

Zasada: każda fraza ma 2–4 wyrazy i wyraża zamiar; frazy z „psycholog/psychoterapeuta/terapeuta” zostawiamy Ośrodkowi (733), żeby dwa konta nie licytowały przeciw sobie. Frazy „za darmo/bezpłatny” wchodzą tylko, jeśli potwierdzisz, że pierwszy kontakt i infolinia są bezpłatne (decyzja D1); inaczej idą do wykluczeń.

**A. Pomoc psychologiczna po polsku (K1)** — 14 fraz
"pomoc psychologiczna po polsku", "pomoc psychologiczna po polsku uk", "pomoc psychologiczna dla polaków w uk", "pomoc psychologiczna dla polaków w anglii", "wsparcie psychologiczne po polsku", "wsparcie psychologiczne dla polaków", "wsparcie emocjonalne po polsku", "potrzebuję pomocy psychologicznej", "gdzie szukać pomocy psychologicznej w uk", "pomoc psychologiczna online po polsku", "polska fundacja pomoc psychologiczna", "pomoc dla polaków w uk", "wsparcie dla polaków w uk" (dziś jedyne klikane), "pomoc psychologiczna emigracja"
NIE dodawać fraz „bezpłatna/darmowa/za darmo” (decyzja D1 otwarta).

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

Fraz „bezpłatny/darmowy/za darmo” nie dodajemy ani do słów, ani do wykluczeń (D1 otwarta).

---

## 6. Reklamy (RSA; każda grupa ≥ 2; nagłówki ≤ 30 znaków, opisy ≤ 90; bez przypinania poza H1 w grupie D)

Zasady treści: zero obietnic efektu, zero „bezpłatnie” (do czasu D1), zero słów o uzależnieniach w PL (Addiction services), numer charity w każdej reklamie, spokojny ton. Twierdzeń „Działamy od 2011”, „ponad 200 osób na liście”, „infolinia” NIE używamy (D3: brak dokumentu).

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
- `Odpowiadamy w dni robocze`
- `Wsparcie w trudnym czasie`
- `Jesteśmy po to, by słuchać`
Opisy:
- `Opisz w kilku zdaniach, co się dzieje. Odezwiemy się i podpowiemy, co może pomóc.`
- `Polska charity w UK. Grupy wsparcia, spotkania online i pomoc w Twoim języku.`
- `Nie oceniamy i nie diagnozujemy. Pomagamy znaleźć wsparcie dopasowane do Twojej sytuacji.`
- `Charity nr 1190615 z siedzibą w Evesham. Działamy online dla Polaków w całym UK.`

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
- `Grupy wsparcia dla Polaków`
- `Zapisz się na grupę`
- `Pierwszy krok bez presji`
- `Wsparcie w Twoim języku`
- `Niska opłata, pełne wsparcie`
- `Zobacz opisy grup`
Opisy:
- `Grupa wstępna £50/mies. stabilizuje sytuację. Grupa terapeutyczna £120/mies. idzie dalej.`
- `Spotkania online po polsku w grupie. Opłaty wspierają misję charity nr 1190615.`
- `Zobacz, jak działają nasze grupy, i zapisz się. Odezwiemy się i dobierzemy grupę razem.`
- `Yellow Scarf to polska charity w UK. Grupy prowadzą doświadczeni specjaliści.`

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
- `Pomoc dla Polaków w UK`
- `Siedziba w Evesham`
Opisy:
- `Wolontariat, darowizna albo Twój czas i wiedza. Zobacz, jak możesz wesprzeć Yellow Scarf.`
- `Darowizny finansują grupy wsparcia i projekty dla Polaków w UK. Charity nr 1190615.`
- `Szukamy wolontariuszy do działań online i lokalnych w Worcestershire. Napisz do nas.`
- `Każda regularna darowizna pomaga planować kolejne grupy. Wesprzyj nas od £5 miesięcznie.`

### E2 — Chcę pomóc (wariant: darowizna)
Nagłówki:
- `Wesprzyj Polaków w UK`
- `Darowizna dla Yellow Scarf`
- `Charity nr 1190615`
- `Od £5 miesięcznie`
- `Finansujemy grupy wsparcia`
- `Polska fundacja w UK`
- `Jednorazowo lub co miesiąc`
- `Wsparcie polskiej społeczności`
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
- `Friendly, Informal Group`
- `Meet People Who Understand`
- `Get in Touch`
Opisy:
- `Outdoor walk and talk sessions for Ukrainian refugees in Worcestershire, twice a month.`
- `Funded by Worcestershire Community Foundation. Yellow Scarf CIO, charity 1190615.`
- `Join a friendly group, talk in your language and get to know the local community.`

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

