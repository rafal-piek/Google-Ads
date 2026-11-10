# Mental 311 — przebudowa reklam (propozycja, 10.11.2026)

Konto: **Mental**, 311-878-5541, yellowscarftherapy.co.uk, YELLOW SCARF CIC, en-GB. Budżet bez zmian: **£16,45/dz**.
Kierunek od Rafała (10.11): „bardziej przebudowa reklam niż zlikwidowanie”. Nic jeszcze nie zmieniono. Wdrożenie tylko po „tak”, jedną partią, z odczytem API przed i po.

## 1. Diagnoza w trzech zdaniach

1. **Kupujemy ruch ludzi, którzy szukają kogoś innego.** W 60 dniach (10.09–9.11) 64% kosztu (£638 z ok. £990) poszło przez jedno słowo „find a private counsellor” w dopasowaniu do wyrażenia. Wyszukiwania to nazwy cudzych gabinetów i miast („tlc chesterfield”, „dudley counselling centre”, „life link glasgow”, „counselling bridgend”) oraz NHS/CAMHS i organizacje charytatywne („camhs poole”, „mind uk counselling”, „age uk bereavement support”, „breathing space scotland”).
2. **Numer w reklamie przyciąga osoby szukające infolinii.** Wśród klikniętych haseł są „mental health number to call”, „helplines for mental health”, „mental health number 24 7”, „childline number”, „anxiety phone number” i „therapist to call right now”. To wyjaśnia, dlaczego Nikola ma ok. 14 pomyłek na 20 telefonów (log X).
3. **Reklama nie mówi, czym nie jesteśmy.** Nigdzie nie pada, że to usługa prywatna, wyłącznie online i nie NHS. Pomyłki są więc przewidywalne.

Lista wykluczeń (247 słów) nie nadąża, bo co tydzień pojawiają się nowe miasta i gabinety. Trzeba zmienić **sposób dopasowania**, a nie dopisywać kolejne nazwy.

## 2. Partia przebudowy R-311 (do jednego „tak”)

| # | Zmiana | Po co | Ryzyko |
|---|---|---|---|
| R1 | Wstrzymać wszystkie słowa w dopasowaniu do wyrażenia (w tym „find a private counsellor”). | Koniec przecieku na cudze gabinety, miasta i NHS. | Spadek wyświetleń, możliwe niewydanie budżetu. |
| R2 | Dodać ok. 24 słowa w **dopasowaniu ścisłym**, każde z „online/video/private” (lista w §3), w dwóch grupach: Individual i Couples. | Ruch tylko od osób, które szukają terapii online. | Mały wolumen. Jeśli przez 14 dni wydajemy mniej niż 50% budżetu, dokładamy 3–4 frazy z „online” w dopasowaniu do wyrażenia. |
| R3 | Nowe wykluczenia (do wyrażenia) na listę master: number, helpline, line, 24/7, 24 7, right now, crisis, nhs, camhs, near me, centre, center, charity, free, childline, samaritans, mind, cruse, age uk, face to face, in person. | Odcina infolinie, NHS, organizacje charytatywne i terapię stacjonarną. | Nie blokuje naszych słów (sprawdzone: żadne słowo z §3 nie zawiera tych tokenów). |
| R4 | Nowa RSA w obu grupach (teksty w §4). D1 przypięty na poz. 1, H „Private Service, Not NHS” lub „Online Only, Not Face to Face” na poz. 2. Stare RSA wstrzymane, nie usunięte. | Pomyłkowe osoby odfiltrowują się, zanim klikną albo zadzwonią. | Niższy CTR, co jest zamierzone. |
| R5 | Strategia: **Maximise clicks z limitem CPC £3,00** na 4 tygodnie zamiast Maximise conversions. | Przy 0–2 konwersjach miesięcznie, w większości pomyłkach, algorytm uczy się na złym sygnale. | Brak optymalizacji pod konwersje do czasu realnego sygnału (form_submit w GA4 + log Nikoli). |
| R6 | Rozszerzenie połączeń zostaje (pn–pt 9–17 od 10.11). | 9.11 były 3 sensowne telefony, 2 z reklamy. | Ocena po 2 tygodniach z logiem Nikoli; jeśli pomyłki nadal >50%, usunąć numer z reklam i zostawić go tylko na stronie. |

Zakazy sprawdzone: bez broad, bez AI Max, bez tCPA, bez auto-apply, bez Display i Demand Gen, bez „free”, bez obietnic efektów, bez BACP, bez słów o uzależnieniach.

## 3. Słowa kluczowe — dopasowanie ścisłe

**Individual – online therapy**
[online therapy uk] · [online therapist uk] · [online counselling uk] · [online counsellor uk] · [private online therapy] · [private online counselling] · [private therapist online] · [private therapy online uk] · [online psychotherapy uk] · [therapy by video call] · [counselling by video call] · [online therapy for anxiety] · [online counselling for anxiety] · [online therapy for stress] · [burnout therapy online] · [private talking therapy uk]

**Couples – online**
[online couples therapy] · [online couples counselling] · [couples therapy online uk] · [online relationship counselling] · [relationship counselling online] · [online marriage counselling] · [couples therapy by video call] · [private couples counselling online]

Stawki: limit CPC £3,00 (średni CPC w ostatnich 60 dniach ok. £3,0).

## 4. Teksty RSA (brytyjski angielski, długości sprawdzone)

Nagłówki (≤30): Private Online Therapy UK · Online Counselling by Video · Sessions by Video, UK-Wide · **Online Only, Not Face to Face** · **Private Service, Not NHS** · Choose Your Therapist · Individuals and Couples · Sessions from £75 · 50-Minute Online Sessions · Book a First Session Online · See Therapist Profiles · Weekday Appointments · Yellow Scarf Therapy · Confidential Online Therapy · Online Couples Counselling

Opisy (≤90):
1. Private online therapy by video across the UK. Not an NHS or crisis service. *(przypięty, poz. 1)*
2. Talk to a qualified therapist from home. Read profiles and choose who you see.
3. You do not need to have everything figured out. Send a booking request today.
4. First session 50 min, from £75. Fees depend on the therapist. Online only.

W grupie Couples zamiast „Individuals and Couples” i „Choose Your Therapist” wchodzą: „Online Couples Therapy” i „Sessions for Couples Online”. Kwota „from £105” dla par dopiero po potwierdzeniu cennika (fees.html: 50 min £105).

„£75” i „qualified” trzeba potwierdzić ze stroną w dniu wdrożenia (fees.html i profile terapeutek). „Weekday Appointments” jest prawdziwe, dopóki telefon działa pn–pt; nie obiecuje terminów wieczornych.

## 5. Strona docelowa (/therapists) — zlecenie dla Seltena

- Pas nad listą terapeutek: „Online sessions by video, anywhere in the UK. We are a private service and not part of the NHS. If you need urgent help, call 999 or NHS 111.”
- Numer telefonu jako link tel: z godzinami „Monday to Friday, 9am–5pm”.
- GA4 538367736: form_submit jako zdarzenie kluczowe i kliknięcie numeru telefonu (R8 z audytu). Bez tego nie zmierzymy przebudowy w Ads.

## 6. Jak ocenimy (pierwsza ocena 2 tygodnie po wdrożeniu, pełna po 4)

| Miara | Dziś | Cel |
|---|---|---|
| Udział kosztu na hasła z nazwą miasta, gabinetu, NHS lub infolinii | szacunkowo ponad połowa (z listy haseł) | < 10% |
| Pomyłki wśród telefonów (log Nikoli) | ok. 70% (X) | < 30% |
| Sensowne zgłoszenia (formularz + telefon) / tydzień | ok. 0–1 | ≥ 2 |
| Umówione pierwsze sesje | 0 od VIII | ≥ 1 w 4 tygodnie |

Decyzja po 4 tygodniach: jeśli ruch jest czysty, ale nadal nie ma umówień, problem leży w ofercie i procesie, nie w reklamach. Wtedy wraca wariant z audytu: pauza Ads i przeniesienie środków do katalogów i SEO.

## 7. Zgodność (skrót)

Kontrola zasad z 10.11 (audyt §3) i 3.11 (11 źródeł): brak zmian zasad dotyczących reklam terapii online w UK. Hasła o stanach zdrowia (anxiety, stress) są dozwolone w Search, ale bez personalizacji i remarketingu. Zdanie „Not an NHS service” jest prawdziwym stwierdzeniem o nas, a nie porównaniem z NHS (CAP 3.33). „From £75” wymaga zgodności ze stroną (CAP 3.17–3.18).
