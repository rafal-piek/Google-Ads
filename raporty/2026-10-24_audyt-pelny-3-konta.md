# Pełny audyt trzech kont Yellow Scarf — Ads, GA4, Search Console, SEO/GEO

Data: 2026-10-24 (dane pobrane ok. 09:50–10:00 UTC, tylko odczyt; na kontach nic nie zmieniono).
Autor: Claude dla Rafała Piekarczyka. Źródła liczb: Google Ads API (MCC 7007385800), GA4 Data API, Search Console API. Pełne tabele surowe: `~/Desktop/audyt-dane-2026-10-24.md` na Macu Rafała (kopia w `~/claude/pamiec/`).
Okna: **90 dni = 2026-07-26 – 2026-10-23**, **30 dni = 2026-09-24 – 2026-10-23**, GSC porównanie z **2026-04-27 – 2026-07-25**.
Konta osobno, bez sumowania. Zasady Google sprawdzone u źródła 24.10.2026 (lista w §7).

Oznaczenia: **[F]** fakt z danych lub źródła, **[Z]** założenie do potwierdzenia, **[W]** mój wniosek.

---

## 1. Co się dzieje (krótko)

1. **Ośrodek (733)** jest zdrowym kontem z jednym silnikiem (Leads 1) i trzema dziurami: kampania Par (£252 za konwersję w 90 dni), ok. £1 900 w 90 dni na słowach bez konwersji oraz największa pozycja wydatku w grupie UZALEŻNIENIA (£2 487 / 90 dni), która jest „zamrożona”, ale cały czas emituje reklamy pod hasła alkoholowe, czego w UK nie da się certyfikować. Koszt leadu widoczny w Ads to £79 (30 dni); po uwzględnieniu trybu zgód realnie bliżej £45–55, czyli w okolicy brytyjskiego benchmarku dla healthcare (£48–52), ale 2× powyżej benchmarku dla zdrowia psychicznego (£22).
2. **Mental (311)** nie działa jako kanał pozyskania: 2 konwersje za £519 w 30 dni (£259/lead), zero telefonów od miesiąca, 0 płacących klientów od kwietnia, udział w wyświetleniach poniżej 10%. Koszt leadu jest 5–12× powyżej benchmarku. To nie jest problem ustawień, tylko strony docelowej, wolumenu i doboru kanału. Decyzja z 1.11 powinna brzmieć: ile z £500 idzie w ruch kupowany, a ile w obecność własną.
3. **Fundacja (798)** nie wykorzystuje grantu: w październiku GA4 widzi 2 sesje z płatnego wyszukiwania, w 90 dniach 7. To zagraża wymogom Ad Grants (CTR ≥ 5% miesięcznie, ≥ 1 konwersja miesięcznie, aktywne konto). Bez dostępu do panelu nie wiem, czy kampanie są wstrzymane, odrzucone, czy po prostu nie wygrywają aukcji. To jest dziś najpilniejsza rzecz na trzech kontach.
4. **SEO** jest słabe tam, gdzie powinno być najsilniejsze: osrodek.uk stracił 29% kliknięć kwartał do kwartału, a główna fraza „polski psycholog uk” stoi na pozycji 10 przy 671 wyświetleniach i 2 kliknięciach. Ponad połowa wyświetleń witryny pochodzi z Polski i nie ma wartości. yellowscarftherapy.co.uk ma 43 kliknięcia w 90 dni, prawie wyłącznie brandowe; jedyny pozamarkowy ślad to „burnout”. yellowscarf.org jest w Google wyłącznie marką; nie ma ani jednego polskojęzycznego zapytania o pomoc.
5. **GEO (widoczność w AI)**: ruch z asystentów AI jest śladowy (Ośrodek 3 sesje, Mental 7, Fundacja 3 w 90 dni), ale Mental ma już więcej sesji z ChatGPT niż z organicznego wyszukiwania w niektórych tygodniach. W healthcare 52,6% cytowań AI pochodzi z katalogów i wizytówek, nie ze stron własnych, więc dźwignią są Google Business Profile, katalogi terapeutów i spójne dane, a nie „treści pod AI”.

---

## 2. Liczby — osobno dla każdego konta

### 2.1 OŚRODEK — Ads 733-094-4080 (osrodek.uk, Yellow Scarf Support CIC)

**Kampanie, 30 dni (2026-09-24 – 2026-10-23)**

| Kampania | Budżet/dz | Koszt | Klik. | CTR | CPC | Konw. | Koszt/konw. | IS | Utrata: budżet / ranking |
|---|---|---|---|---|---|---|---|---|---|
| Leads 1 (Search) | £110 | £3 026 | 1 119 | 8,5% | £2,70 | 45,0 | **£67** | 36,6% | **35,9%** / 27,6% |
| Sales-PMax-1 | £35 | £1 032 | 458 | 3,5% | £2,25 | 11,0 | £94 | 26,2% | 14,8% / 59,0% |
| [PL] Terapia Par i Rodzin | £12 | £616 | 113 | 9,7% | £5,45 | 3,0 | **£206** | 45,5% | 32,1% / 22,4% |
| PL \| London \| Search (od 8.10) | £30 | £348 | 95 | 12,9% | £3,66 | 2,0 | £174 | 69,6% | 9,1% / 21,4% |
| Kampania kryzysowa (PMax) | £7 | £185 | 108 | 3,3% | £1,71 | 5,0 | £37 | 25,9% | 16,2% / 57,9% |
| Wsparcie Rodzin | £1 | £32 | 20 | 6,8% | £1,59 | 0 | — | 24,4% | 28,3% / 47,3% |
| **Konto** | 195 | **£5 238** | 1 913 | 6,0% | £2,74 | **66,0** | **£79** | | |

Domknięcie: 26 dni × 179–195 £ ≈ £5 430 → wydano 96%. [F]
Konwersje w kolumnie = formularz „Umów wizytę” (GA4, 1 na kliknięcie) 46 + połączenia 20. Bez duplikatów. [F]

**90 dni (2026-07-26 – 2026-10-23):** konto £13 297, 149 konwersji, £89/konw. Leads 1 £8 398 / 103 konw. / £82; PMax-1 £2 044 / 30 / £68; Pary £2 015 / 8 / **£252**; Kryzysowa £393 / 6 / £65; London £348 / 2 / £174; WR £99 / 0. [F]

**Grupy reklam Leads 1, 90 dni:** UZALEŻNIENIA £2 487 / 33,5 konw. / £74 · OGÓLNY £1 750 / 25,8 / £68 · DZIECIĘCY £1 705 / 22 / £78 · PSYCHOLOG ONLINE £1 065 / 9,5 / £112 · PSYCHOTERAPIA ONLINE £944 / 12,2 / £78 · TERAPIA PAR (wstrzymana 4.10) £447 / 0. [F]

**Porównanie z benchmarkami UK (Search, zdrowie psychiczne i healthcare)**

| Miara | Ośrodek 30 dni | Medico Digital UK 2025: mental health | Medico: healthcare ogółem | Ridley UK 2026: healthcare | LocaliQ US 2026: mental health |
|---|---|---|---|---|---|
| CTR (Search) | **8,5–9,0%** | 6,28% | 6,55% | 4,7% (wszystkie branże) | 4,46% |
| CPC | £2,70 | £1,02 | £1,86 | £2,85 | $4,22 |
| Współczynnik konwersji | 3,5% (Ads) / ~5,4% (GA4 paid) | 4,69% | 4,89% | ~5,5% | 1,85% |
| Koszt leadu | **£79** (Ads) / **~£45–55** realnie [Z] | £21,74 | £47,91 | £51,80 | $141 |

[W] Reklamy są lepsze od rynku (CTR), kliknięcie jest droższe niż w anglojęzycznym healthcare (niewielka polskojęzyczna pula aukcji), a koszt leadu jest w normie dla healthcare, ale nie dla taniego zdrowia psychicznego. Ads widzi tylko konwersje osób, które zaakceptowały cookies; GA4 pokazuje 165 zdarzeń kluczowych z Paid Search w 90 dni, a `form_submit` odpala się podwójnie (306 submit przy 207 start), więc realna liczba zgłoszeń to ok. 60–70% liczby w GA4 i ok. 1,4–1,7× liczby w Ads. Dokładny mnożnik da dopiero kalendarz.

**Co jeszcze wynika z danych (fakty):**
- Słowa z kosztem > £30 i 0 konwersji w 90 dni: 24 słowa, ok. **£1 900**. Największe: „psycholog polski uk” w grupie TERAPIA PAR £264 (grupa już wstrzymana), „terapia małżeńska” (Pary, QS 3) £244, „pomoc w uzależnieniach” £154, „psycholog konsultacja online” £118, „terapia małżeńska online” £103 przy CPC £9,41, „psycholog rodzinny” £103.
- **Kanibalizacja:** „psycholog polski uk” / „polski psycholog uk” siedzi w 5 grupach naraz (OGÓLNY QS 7 i £53/konw., PSYCHOLOG ONLINE QS 5 i £111, DZIECIĘCY QS 3 i £102, PSYCHOTERAPIA ONLINE £80/0, TERAPIA PAR £264/0). Google wybiera grupę aukcją, więc najlepsza grupa nie dostaje całego ruchu.
- **Hasła spoza oferty (30 dni):** nazwy innych organizacji („polskie centrum pomocy rodzinie” ×4, „opoka uk” — ta ostatnia w PMax z 1 konwersją), hasła o lekach („leki bulimia”, „jakie psychotropy na depresję”), angielskie ogólne („mental health telford”, „extreme restlessness”), hazard, przemoc (częściowo wykluczone 23.10).
- **Grupa UZALEŻNIENIA:** hasła z 30 dni to m.in. „online alcohol support”, „leczenie alkoholizmu w uk”, „terapia alkoholowa w uk”, „terapia dla alkoholików online”, „linia dla alkoholików”. Słowa kluczowe grupy: „terapeuta uzależnień”, „terapia od uzależnień”, „terapia alkoholowa”, „pomoc uzależnienia”.
- Partnerzy wyszukiwania w Leads 1: £78 / 228 kliknięć / 0 konwersji (90 dni). YouTube wewnątrz PMax: £136 / 214 kliknięć / 0.
- Komputery: £513 / 177 kliknięć / 1 konwersja (90 dni). Od 23.10 Rafał dał −100% na komputery w 4 kampaniach Search (z API nie da się tego odczytać; PMax nie ma tej opcji).
- Z zagranicy mimo ustawienia „obecność”: Pary + WR £96 / 47 kliknięć / 0 (Polska, Niemcy, Holandia, Turcja).
- Godziny (całe konto, 90 dni): 13:00–16:59 koszt/konw. £43–59; 08:00 £195; 17:00–18:59 £141–198 (razem £1 565 / 9,5 konw.). Dni: Pn £66, Pt i Sb £105. Przy Maks. konwersji korekty stawek wg godzin są ignorowane; działa tylko wyłączenie godzin.
- **Strony docelowe (GA4, ruch płatny, 90 dni):** /pl/umow-wizyte.html **24,6%** sesji z kluczowym zdarzeniem · /pl/oferta.html 11,4% · /pl/psychoterapia-dzieci-i-mlodziezy.html 10,0% · /pl/psychologia-i-psychoterapia.html 9,9% · /pl (PMax) 12,5% · **/pl/terapia-par-po-polsku-w-uk-online.html 2,8%** · /pl/kontakt.html 65 sesji, 0 kluczowych, zaangażowanie 24,6%.
- PMax-1: grupa „Competitors” £771 / 13,5 konw. (£57); „psychologia i psychoterapia” £225 / 0; „zespół” £39 / 0.
- Ustawienia: auto-apply **RESPONSIVE_SEARCH_AD = ENABLED** (reszta wyłączona); AI Max wyłączony wszędzie; komponent LEAD_FORM istnieje, niepodpięty, Google pcha 6 rekomendacji, żeby go włączyć; na koncie 733 wiszą ukryte działania konwersji domeny yellowscarf.org (relikt). Status weryfikacji reklamodawcy z API nieodczytywalny.
- **GSC osrodek.uk, 90 dni:** 1 116 kliknięć (−29%), 63 819 wyświetleń (−19%), poz. 8,7. UK 737 kliknięć (−27%), **Polska 334 kliknięć / 32 812 wyświetleń** (51% wyświetleń, bez wartości). Najwięcej kliknięć: „wszywka alkoholowa uk” 22, „polski psycholog uk za darmo” 14 (poz. 1,6; kwartał temu 44), marka 14. Kluczowe frazy komercyjne: „polski psycholog uk” poz. 10,2 (671 wyśw., 2 klik.), „polski psycholog w uk” 8,1, „terapia dla par uk” 14,5, „polski psycholog dziecięcy uk” 14,0, „polski psycholog londyn” 18,6. Strona /pl/psychologia-i-psychoterapia.html poz. 20,2 przy 1 353 wyświetleniach. 7 strony blogowych o uzależnieniach (esperal, wszywka, narkomania) daje więcej kliknięć niż strony usług. W indeksie duplikaty `/pl/pl/blog/...` i adresy z literówkami. Mobile poz. 6,3 vs desktop 13,7.

### 2.2 MENTAL — Ads 311-878-5541 (yellowscarftherapy.co.uk, Yellow Scarf Support CIC)

| Okres | Koszt | Klik. | CTR | CPC | Konw. (formularz / telefon) | Koszt/konw. | IS | Utrata: budżet / ranking |
|---|---|---|---|---|---|---|---|---|
| 30 dni | £519 | 163 | 5,6% | £3,18 | 2 (2 / **0**) | **£259** | <10% | 31,9% / **60,4%** |
| 90 dni | £2 851 | 865 | 4,2% | £3,30 | 14 (6 / 8) | £204 | 13,1% | 33,6% / 53,4% |

Domknięcie 30 dni: 16,45 × 30 = £494 → wydano 105%. [F] Jedna aktywna kampania, jedna grupa, 6 aktywnych słów (PHRASE). 13 słów wstrzymano 15.10. [F]

| Miara | Mental 30 dni | Medico UK mental health | Medico healthcare | Ridley UK healthcare |
|---|---|---|---|---|
| CTR | 5,6% | 6,28% | 6,55% | 4,7% |
| CPC | **£3,18** | £1,02 | £1,86 | £2,85 |
| Koszt leadu | **£259** (90 dni: £204) | £21,74 | £47,91 | £51,80 |
| Lead → klient | **0 z ~67 kontaktów od kwietnia** [F z plików] | — | — | — |

**Fakty:**
- „find a private counsellor” (PHRASE) = £1 590 / 475 klik. / 9,3 konw. (£170) w 90 dni, czyli 56% wydatku. Pozostałe aktywne: „private counselling sessions” £265 / 2,7 konw. (£99), „private therapist uk” £47 / 1 konw.
- Wyszukiwane hasła 30 dni: 49 widocznych = £240 / 58 klik. / **0 konw.**; **54% kosztu i obie konwersje są w hasłach, których Google nie pokazuje.** Widoczne to głównie nazwy innych praktyk („the talking rooms… glasgow”, „quiet mind centre exmouth”, „focus counselling bath”, „bacp find a therapist”, „age uk bereavement support”), zapytania lokalne („counsellor gloucester”, „counselling bridgend”) i żałoba. Rafał dodał 29 wykluczeń 23.10, 10 wykluczeń 14.10, 33 wykluczenia 4.10.
- Telefon: 8 połączeń w 90 dniach, **0 w ostatnich 30**. GA4 538367736 nie ma ani jednego zdarzenia kluczowego (form_submit 8, form_start 15 nieoznaczone).
- Strona docelowa /book-a-session: 141 sesji płatnych, zaangażowanie 41%; /fees.html 63%. QS 3 na słowach z danymi (strona docelowa i przewidywany CTR poniżej średniej, trafność reklamy powyżej).
- Wstrzymana kampania „Google AI Test | Broad” ma włączony AI Max i automatyczne teksty — gdyby ktoś ją włączył, wejdzie z broad match i tekstami Google.
- Geo 90 dni: Walia £96 / 3 konw., Irlandia Płn. £164 / 1, Szkocja £200 / 0, Londyn £271 / 1.
- **GSC yellowscarftherapy.co.uk, 90 dni:** 43 kliknięcia (+39%), 1 139 wyświetleń, poz. 12,5. Zapytania: marka („yellow scarf support” 3/90) i **burnout** („burnout counselling uk” poz. 31, „burnout counselling” 56, „burnout therapist” 35, „therapy for burnout uk” 53) plus „difference between low mood and depression”. Strona /stress-and-burnout.html poz. 42 przy 98 wyświetleniach; blog „overthinking at night” 141 wyświetleń, 0 kliknięć. /fees i /book-a-session poza top 20.
- GA4: Paid Search 246 sesji / 65 s / 0 kluczowych; **AI Assistant 7 sesji (chatgpt.com), 86% zaangażowania** — więcej niż z Referral.

### 2.3 FUNDACJA — Ads 798-577-2656 (yellowscarf.org, Yellow Scarf CIO, Ad Grants)

| Źródło | Wynik (90 dni) |
|---|---|
| Google Ads API | **brak** — link MCC w stanie PENDING (wymaga drugiego administratora 798, do 20 dni) |
| GA4 538419573, kanały | Direct 944 sesji (zaangażowanie **8,9%**, 15 s, 86% desktop = boty) · Organic 172 (62,8%) · Referral 46 · Social 24 · **Paid Search 7 sesji, 14,3% zaangażowania, 0 kluczowych** · AI Assistant 3 |
| GA4, kluczowe zdarzenia | `donate_click` 5 (wszystkie Direct, /en-gb); `form_submit` 7 — **nieoznaczone jako kluczowe** |
| GA4, Paid Search w październiku | tylko 2026-10-20: 2 sesje na /pl/potrzebuje-pomocy.html, 0% zaangażowania |
| GSC sc-domain:yellowscarf.org | 113 kliknięć (−16%), 5 334 wyświetleń, poz. 7,4. Zapytania: niemal wyłącznie marka i jej literówki („yellow scarf” 2 529 wyśw. / 8 klik.), „superwajzor” 518 wyśw. / 0; „counselling evesham” 2/10; „lgbtq therapist near me” 2/7. **Zero polskojęzycznych zapytań o pomoc.** Stare adresy `uk.yellowscarf.org` nadal w indeksie. |

[W] Wymogi Ad Grants (sprawdzone 24.10.2026, support.google.com/grants/answer/117827 i /nonprofits/answer/9314402): CTR konta ≥ 5% co miesiąc (dwa kolejne miesiące poniżej = dezaktywacja), ≥ 1 konwersja miesięcznie, Smart Bidding oparty na konwersjach, ≥ 2 grupy na kampanię, ≥ 2 sitelinki, geotargeting tylko tam, gdzie usługa, brak słów jednowyrazowych i zbyt ogólnych, QS 1–2 do wstrzymania, odpowiedź na ankietę. **Przy 7 sesjach w 90 dni konto albo nie emituje, albo emituje bez kliknięć — obie sytuacje grożą zawieszeniem.** Google komunikuje to głównie powiadomieniem w koncie, którego bez panelu nie widzę.

---

## 3. Wnioski

**Ośrodek (733)**
1. Konto ogranicza budżet, nie jakość: Leads 1 traci 36% wyświetleń przez budżet przy £67/konw. Każdy funt przeniesiony z Par (£206–252) i Londynu (£174) do Leads 1 kupuje lead 2,5–3,5× taniej. Przesunięcie z 23.10 jest zgodne z danymi; jest przestrzeń na kolejny krok, jeśli kalendarz potwierdzi, że leady z Leads 1 stają się pacjentami.
2. Pary to problem strony, nie słów: CTR 9,7% (ludzie klikają), ale strona docelowa zamienia 2,8% sesji w zgłoszenie wobec 10–25% na innych stronach. Dopóki /pl/terapia-par-po-polsku-w-uk-online.html nie zostanie przebudowana, podnoszenie budżetu Par jest wyrzucaniem pieniędzy.
3. Największe ryzyko regulacyjne konta to grupa UZALEŻNIENIA. Jest formalnie „zamrożona”, ale wydała £2 487 w 90 dni i emituje pod „terapia alkoholowa”, „leczenie alkoholizmu w uk”. Polityka Google „Addiction services” (sprawdzona 24.10.2026) obejmuje „recovery-oriented drug and alcohol addiction services”, a certyfikacja istnieje tylko w AU, CA, FR, IE, NZ, US. Od 12.06.2026 Google rozszerza też politykę „Limited ad serving” na Search, a historia zgodności jest jednym z siedmiu czynników. Jedno odrzucenie może ograniczyć emisję całego konta, nie tylko tej grupy. To decyzja Rafała, nie moja, ale musi być świadoma: ta grupa daje ok. 1/3 konwersji Leads 1 po £74.
4. Struktura ma dwa błędy techniczne, które kosztują: to samo słowo w 5 grupach (kanibalizacja, QS 3 w grupie dziecięcej) i ok. £1 900 w 90 dni na słowach bez konwersji, z czego część już wstrzymano.
5. Higiena: auto-apply dla RSA włączony; sitelink/ruch płatny na /pl/kontakt.html, który nic nie daje; partnerzy wyszukiwania i YouTube w PMax £214 bez konwersji; działania konwersji Fundacji na koncie CIC; podwójne `form_submit` w GA4 (błąd tagu, Selten).
6. SEO to największa niewykorzystana dźwignia: główna fraza na 2. stronie Google, strona usług na pozycji 20, treści o uzależnieniach ciągną ruch, którego nie chcemy, i 51% wyświetleń z Polski. Wszystko, co płacimy w Ads za „polski psycholog uk” (£1 032 / 90 dni za jedno słowo), można częściowo odzyskać organicznie w 3–6 miesięcy.

**Mental (311)**
7. Przy 2 konwersjach miesięcznie żadna strategia licytacji nie ma danych (Google: ok. 50 konwersji do kalibracji; Optmyzr: brak kont, które przy <25 konwersjach działały lepiej niż przy >50). Utrata przez ranking 60% to w połowie artefakt Maks. konwersji na zatkanym budżecie, a w połowie QS 3 za stronę docelową.
8. Ekonomia nie domyka się o rząd wielkości: £259 za lead przy progu £52 (1 z 3 leadów zostaje klientem) i przy historycznym domknięciu 0 z ~67 kontaktów. Nawet idealna strona (×2–3) nie zamknie tej luki, jeśli proces po zgłoszeniu nie zamienia kontaktów w klientów.
9. Anglojęzyczne zapytanie „private counsellor” jest w UK lokalne i katalogowe (Counselling Directory, Psychology Today, BACP „find a therapist” pojawia się w naszych hasłach jako konkurent). Praktyka wyłącznie online bez marki przegrywa z lokalnym gabinetem i z katalogiem. Jedyna nisza, w której witryna sama zaczyna się pokazywać, to **burnout** (pozycje 31–56 — do zdobycia treścią, nie reklamą).
10. Google już wie, że /book-a-session jest słaby (QS „poniżej średniej”). Brief dla Seltena z 15.10 istnieje. Bez tej strony dalsze wydawanie £500/mies. nie jest testem, tylko kosztem.

**Fundacja (798)**
11. Grant jest de facto nieużywany, a wymogi programu są miesięczne. Najpilniejsze działanie na trzech kontach to odczyt panelu 798 (nawet zrzuty ekranu).
12. Polskojęzyczne zapytania o pomoc nie trafiają na yellowscarf.org ani organicznie, ani płatnie. Nie dlatego, że ich nie ma („polski psycholog uk za darmo” ma na osrodek.uk pozycję 1,6 i 209 wyświetleń; „darmowa terapia uzależnień uk” 37), tylko dlatego, że Fundacja nie ma stron, które by na nie odpowiadały, a te zapytania trafiają na komercyjną stronę Ośrodka, gdzie nie ma dla nich oferty. To jest luka, którą grant może zamknąć bez złotówki: ruch „za darmo / grupa wsparcia / pomoc psychologiczna po polsku” należy do Fundacji.

---

## 4. Rekomendacje (priorytet, ryzyko, co i dlaczego). Nic nie wdrożone.

### 4.1 OŚRODEK 733

| # | Priorytet | Co | Dlaczego / dowód | Ryzyko | Wymaga |
|---|---|---|---|---|---|
| O1 | **1 — decyzja** | **Grupa UZALEŻNIENIA**: wybrać świadomie jedną z trzech dróg: (a) wstrzymać grupę i słowa alkoholowe; (b) przebudować na „współuzależnienie / rodzina osoby pijącej” bez obietnicy leczenia i bez słów „terapia alkoholowa”, „leczenie alkoholizmu” (nadal szara strefa); (c) zostawić i przyjąć ryzyko. | £2 487 / 33,5 konw. w 90 dni, ale polityka Addiction services bez certyfikacji w UK; Limited ad serving liczy historię zgodności. | (a) −1/3 konwersji Leads 1 na krótko; (c) ryzyko odrzuceń i ograniczenia emisji całego konta. | Decyzja Rafała |
| O2 | 1 | Słowa bez konwersji (90 dni, >£30/0): wstrzymać 14 nadal aktywnych, m.in. „terapia małżeńska” (Pary, QS 3), „psycholog konsultacja online”, „pomoc w uzależnieniach”, „psycholog rodzinny”, „terapia małżeńska online”, „polski psycholog londyn” (w Leads 1, Londyn wykluczony), „terapia z psychologiem”, „jak pomóc alkoholikowi” (WR). Lista w pliku surowym A5. | ok. £1 100 w 90 dni bez zgłoszenia; przy budżecie ograniczonym to pieniądz zabrany Leads 1. | Niskie; odwracalne. | „tak” Rafała, jedna partia |
| O3 | 1 | Dedup słowa „psycholog polski uk / polski psycholog uk”: zostawić w OGÓLNY (QS 7, £53), wstrzymać kopie w PSYCHOLOG ONLINE, DZIECIĘCY (QS 3), PSYCHOTERAPIA ONLINE, TERAPIA PAR; w tych grupach dodać je jako wykluczenia na poziomie grupy. | Google wybiera grupę aukcją; dziś 40% kliknięć na tę frazę idzie do grup z koszt/konw. £102–111 lub 0. | Niskie; przez 1–2 tyg. lekki spadek wolumenu grupy. | „tak” |
| O4 | 1 | Wykluczenia (konto + lista współdzielona dla PMax): nazwy innych organizacji („polskie centrum pomocy rodzinie”, „opoka”, „instytut psychologii związków”), leki („leki”, „psychotropy”, „tabletki”), nazwiska spoza zespołu, angielskie ogólne („mental health”, „restlessness”), „praca”, „kurs”, „za darmo / bezpłatn* / nhs” (Ośrodek nie ma darmowej oferty; te zapytania należą do Fundacji). | Hasła 30 dni A6/A6b; „opoka uk” dało konwersję, ale to osoba szukająca innej organizacji. | Niskie. | „tak” |
| O5 | 2 | Pary: zostawić £12/dz, **nie podnosić** do czasu nowej strony; brief dla Seltena: strona /terapia-par… z nazwiskami terapeutów par, ceną, formularzem na stronie, 3–4 pola, „co dzieje się po wysłaniu”. Po wdrożeniu test 4 tygodnie. | 2,8% vs 10–25% konwersji sesji na innych stronach; CTR 9,7% pokazuje, że popyt jest. | Brak. | Brief (napiszę), Selten |
| O6 | 2 | Budżet: jeśli kalendarz za 1–23.10 potwierdzi, że leady Leads 1 stają się pacjentami w akceptowalnym koszcie, podnieść Leads 1 o ≤20% (do £130/dz) jednym ruchem; więcej niż 20% resetuje uczenie. London: jeśli do 20.11 nadal ≤2 konw./mies., ściąć do £15 i przenieść do Leads 1. | Leads 1 traci 36% wyświetleń przez budżet; London £174/konw. | Średnie: więcej leadów = więcej pracy Gośki; sprawdzić pojemność kalendarza. | Dane z kalendarza, „tak” |
| O7 | 2 | PMax-1: wstrzymać grupy plików „psychologia i psychoterapia” (£225/0) i „zespół” (£39/0); wymienić 5 tekstów z 20.10 (superlatyw, „skuteczna”, literówki). | Pliki A12; analiza z 20.10. | Niskie. | „tak” + teksty (gotowe z 20.10) |
| O8 | 2 | Godziny: test wyłączenia 17:00–18:59 w Leads 1 na 4 tygodnie (koszt/konw. £141–198 przy £43–59 w 13–16). Ocena po kalendarzu, nie po Ads. | 90 dni: £1 565 / 9,5 konw. w tych godzinach. Próbka mała — dlatego test, nie decyzja. | Średnie: część osób szuka po pracy; przy budżecie ograniczonym pieniądz i tak przejdzie na inne godziny. | „tak” |
| O9 | 3 | Higiena: wyłączyć auto-apply RSA; wyłączyć partnerów wyszukiwania w Leads 1 (£78/228/0); zamienić sitelink „Kontakt” na „Umów wizytę”; odrzucić 6 rekomendacji LEAD_FORM (dane wrażliwe w formularzu Google, UK GDPR art. 9); usunąć z 733 ukryte działania konwersji yellowscarf.org; dodać wykluczenia krajów PL/DE/NL/TR w Parach i WR. | A9–A11, A8. | Brak. | „tak” |
| O10 | 3 | Reklamy (z 20.10, bez zmian): poprawić {KeyWord} → „Polski Psycholog UK”; dodać jeden nagłówek z konkretem doświadczenia („Pomagamy Polakom w UK od 2020”, „14 psychologów i psychoterapeutów”) — oba fakty są już na stronie (Selten 20.10); test ceny „Sesja Online 50 Min: £65” w jednej reklamie. | Badania: lata doświadczenia i specjalizacja = 51,6% wagi decyzji (Jørgensen i Makransky 2022); koszt = bariera nr 1 (BACP 2026: 35%). | Test ceny może obniżyć CTR, ale podnieść jakość zgłoszeń. | „tak” |
| O11 | 2 (strona) | Selten: naprawić podwójne `form_submit` (GTM); zdecydować o „bezpłatnej konsultacji 15 min” na /pl/oferta.html (albo jest i mówimy o niej, albo jej nie ma i znika ze strony); ujednolicić „konsultacja £65” vs „terapia indywidualna £65”. | GA4 D1; analiza 20.10 D1. | Brak. | Decyzja Rafała + Selten |
| O12 | **2 — SEO** | Plan 90 dni dla osrodek.uk (szczegóły §5): 3 strony filarowe („polski psycholog w uk”, „polski psycholog dziecięcy uk”, „terapia par po polsku uk”), porządek techniczny (duplikaty /pl/pl/, literówki, stare profile → 301), sygnał geograficzny UK (hreflang pl-GB, GSC targeting, treść „w Anglii/Szkocji/Walii”), schema MedicalBusiness + Person dla 14 terapeutów, Google Business Profile (jeśli jest adres/obszar), opinie. | GSC E1: „polski psycholog uk” poz. 10,2 / 671 wyśw. / 2 klik.; strona usług poz. 20,2; −29% kliknięć kw/kw. | Brak ryzyka; efekt za 3–6 mies. | Selten, Rafał (GBP) |

### 4.2 MENTAL 311

| # | Priorytet | Co | Dlaczego / dowód | Ryzyko | Wymaga |
|---|---|---|---|---|---|
| M1 | **1 — decyzja 1.11** | **Rekomenduję wariant A:** wstrzymać wydatek Search do czasu nowej strony /book-a-session i przenieść £350–400/mies. na obecność własną: Psychology Today (8 profili, 6 mies. £0), Counselling Directory (w tym bezpłatny wpis CIO jako charity), BACP/NCPS/UKCP directory tam, gdzie członkostwo jest potwierdzone dokumentem, Google Business Profile, rejestr Healthcode i panele ubezpieczycieli dla terapeutów spełniających próg. Powrót do Ads w lutym 2027 z nową stroną, kampanią brandową i jedną kampanią „online therapy uk / private therapist online” z pinowaną marką. **Wariant B:** zostać przy £16,45/dz tylko pod warunkiem, że nowa strona wejdzie w listopadzie; wtedy M2–M5. | £259/lead vs próg £52; 0 klientów z ~67 kontaktów; 54% kosztu w hasłach niewidocznych; katalogi i „bacp find a therapist” są naszymi konkurentami w aukcji — taniej być w nich niż licytować przeciw nim. Healthcare: 52,6% cytowań AI z katalogów (Yext 2025). | A: tracimy ciągłość danych (i tak za małych). B: kolejne £500/mies. bez zmiany wyniku. | Decyzja Rafała |
| M2 | 1 (jeśli B) | Opis reklamy A: „HCPC-registered psychologist or psychotherapist” → „An HCPC-registered psychologist or a qualified psychotherapist” (CAP 3.1/3.7; HCPC nie rejestruje psychoterapeutów). Sprawdzić, czy zmiana reklam z 23.10 to już objęła. | Analiza 20.10 A1; historia zmian 23.10: 2 reklamy UPDATE. | Brak. | Odczyt + ew. „tak” |
| M3 | 1 (jeśli B) | Marka pinowana na pozycji 1 w reklamie B („Yellow Scarf Therapy”); usunąć „Therapy For Grief” (żałoba to w UK kategoria darmowa: 9/9 wyników organicznych instytucjonalnych). | 20.10 A3; Limited ad serving: jasność marki + pinowanie domeny/marki. | Spadek „siły reklamy” — bez znaczenia dla aukcji. | „tak” |
| M4 | 2 (jeśli B) | Wykluczenia: nazwy praktyk i organizacji z hasła (A6 311: 20+ nazw), „near me”, nazwy miast przy usłudze online (albo odwrotnie: zostawić miasta, bo online obsługuje całe UK, ale wtedy strona musi to mówić), „bereavement/grief/loss”, „free”, „nhs”, „bacp find”. | 49 widocznych haseł, 0 konwersji. | Niskie. | „tak” |
| M5 | 2 | GA4: oznaczyć `form_submit` na /book-a-session jako kluczowe (bez importu do Ads — Ads ma własny tag); dodać zdarzenie „telefon kliknięty” na stronie; raport tygodniowy Nikoli: liczba telefonów, źródło, co dalej. | GA4 0 kluczowych; telefon 0 w 30 dni. | Brak. | Selten / Rafał |
| M6 | **2 — SEO/GEO** | Klaster „burnout” (jedyna nisza z sygnałem): przebudować /stress-and-burnout.html (poz. 42) jako stronę usługi z nazwiskami, ceną, formularzem; 3 artykuły wspierające (różnica low mood vs depression już ma wyświetlenia); FAQ z 40–60-słowymi odpowiedziami; schema MedicalBusiness + Person; profil GBP „Psychotherapist”, obszar usług UK, „online appointments”. | GSC E2: burnout poz. 31–56; ChatGPT już daje 7 sesji o zaangażowaniu 86%. | Brak; efekt 3–6 mies. | Selten, Nikola (treść kliniczna) |
| M7 | 3 | Wstrzymana kampania „Google AI Test | Broad”: zostawić wstrzymaną, ale wyłączyć w niej AI Max i auto-teksty, żeby przypadkowe włączenie nie uruchomiło broad match. Zasób LEAD_FORM 355420073667 — usunąć. Duplikaty działań telefonicznych — usunąć. | B1, B5, B7. | Brak. | „tak” |

### 4.3 FUNDACJA 798

| # | Priorytet | Co | Dlaczego / dowód | Ryzyko | Wymaga |
|---|---|---|---|---|---|
| F1 | **1 — pilne, do 28.10** | Odczyt panelu 798: Rafał loguje się jako infoyellowscarf@gmail.com i wysyła zrzuty ekranu: Przegląd (ostatnie 30 dni), Kampanie (status, budżet, wyświetlenia, CTR), Menedżer zasad (odrzucenia), dzwonek powiadomień, Cele → Konwersje. Alternatywnie sesja na Macu z Chrome, tylko odczyt. | 7 sesji płatnych w 90 dni; wymogi CTR 5% i 1 konwersja/mies.; dezaktywacja po 2 miesiącach; zawieszenie za naruszenie bez powiadomienia. | Brak (odczyt). Brak działania = ryzyko utraty grantu. | Rafał: 10 minut |
| F2 | 1 | Dokończyć link MCC (drugi administrator 798 musi zaakceptować w Admin → Dostęp i bezpieczeństwo → Menedżerowie). | Bez tego każdy przegląd Fundacji to ręczne zrzuty. | Brak. | Rafał + drugi admin |
| F3 | 1 | Konwersje grantu: w GA4 538419573 oznaczyć `form_submit` jako kluczowe i podpiąć do 798 (import GA4), dodać zdarzenia „zapis na grupę” i „kliknięcie telefonu/e-maila”; `donate_click` zostaje. Wyrzucić reguły, które liczą czas na stronie. | Google: „meaningful conversion”, min. 1/mies.; dziś 5 donate_click w 90 dni i 7 nieoznaczonych formularzy. | Niskie. | Selten + panel 798 |
| F4 | 2 | Struktura kampanii grantowej pod polskojęzyczne zapytania o pomoc (szczegóły §6): 3 kampanie Search × 2–3 grupy, Maks. konwersji, UK, język PL, słowa 2–4-wyrazowe, bez słów jednowyrazowych; osobna kampania EN dla Evesham/Worcestershire (grupy, wolontariat, darczyńcy). **Najpierw strony:** /pl/potrzebuje-pomocy.html, /pl/grupy-wsparcia.html i jedna strona na każdą realną grupę z terminem, ceną i zapisem. | GSC: zero polskich zapytań pomocowych na yellowscarf.org, a na osrodek.uk „polski psycholog uk za darmo” poz. 1,6 i „darmowa terapia uzależnień uk” — ten ruch powinien lądować w Fundacji. Cel 2026: 4 grupy × 6–8 osób. | CTR < 5%, jeśli słowa za szerokie; stąd ścisłe dopasowanie i wykluczenia. | Treść stron (Selten), panel 798 |
| F5 | 2 | PMax w Ad Grants (dostępny od 2025, inventory Search + Maps) tylko wtedy, gdy Fundacja ma Google Business Profile z adresem w Evesham; wtedy Maps = tanie lokalne zasięgi dla grup 60+. | Google for Nonprofits, 11.06.2025. | Niskie; na Ad Grants nie ma kosztu. | GBP, panel |
| F6 | 3 | Techniczne: filtr botów / wykluczenie ruchu Direct desktop bez zaangażowania w GA4 (944 sesji, 15 s); przekierowania 301 ze starych adresów `uk.yellowscarf.org`; Consent Mode na stronie (dziś GA4 widzi tylko zgody). | D3, E3. | Brak. | Selten |

---

## 5. SEO i GEO — co mówią źródła i co z tego dla nas (sprawdzone 24.10.2026)

**Fakty ze źródeł (≤ 12 miesięcy):**
- Seer Interactive (24.04.2026, 53 marki, 5,47 mln zapytań): gdy pojawia się AI Overview, CTR organiczny spada z 3,19% do 1,31% (XII.2025) i odbija do 2,36% (II.2026); marka cytowana w AIO ma o 120% więcej kliknięć niż niecytowana, ale wciąż o 38% mniej niż bez AIO. **Płatny CTR przy AIO rośnie** (14,6% → 16,2%). Korelacyjne.
- Yext (10.2025, 6,8 mln cytowań ChatGPT/Gemini/Perplexity): 86% cytowań pochodzi ze źródeł kontrolowanych przez markę; **healthcare: 52,6% z katalogów i wizytówek** (najwięcej ze wszystkich branż).
- SOCi Local Visibility Index (17.02.2026): ChatGPT poleca 1,2% lokalizacji vs 35,9% w 3-pack Google; polecane mają ≥ 4,3★, odpowiadają na opinie, spójny NAP.
- Similarweb GEO guide (23.03.2026, za Princeton 2024): treści ze statystykami i cytatami +30–40% widoczności w odpowiedziach AI; AirOps: tylko 30% marek utrzymuje się między kolejnymi odpowiedziami.
- SEO dla terapeutów 2026 (seofortherapists.org 23.05.2026, scoutrival 2026): 1 strona na specjalizację i 1 na obszar; YMYL: kwalifikacje tekstem, „ostatnio sprawdzone przez”; schema MedicalBusiness + Person; GBP dla praktyk online = obszar usług, map pack ograniczony; **nie prosić klientów o opinie** (etyka) — budować wiarygodność profilami, katalogami i treścią.
- Ads w AI Mode / AI Overviews: w UK jeszcze nie ma (the7stars 2025; status 24.10.2026 bez zmian w dostępnych źródłach); kwalifikują broad match / AI Max / PMax, których nie używamy. Healthcare wykluczone z AIO ads (notatka 15.10). Nic do roboty.

**Co to znaczy dla trzech stron:**
- **osrodek.uk:** AI Overviews praktycznie nie dotyczą polskojęzycznych zapytań w UK (brak danych, ale wolumen i język poza priorytetem Google). Spadek −29% to raczej utrata pozycji (desktop 13,7) i przesunięcie w stronę treści o uzależnieniach niż AIO. Priorytet: pozycje 8–15 na frazach komercyjnych → top 5. To 3 strony filarowe + technika + GBP. Szacowany efekt: „polski psycholog uk” z 671 wyświetleń przy pozycji 10 na pozycję 3–5 to ok. 30–60 dodatkowych kliknięć miesięcznie, czyli £80–160 miesięcznie oszczędności w Ads na jednej frazie.
- **yellowscarftherapy.co.uk:** tu AIO i ChatGPT już działają (AI Assistant > Referral). GEO w praktyce = katalogi (Psychology Today, Counselling Directory, BACP/NCPS tam, gdzie wolno), GBP, strona „o nas” z faktami (liczby, lata, kwalifikacje tekstem), FAQ z krótkimi odpowiedziami, spójne dane we wszystkich miejscach. Treść: burnout jako jedyny klaster z sygnałem.
- **yellowscarf.org:** najpierw treść po polsku o pomocy, potem SEO; AI drugorzędne. Lokalnie (Evesham/Worcestershire) GBP + strona „community wellbeing” po angielsku pod granty i wolontariat.

---

## 6. Ile i gdzie inwestować — propozycja na listopad–grudzień 2026

**Stan dziś (miesięcznie, [F]):** 733 ≈ £5 070 (195 £/dz × 26 dni emisji) · 311 ≈ £494 · 798 £0 gotówki (grant). Razem gotówki CIC ≈ **£5 560/mies.**

**Rynek:** publicznych danych o typowym budżecie małej praktyki w UK nie ma [F]; dostępne benchmarki mówią o koszcie leadu (healthcare £48–52, zdrowie psychiczne £22, US mental health $141). Nie ma publicznego benchmarku kosztu pozyskania **płacącego klienta** terapii w UK — wszystko, co dostępne, to koszt zapytania [F, notatka 15.10].

**Próg opłacalności [Z — do potwierdzenia przez Rafała]:** przy marży ok. £25/sesję i 6–8 sesjach na pacjenta wkład na pacjenta to £150–200; przy domknięciu 1 lead → 1 pacjent na 2–3 leady maksymalny koszt leadu to **£50–100**, a koszt pacjenta nie powinien przekraczać ~£150. Ośrodek przy realnych ~£45–55 za lead i domknięciu 1:2–1:3 mieści się w tym progu; Mental przy £259 nie mieści się przy żadnym domknięciu.

| Konto | Dziś | Propozycja XI–XII | Warunek | Oczekiwany efekt |
|---|---|---|---|---|
| 733 Leads 1 | £110/dz | **£110 → £130/dz** (+18%, jeden ruch) | Kalendarz za 1–23.10 potwierdza koszt pacjenta ≤ £150 i jest miejsce w grafikach | +15–20% leadów przy podobnym koszcie (traci 36% przez budżet) |
| 733 PMax-1 | £35 | £35 (bez zmian) + porządki O7 | — | £68–94/konw.; stabilny |
| 733 Pary | £12 | £12 do nowej strony; potem £25 | Nowa strona (O5) | £206 → cel ≤ £100 |
| 733 London | £30 | £30 do 20.11, potem £15 lub 0 | ≥ 3 konw./mies. | — |
| 733 Kryzysowa, WR | £7, £1 | bez zmian | — | — |
| **733 razem** | **£195/dz** | **£215/dz (≈ £5 600/mies.)** | | |
| 311 Search | £16,45/dz | **Wariant A: £0 (pauza) · Wariant B: £16,45** | A: decyzja 1.11; B: nowa strona w XI | A: −£494/mies. |
| 311 obecność własna | £0 | **£350–400/mies.** przez 6 mies. (Psychology Today ×8 po okresie darmowym £160/mies., Counselling Directory ×8 ≈ £165/mies. w ujęciu rocznym, BACP directory £6/mies.) + jednorazowo strona /book-a-session i klaster burnout (Selten, wycena) | Profile wypełnione (lata, specjalizacja, cena, zdjęcia) | Pierwsze zapytania z katalogów po 4–8 tyg.; mierzyć log Nikoli |
| 798 Ad Grants | £0 | £0 gotówki; cel wykorzystania grantu **£300–1 000/mies.** na polskojęzyczne zapytania | Panel + strony + konwersje (F1–F4) | 1–3 zapisy na grupy miesięcznie w pierwszym kwartale; spełnienie wymogów programu |
| **Gotówka CIC razem** | **≈ £5 560** | **≈ £5 950–6 000** (A) | | Ta sama suma rzędu, lepszy miks: więcej w sprawdzony silnik, zero w kanał bez wyniku, pierwszy raz pieniądze w obecność własną |

**Maksimum, gdyby koszt pacjenta się zgadzał:** Leads 1 traci 36% wyświetleń przez budżet, więc do ok. £170/dz (≈ £4 400/mies. na samej Leads 1) koszt leadu powinien rosnąć łagodnie; powyżej tego wchodzimy w utratę przez ranking (28%) i koszt rośnie szybciej. Granicą jest pojemność 14 terapeutów, nie Google. Podnosić krokami ≤ 20% co 3–4 tygodnie, zawsze po kalendarzu.

**SEO jako inwestycja jednorazowa [Z]:** 3 strony filarowe + technika + schema + GBP dla osrodek.uk oraz strona /book-a-session i klaster burnout dla Mental to w realiach małej agencji rząd £1 500–3 000 jednorazowo (do wyceny u Seltena). Zwrot: każda fraza komercyjna przeniesiona z pozycji 10 na 3–5 oszczędza £80–160/mies. w Ads; Pary z 2,8% na 10% konwersji sesji to przy obecnym budżecie ok. 6–8 dodatkowych zgłoszeń miesięcznie.

---

## 7. Zasady i źródła (sprawdzone 2026-10-24)

**Oficjalne Google**
- Ad Grants: Policy compliance guide (support.google.com/nonprofits/answer/9314402) i Account management policy (support.google.com/grants/answer/117827): CTR ≥ 5%/mies., ≥ 1 konwersja/mies., Smart Bidding oparty na konwersjach, ≥ 2 grupy, ≥ 2 sitelinki, geotargeting, bez słów jednowyrazowych/ogólnych, QS 1–2 do wstrzymania, ankieta; naruszenie = zawieszenie bez powiadomienia. Limit CPC $2 nie dotyczy Maks. konwersji (Whole Whale, akt. 05.2026). PMax i Maps w Ad Grants od 2025 (blog.google 11.06.2025).
- Healthcare and medicines (adspolicy/answer/176031, en-UK): dla psychoterapii/counsellingu w UK brak certyfikacji; telemedycyna lekowa wymaga LegitScript. Addiction services (15598649): certyfikacja tylko AU, CA, FR, IE, NZ, US.
- Health in personalised advertising (16701855): bez zmian; aktualizacja 17598957 (3.09.2026, od 30.10.2026) dotyczy tylko alkoholu na YouTube.
- AI Max for Search (google-ads/answer/15909989): domyślnie włączony w nowych kampaniach Search; wyłączać w kreatorze (zgodne z zasadą stałą).
- Limited ad serving (ppc.land 5.08.2026 za Google): rozszerzony na Search 12.06.2026 i na wszystkie produkty w sierpniu 2026, pełne wdrożenie do 2028; czynniki: dojrzałość konta, weryfikacja reklamodawcy, jasność marki, historia zgodności; zalecenia: weryfikacja, marka w reklamie i na stronie, pinowanie domeny/marki.
- Smart Bidding: kalibracja ok. 50 konwersji / 3 cykle (answer/13020501), zalecenie 50 konwersji przed zmianami (12563349) — z notatki 15.10, bez zmian.

**Branżowe (data publikacji)**
1. Medico Digital, UK Healthcare Paid Search Benchmarks 2025 (XII.2024–XI.2025; £5,5 mln, 433 kampanie) — mental health CPC £1,02, CTR 6,28%, CVR 4,69%, CPA £21,74; healthcare CTR 6,55%, CPC £1,86, CPA £47,91.
2. Ridley Digital, Google Ads costs 2026 UK (26.06.2026, rev. 09.2026) — healthcare CPC £2,85, CPL £51,80.
3. LocaliQ, Healthcare Search Benchmarks (13.01.2026; X.2024–IX.2025, US) — mental health CTR 4,46%, CPC $4,22 (+42%), CVR 1,85% (−61%), CPL $141 (+146%).
4. Benchmarketing, Mental Health benchmarks (akt. III.2026, US) — CPC $4,76, CTR 6,61%.
5. Seer Interactive, AIO Impact on Google CTR: 2026 Update (24.04.2026).
6. Yext Research, AI citations (9.10.2025) — 86% cytowań ze źródeł kontrolowanych; healthcare 52,6% z listingów.
7. SOCi, Local Visibility Index (17.02.2026).
8. Similarweb, GEO guide (23.03.2026) i AirOps 2025.
9. OpenLens, How AI recommends local businesses — source audit (2026; przegląd Whitespark, BrightLocal, Doctor Rank, Semrush).
10. NAV43, When not to use Performance Max for lead gen (4.05.2026) + Adalysis 2025 (3 300 kampanii: Search > PMax na tych samych hasłach).
11. Hellyeah, Smart Bidding playbook (19.10.2026) — < 15 konw./mies. → Maks. konwersji bez tCPA; zmiana budżetu > 20% resetuje uczenie.
12. Web Tonic, Health & wellness landing page benchmarks (akt. 9.10.2026, za Unbounce/FoundryCRO) — mediana CVR healthcare 3,8–5,1%; 3–5 pól formularza; desktop konwertuje o 22% lepiej.
13. seofortherapists.org, SEO for Therapists 2026 (23.05.2026) i Scoutrival, Local SEO for therapists 2026.
14. Whole Whale, Ad Grants policy updates (akt. 20.05.2026) i 2025 PMax/Maps update.
15. the7stars, Google AI Mode — what it means for advertisers (2025; UK bez reklam w AIO/AI Mode).
16. BACP Public Perceptions Survey 2026 (YouGov, n = 5 058, 16.02–6.03.2026) — koszt 35%, kolejki 22%, 26% sprawdza kwalifikacje.
17. ASA, Gary Baron (12.08.2026) — fałszywy claim członkostwa BACP: CAP 3.1, 3.52, 3.53.
18. Hyphenate Consulting, Ad Grant compliance 2026 (3.08.2026) — powiadomienia w koncie, konwersje psują się po migracjach.
19. Optmyzr RSA/bidding (2026) i Jørgensen & Makransky (2022) — z analiz 15.10 i 20.10, bez zmian.
20. Google for Nonprofits blog (11.06.2025) — PMax i Maps w Ad Grants.

**Najważniejsze zasady i ryzyka wynikające ze źródeł:** (1) w UK nie da się legalnie reklamować usług leczenia uzależnień alkoholowych/narkotykowych; (2) Limited ad serving rozszerza się na Search — weryfikacja reklamodawcy i widoczna marka stają się warunkiem pełnej emisji; (3) Ad Grants wymaga miesięcznych minimów — nieaktywne konto to konto do zawieszenia; (4) przy < 15 konwersjach miesięcznie tCPA szkodzi, a PMax dla leadów bez importu offline (zakazanego u nas) optymalizuje ilość, nie jakość; (5) każdy claim członkostwa musi mieć dokument (ASA 12.08.2026); (6) w healthcare widoczność w AI buduje się katalogami i wizytówką, nie „treściami pod AI”.

---

## 8. Czego potrzebuję od Rafała

1. **Fundacja, do 28.10:** zrzuty ekranu panelu 798 (Przegląd 30 dni, Kampanie, Menedżer zasad, powiadomienia, Konwersje) albo zgoda na sesję z Chrome w trybie odczytu. Plus akceptacja linku MCC przez drugiego administratora.
2. **Decyzja O1:** co z grupą UZALEŻNIENIA — (a) wstrzymać, (b) przebudować na rodzinę/współuzależnienie, (c) zostawić świadomie.
3. **Decyzja M1 (do 1.11):** wariant A (pauza Ads, obecność własna) czy B (zostać pod warunkiem nowej strony w listopadzie).
4. **Wartość pacjenta i pojemność:** średnia liczba sesji nowego pacjenta Ośrodka, marża na sesji, ile nowych pacjentów miesięcznie mieści się w grafikach 14 terapeutów. Bez tego progi w §6 są założeniem.
5. **Logi:** raport Gośki od 18.10 i Nikoli od 20.10 (zgłoszenia → sesje).
6. **Weryfikacja reklamodawcy:** w obu kontach (733, 311) Rozliczenia → Weryfikacja reklamodawcy — czy status jest „zweryfikowano”. Z API tego nie widać, a to teraz czynnik emisji.
7. **Google Business Profile:** czy Ośrodek, Mental i Fundacja mają wizytówki (adres w Evesham? obszar usług?). To warunek GEO i Maps w grancie.
8. **Strona oferty Ośrodka:** czy „bezpłatna konsultacja telefoniczna 15 min” istnieje naprawdę.
9. **Zgoda na partię zmian O2–O4, O7, O9** (słowa bez konwersji, dedup, wykluczenia, grupy PMax, higiena) — wszystko odwracalne; zrobię jedną partią, z zapisem „przed / po” przez API.

Kontrola końcowa: konta nie pomylone (733 = osrodek.uk/CIC, 311 = yellowscarftherapy.co.uk/CIC, 798 = yellowscarf.org/CIO, grant); żadna rekomendacja nie obiecuje efektów terapii, nie używa „free/bezpłatna” na kontach komercyjnych, nie proponuje tCPA, broad match, Demand Gen, sieci reklamowej, auto-apply, Customer Match, EC for leads, importu offline ani AI Max; konto grantowe traktowane wg zasad Ad Grants, nie jak komercyjne.
