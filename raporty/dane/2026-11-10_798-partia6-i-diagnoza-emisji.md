# Fundacja 798 — partia 6 (10.11.2026) i diagnoza braku emisji

Konto: 798-577-2656 (yellowscarf.org, Yellow Scarf CIO, Ad Grants). Panel, login infoyellowscarf; tożsamość konta potwierdzana przed każdym odczytem, własna karta. **Na koncie nic nie zmieniono.**

## 1. Partia 6 (Rafał „tak 798 cel” 10.11 10:45) — ZBĘDNA
- Cel domyślny konta „Submit lead form” obejmuje 20/20 kampanii, działanie GA4 form_submit główne.
- Cel „Sign-up” przypięty tylko do wstrzymanej kampanii [EN] Donations (poza zakresem). K1–K3 go nie mają (sprawdzone pośrednio po liczniku kampanii; ekran Ustawień kampanii w tym Chrome otwiera się pusty).
- „Rejestracja (osrodek.uk/umow-wizyte.html)” i „Połączenie 07534116573” = status Removed, nie liczą się w żadnym celu.
- Komunikat „missing a primary conversion action” / „stopped serving” na liście kampanii już nie występuje (dotyczył najpewniej Donations).
- Wniosek: odczyt z 5.11 pokazywał stan sprzed propagacji zmian z 4.11; cele nie są przyczyną.

## 2. Emisja 3–9.11: K1, K2, K3 „Eligible”, 0 wyświetleń (K1: 4 wyśw. / 3 klik. w 30 dni)

### Główna przyczyna: brak wolumenu wyszukiwań w zasięgu limitu CPC
| Kampania | Słowa | „Low search volume” | „Eligible” |
|---|---|---|---|
| K1 [PL] Pomoc po polsku w UK | 86 | 70 | 16 |
| K2 [PL] Fundacja Yellow Scarf | 28 | 18 | 10 (realnie tylko marka „yellow scarf”) |
| K3 [EN] Midlands – Support groups | 74 | 52 | 22 (głównie grupa F „gambling support”) |
| Razem | 186 | 140 (75%) | 44 |

- Słowa LSV nie biorą udziału w aukcji. Pozostałe 44 wg Planera: 0–10 wyszukiwań/mies. w UK („pomoc psychologiczna po polsku”, „grupy wsparcia po polsku”: brak danych; „pomoc dla polaków w uk”: 10).
- Frazy PL z realnym wolumenem („polski psycholog online uk”, „polski psychoterapeuta uk”, ok. 20/mies.) mają stawkę za górę strony $2,63–5,63 → powyżej limitu **$2 (Maks. kliknięć, limit CPC $2 z partii 4.11)**. W Ad Grants limit $2 nie obowiązuje przy strategiach inteligentnych (Maks. konwersji) – oficjalne zasady Ad Grants, odczyt 4.11.2026.
- Wolumen w zasięgu: „gambling support” ~480/mies. (stawka u góry $0,30–7,49, niska konkurencja), „Birmingham” ~30/mies. — oba w K3.
- Wynik Jakości i szacunkowe stawki „—” przy wszystkich 186 słowach (brak danych); słów z QS 1–2: 0.

### Wykluczone
- Reklamy: 14 RSA Eligible (2 w wstrzymanej grupie), 0 odrzuconych, siła Poor–Excellent. Menedżer zasad: brak problemów z reklamami. Rozliczenia: „We don’t bill you”, bez ostrzeżeń. Historia zmian 3–9.11: tylko ręczne zmiany z 4.11; Google nic sam nie zmieniał.

### Nie dało się odczytać (Chrome: „Turn off ad blockers”, dymki/kolumny/ustawienia nie otwierają się)
Udział w wyświetleniach i utracony udział, teksty dymków statusu, ustawienia K1–K3 (lokalizacje, „obecność”, język, sieci, harmonogram, urządzenia, AI Max).

## 3. 🔴 Weryfikacja reklamodawcy
Menedżer zasad: zadanie „Advertiser verification – Organization details required”, termin **4.12.2026** — klika Rafał (Yellow Scarf CIO, charity 1190615, Church House, Market Place, Evesham, WR11 4RW; jeśli Google podpowie „YELLOW SCARF CIC” – stop). Drugie zadanie (zalecane): potwierdzenie źródła finansowania reklam.

## 4. Propozycje do decyzji Rafała (nic nie wdrożono)
| # | Propozycja | Priorytet | Ryzyko |
|---|---|---|---|
| A | K1 i K3 → z powrotem **Maks. konwersji** (bez tCPA). Znosi limit $2 CPC, więc frazy PL z realnym wolumenem ($2,63–5,63) zaczną wchodzić do aukcji. Cel konta z form_submit już działa, więc powód przejścia na Maks. kliknięć z 4.11 zniknął. | 1 | przy 0 konwersji w historii stawki mogą być nierówne; Ad Grants i tak wymaga tej strategii |
| B | K1: dodać 5–8 krótszych fraz PL z wolumenem („polski psycholog uk”, „polski psychoterapeuta uk”, „polski psycholog online uk”, „psycholog po polsku anglia”, „polskie grupy wsparcia uk”…) w dopasowaniu do wyrażenia; bez słów „darmowy/za darmo” (oferta jest odpłatna). Częściowo nakłada się z 733 — rozdzielenie: 733 = terapia indywidualna, 798 = grupy i wsparcie fundacji; w 798 wykluczyć „terapia indywidualna”, „psychoterapeuta prywatnie”. | 2 | kanibalizacja z 733 (ten sam użytkownik może zobaczyć obie reklamy) |
| C | K3: oprzeć emisję na „gambling support” (grupa F) + Birmingham; dodać 5–10 szerszych wariantów phrase po sprawdzeniu w Planerze; ewentualnie podnieść budżet K3 kosztem K2 (K2 realnie tylko marka). | 2 | treści o hazardzie = „Health in personalized advertising” (bez remarketingu), nie Addiction services; LP /en-gb/gambling-support.html (zlecenie Selten) |
| D | Odczyt ustawień K1–K3 (geo/„obecność”, język, AI Max, partnerzy) w oknie incognito lub wbudowanej przeglądarce; wyłączyć AI Max, jeśli włączony. | 1 (odczyt) | — |
| E | Po 30 dniach wyciąć słowa LSV bez wyświetleń (nie teraz). | 3 | — |

Pliki na Macu: ~/Desktop/798_partia6_2026-11-10.md (sekcja „Diagnoza emisji 10.11”), ~/Desktop/798_partia6_2026-11-10.png. Efekt uboczny: Planer zapisał szkic „Plan from Nov 10, 2026, 11 am” (bez wpływu, do usunięcia).
