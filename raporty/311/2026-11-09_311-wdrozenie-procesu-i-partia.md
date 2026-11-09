# Mental 311 — wdrożenie karty „przyszłość kampanii EN” (stan 9.11.2026)

Konto: **Mental**, Google Ads 311-878-5541, yellowscarftherapy.co.uk, YELLOW SCARF CIC (komercyjne), en-GB.
Nie dotyczy kont 733, 798 ani 942. Budżet bez zmian: £16,45/dz. Przegląd: **20.11.2026**.

---

## 1. Stan zadań z karty (odczyt API 9.11, ok. 18:00 UTC; nic nie zmieniono)

| Zadanie | Stan | Dowód |
|---|---|---|
| A. Komponenty automatyczne na poziomie konta (w tym Automated Promotions) | **Nie widać wykonania.** W historii zmian od 2.11 brak takiej zmiany; API nie pokazuje tego ustawienia, więc potwierdzenie tylko w panelu. | change_event 2–9.11: tylko blokady IP (3.11, 5.11) i zmiany z 2.11 (AI Max w „AI Test”, usunięty duplikat „Therapy Fees”). |
| B. Usunięcie automatycznego logo | **Niewykonane.** | Kampania „Private Online Therapy UK”: logo `379899902948`, źródło AUTOMATICALLY_CREATED, status ENABLED (obok Twojego heart-blue.jpg). |
| Test tajemniczego klienta | Brak śladu wykonania. Scenariusz w sekcji 3. | — |
| Proces po zgłoszeniu | Brak wdrożenia, które dałoby się sprawdzić (log Nikoli bez wpisów po 22.10 wg audytu 31.10). Gotowy pakiet w sekcji 4 i arkusz. | — |

Na poziomie kampanii nadal wszystko w porządku: AI Max wyłączony, automatyczne teksty wyłączone w aktywnej kampanii (status 3 = wyłączone dla obu typów).

### Co pokazują telefony z reklam (call_view)

Od 3.11 do 9.11 przyszło **8 połączeń z reklam**:
- 2 nieodebrane w **sobotę 7.11 o 12:34** (dwa razy w ciągu 8 sekund, najpewniej ta sama osoba),
- 6 odebranych, trwały 5–40 sekund; żadne nie przekroczyło 60 s, więc żadne nie liczy się jako konwersja.

Wniosek: ludzie dzwonią, ale rozmowy są bardzo krótkie, a w weekend nikt nie odbiera. Reklamy i rozszerzenie połączeń działają **codziennie 7:00–23:00**, a rozszerzenie połączeń nie ma własnego harmonogramu. To wprost wąskie gardło z karty. Krótkie rozmowy (ok. 30 s) mogą oznaczać pomyłki, pocztę głosową albo osoby, które się rozłączają; tylko Nikola wie, co się w nich działo, dlatego arkusz poniżej ma kolumnę na telefon.

Tydzień 2–8.11: £100,86, 466 wyświetleń, 34 kliknięcia, 0 konwersji w Ads, 6 połączeń.

### Strona (odczyt 9.11)

- /therapists (na nią idzie ruch z reklam od 25.10) i /book-a-session **nie pokazują numeru telefonu ani linku tel:**. Zadanie dla Seltena z 2.11 wciąż otwarte.
- Formularz /book-a-session: imię, nazwisko, e-mail, telefon, wiadomość. **Brak zgody na SMS** (PECR: bez zgody SMS wypada z kadencji, zostaje e-mail i telefon) i **brak informacji, kiedy przyjdzie odpowiedź**.
- „Initial consultation” jest na stronie płatna (£75, 50 min). Słowo „free” nie występuje. Dobrze.

### Uwaga do instrukcji z 3.11

Wzór maila w instrukcji (Krok 3) proponuje „a short, **free** 15-minute call”. To łamie naszą zasadę dla 311 (żadnego „free consultation”; to był jeden z błędów, przez które IV–IX nie dało sesji) i jest sprzeczne ze stroną, gdzie konsultacja kosztuje £75. **Nie używać tego wzoru.** Poprawione teksty są w sekcji 4.

---

## 2. Partia zmian w panelu P-311 (czeka na „tak”)

Jedna partia, wykonanie w panelu przez Twojego Chrome, odczyt API przed i po.

| # | Zmiana | Ryzyko | Odwracalność |
|---|---|---|---|
| P1 | Komponenty → ⋮ → Komponenty automatyczne na poziomie konta → Ustawienia zaawansowane: **wyłączyć wszystkie typy**, w tym Automated promotions, dynamiczne linki, objaśnienia, rozszerzenia informacji, obrazy, logo. | Niskie. Konto ma własne linki, objaśnienia, rozszerzenia i cenę. | Pełna |
| P2 | Kampania „Private Online Therapy UK”: usunąć logo `379899902948` (Automatycznie utworzone). heart-blue.jpg zostaje. | Brak | Pełna |
| P3 | Rozszerzenie połączeń 07400 299702 (`355475357605` w kampanii i `354761003094` na koncie): harmonogram **pn–pt w godzinach, w których Nikola faktycznie odbiera** (założenie: 9:00–17:00 UK). Reklamy dalej działają 7–23 codziennie, poza tymi godzinami prowadzą do formularza. | Mniej telefonów poza godzinami; to zamierzone, bo i tak giną. | Pełna |

Kontrola po zmianie (API): automatyczne logo REMOVED, brak nowych komponentów AUTOMATICALLY_CREATED, call_asset.ad_schedule_targets uzupełnione, budżet £16,45 i AI Max bez zmian. Kontrola tygodniowa 16.11: brak wyświetleń z komponentów „Automatycznie utworzone”.

Potrzebne od Ciebie: godziny odbioru telefonu (jeśli inne niż 9–17).

---

## 3. Test tajemniczego klienta (15–20 minut, do zrobienia w tym tygodniu)

**Kto:** ktoś spoza procesu (Ty albo zaufana osoba), **nie Nikola**. Nikola nie wie o terminie testu.
**Jak wejść na stronę:** wpisać adres ręcznie, **nie klikać reklamy** (klik kosztuje i zaburza dane; formularz z reklamy zapisze się jako konwersja główna).

### 3a. Formularz (dzień roboczy, ok. 10:00)
1. yellowscarftherapy.co.uk/book-a-session, rodzaj: Individual therapy, terapeutka: „I'm flexible”.
2. Imię/nazwisko testowe, prawdziwy e-mail i telefon testera. W wiadomości: „Test enquiry - please reply as you would to a client.” (Bez opisu problemu.)
3. Zanotować godzinę wysłania.

### 3b. Telefon 07400 299702
1. W dzień roboczy ok. 11:00: zadzwonić, poprosić o pierwszą sesję online dla siebie.
2. W sobotę albo po 18:00: zadzwonić drugi raz (sprawdza pocztę głosową i oddzwonienie).

### Co odhaczyć (tak/nie + czas)

| Punkt | Wynik |
|---|---|
| Czy przyszło automatyczne potwierdzenie po formularzu? Z jakiego adresu? | |
| Czas do pierwszej odpowiedzi człowieka (cel ≤ 2 h robocze) | |
| Czy odpowiedź zawiera: imię terapeutki, 2–3 konkretne terminy (UK time), cenę? | |
| Czy jest po brytyjsku, bez polskich nazw dni i bez „free”? | |
| Telefon: odebrany do 3. sygnału? Kto odebrał, jak się przedstawił? | |
| Czy w rozmowie padła cena i konkretny termin? | |
| Poza godzinami: czy jest poczta głosowa po angielsku z informacją, kiedy oddzwonimy? | |
| Czy oddzwoniono i po jakim czasie? | |
| Czy przyszedł follow-up w dniu 2 (jeśli tester nie odpisał)? | |

Po teście: wiersz w arkuszu oznaczyć jako TEST i wykluczyć z liczb na 20.11.

---

## 4. Proces po zgłoszeniu (wersja do wdrożenia)

### Zasady
- **Właściciel:** Nikola. **Zastępstwo:** jedna wskazana osoba (do uzupełnienia przez Ciebie).
- **Godziny obsługi:** pn–pt 9:00–17:00 UK (do potwierdzenia).
- **Formularz / e-mail:** pierwsza odpowiedź **w ciągu 2 godzin roboczych**. Zgłoszenie po 15:00 → do 11:00 następnego dnia roboczego.
- **Telefon nieodebrany:** oddzwonić w ciągu 2 godzin roboczych. SMS tylko, jeśli osoba wyraziła zgodę (dziś formularz jej nie zbiera).
- **Pierwsza odpowiedź zawsze zawiera:** imię i nazwisko terapeutki, link do jej profilu, 2–3 potwierdzone terminy (UK time), realną cenę. Nie „we will be in touch”.
- **Kadencja:** dzień 0, dzień 2 (roboczy), dzień 7. Potem zamknięcie. Bez czwartej próby.
- **Nie piszemy:** „free”, obietnic poprawy, „guaranteed”, zbiorczych akredytacji („all our therapists are BACP…”), słów o uzależnieniach w opisie specjalizacji.

### Dzień 0 — odpowiedź (e-mail)

Subject: Appointment times with [Therapist first name] - Yellow Scarf Therapy

```
Hello [First name],

Thank you for getting in touch. You do not need to have everything figured out
before your first session.

I would suggest [Full name]. You can read about [her] background and
qualifications here: https://yellowscarftherapy.co.uk/therapists/[slug]

I have held these times for a first online session with [her]:

  - [Day, date] at [time] (UK time)
  - [Day, date] at [time] (UK time)
  - [Day, date] at [time] (UK time)

The session is 50 minutes and costs £[fee from the approved rate list], paid by
[payment method] before the session. Booking it does not commit you to a course
of sessions.

Just reply with the time that suits you and I will confirm it today with the
video link. If none of these work, tell me roughly when you are free.

If you would rather talk it through first, you can call me on 07400 299702,
Monday to Friday, [hours] (UK time).

Best wishes,
[Name]
Yellow Scarf Therapy | Yellow Scarf Support CIC
```

Wariant „zgłoszenie bez treści” (tylko imię i e-mail): zapytać krótko, czy to dla siebie czy dla pary i jaka pora dnia pasuje; od razu podać: „Fees start at £75 for a 50-minute online session and depend on the therapist.” Bez pytań o problem.

### Dzień 2 — przypomnienie (jeśli brak odpowiedzi)

Subject: Re: Appointment times with [Therapist first name]

```
Hello [First name],

Just checking my message reached you. The earlier times have gone, but I can
offer these with [Therapist first name]:

  - [Day, date] at [time] (UK time)
  - [Day, date] at [time] (UK time)

If the timing is not right, or you would prefer someone else on the team, just
let me know.

Best wishes,
[Name]
Yellow Scarf Therapy
```

Jeśli zgłoszenie było telefoniczne i jest numer: w dniu 2 najpierw jedna próba telefonu, potem ten mail.

### Dzień 7 — zamknięcie

Subject: Closing your enquiry - Yellow Scarf Therapy

```
Hello [First name],

I have not heard back, so I will close your enquiry here and will not email
again.

If you would like to pick it up later, just reply to this message and I will
send you current times. We keep enquiry details for 12 months and then delete
them.

Best wishes,
[Name]
Yellow Scarf Therapy
```

### Telefon — początek rozmowy

```
"Good morning, Yellow Scarf Therapy, [Name] speaking. How can I help?"
[pause]
"Before we go on, can I take your first name and a number, in case we get cut off?"
"Is this for you on your own, or for you and a partner?"
"Roughly what time of day suits you - daytime, evenings, or either?"
"So you know the cost now: a first session is 50 minutes online, from £75 -
 I will tell you the exact fee for the therapist before you book."
"I can see [Therapist] has [day] at [time], or [day] at [time], UK time.
 Would either of those work?"
```

Cel rozmowy: umówić termin w trakcie rozmowy. Nie dopytywać o problem i niczego o nim nie zapisywać.

### Poczta głosowa (nagrać na 07400 299702)

```
"Hello, you have reached Yellow Scarf Therapy. Sorry we missed your call.
Please leave your first name and number and we will call you back within
two working hours, Monday to Friday, [hours] UK time. You can also book online
at yellowscarftherapy.co.uk. If you need urgent help, please call 999 or
NHS 111."
```

### Arkusz zgłoszeń (bez danych klinicznych i bez danych kontaktowych)

Plik: `/mnt/project-files/raporty/311/Mental-311_arkusz-zgloszen.xlsx`

Jeden wiersz = jedno zgłoszenie, identyfikowane tylko numerem (M-2611-01). Imię, e-mail i telefon zostają w skrzynce/systemie rezerwacji. **Nie wpisujemy:** opisu problemu, diagnozy, treści rozmowy, powodu terapii, nazwiska. Arkusz nie trafia do Google Ads ani żadnego narzędzia reklamowego. Dostęp: Nikola + zastępstwo + Ty. Retencja: 12 miesięcy od ostatniego kontaktu.

Kolumny: ID · data i godzina zgłoszenia · kanał · źródło · indywidualnie/para · data i godzina 1. odpowiedzi · godziny robocze do odpowiedzi · ≤2 h? · terapeutka zaproponowana · D2 wysłane · D7 wysłane · wynik · powód niezabukowania · data 1. sesji · sesja odbyta i opłacona · TEST.

Arkusz ma zakładkę „Podsumowanie” z formułami: liczba zgłoszeń, % odpowiedzi ≤ 2 h, liczba umówionych i odbytych sesji, rozkład powodów. Wykluczenie wierszy TEST jest automatyczne.

---

## 5. Przegląd 20.11.2026 — co przyniosę i jak czytać

Okres: 9–19.11 (proces) i 3–19.11 (Ads).

| Miara | Źródło | Cel na 20.11 |
|---|---|---|
| 1. % zgłoszeń z konkretną odpowiedzią ≤ 2 h robocze | arkusz | ≥ 90% |
| 2. Umówione pierwsze sesje / odbyte i opłacone | arkusz + kalendarz Nikoli | ≥ 2 umówione |
| 3. Powody niezabukowania (cena / termin / inny wybór / brak odp. / nie ta usługa) | arkusz | trend |
| 4. Wydatek, kliknięcia, telefony z reklam (w tym nieodebrane), formularze | API Ads | budżet £16,45/dz bez zmian |
| 5. Koszt umówionej sesji = wydatek ÷ umówione sesje | wyliczenie | próg £52 przy 1 z 3 |

Jak czytać:
- **Miara 1 niska** → decyzja o reklamach nie ma podstaw; naprawiamy wykonanie procesu.
- **Miara 1 wysoka, 0 umówionych** po ok. 10+ zgłoszeniach → problem w ofercie/stronie (cena, terminy, zaufanie, telefon na stronie), dopiero potem reklamy.
- **≥ 1 opłacona sesja** → pierwszy realny koszt pozyskania; nadal bez wzrostu budżetu przed decyzją Rafała.
- Termin 22.11 (test /therapists) wymaga zdarzeń w GA4 538367736 (form_submit i kliknięcie telefonu) — nadal po stronie Seltena.

## 6. Czego potrzebuję od Ciebie

1. „Tak 311” na partię P1–P3 (albo wskazanie, które punkty) i godziny odbioru telefonu.
2. Kto zastępuje Nikolę.
3. Tester do sekcji 3 (Ty lub ktoś zaufany) i dzień testu.
4. Przekazanie Nikoli sekcji 4 i arkusza; start procesu od dnia przekazania.
5. Selten: telefon (tel:) na /therapists i /book-a-session, zdanie „We reply within two working hours, Monday to Friday”, opcjonalnie zgoda na SMS w formularzu.
