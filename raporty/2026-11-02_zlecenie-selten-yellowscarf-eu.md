# Zlecenie dla Seltena — yellowscarf.eu (Fundacja Yellow Scarf, Polska) — 2.11.2026

Cel: przygotować stronę do Google Ad Grants dla polskiej fundacji (KRS 0001274628) i do mierzenia zgłoszeń z formularza. To osobny podmiot i osobna strona od yellowscarf.org, więc osobna właściwość GA4 i osobny tag. Termin sugerowany: **do 9.11.2026** (równolegle z weryfikacją fundacji w Google dla Organizacji Non-Profit).

## 1. Indeksowanie i bezpieczeństwo
- Zdjąć `meta robots noindex, nofollow` z całej witryny (WordPress: Ustawienia → Czytanie → odznaczyć „Proś wyszukiwarki o nieindeksowanie”; sprawdzić też ustawienia wtyczki SEO i pliku robots.txt). Wyjątek: strona podziękowania `/dziekujemy/` ma zostać `noindex`.
- Cała witryna w HTTPS, przekierowanie http→https i www→bez www (lub odwrotnie, ale jedna wersja), brak mieszanych treści; sprawdzić ważność i automatyczne odnowienie certyfikatu.
- Po zdjęciu noindex: Google Search Console dla domeny yellowscarf.eu (właściciel: rafal@yellowscarf.eu), zgłosić mapę witryny.

## 2. Nowa strona docelowa reklam: `/pomoc-online/`
Tytuł: „Pomoc psychologiczna online po polsku”. Treść (oryginalna, ok. 400–600 słów), w tej kolejności:
1. Dla kogo: dorośli w Polsce i Polacy mieszkający w Europie; rozmowy po polsku; spotkania online.
2. Jak to działa w 3 krokach: kontakt (formularz lub telefon) → krótka rozmowa o potrzebach → wspólny wybór formy wsparcia. Odpowiedź w dni robocze, zwykle do 2 dni. Bez skierowania i diagnozy.
3. Formy wsparcia: konsultacja psychologiczna, psychoterapia indywidualna, par i rodzin, grupy wsparcia i terapeutyczne, wsparcie dla bliskich osoby w kryzysie. **Na tej stronie nie używamy słów: uzależnienie, alkohol, narkotyki, substancje, hazard, odwyk, terapia uzależnień.** Te treści zostają na innych podstronach.
4. Koszty i misja (akapit do wklejenia): „Część naszych działań finansujemy z grantów i darowizn i oferujemy bezpłatnie. Tam, gdzie obowiązuje opłata, podajemy ją przed rozpoczęciem, a wpływy w całości wspierają cele statutowe fundacji. W uzasadnionych sytuacjach szukamy rozwiązania dla osób w trudnej sytuacji finansowej.”
5. Poufność i kodeks etyki; fundacja nie jest służbą ratunkową; numery 112 i 800 70 2222.
6. Ten sam formularz co na /potrzebuje-wsparcia/ (patrz §4) i telefon +48 453 088 111.
7. Stopka z danymi rejestrowymi (KRS, NIP, REGON, adres) jak na innych stronach.

Druga, lżejsza wersja: `/pomoc-online/polacy-w-europie/` — ta sama struktura plus akapit o pracy online z zagranicy (różnica czasu, terminy wieczorne, w jakich krajach mieszkają osoby, z którymi pracujemy). Obie strony w menu nie muszą być widoczne, ale muszą być dostępne i indeksowalne.

## 3. Pozostałe treści pod politykę witryny Ad Grants
- Akapit o kosztach i misji z §2 pkt 4 także na `/potrzebuje-wsparcia/` i na stronie „O fundacji”.
- „O fundacji”: misja, krótki opis zespołu/zarządu, KRS/NIP/REGON, adres, informacja o fundatorze (Yellow Scarf CIO, nr 1190615). Jeśli jest statut lub sprawozdanie — link do PDF.
- „Wesprzyj nas”: działający, bezpieczny mechanizm darowizn albo co najmniej numer konta, cel wpłat i podziękowanie; strona nie może być tylko przekierowaniem na zewnętrzny portal.
- Brak pustych stron, „w budowie”, zepsutych linków, ikon społecznościowych bez adresu. Sprawdzić wersję `/en/` pod tym kątem (jeśli nie jest gotowa, lepiej ją tymczasowo ukryć niż zostawić puste strony).
- Polityka prywatności: dopisać Google Analytics 4, Google Ads (pomiar konwersji), baner zgody i okres przechowywania danych z formularza.

## 4. Formularz i strona podziękowania
- Pola bez zmian: imię*, e-mail*, kraj*; telefon i „kilka słów” opcjonalne; dla kogo; czego szukasz; preferowany kontakt; zgoda. Zostawić prośbę, by nie opisywać zdrowia w formularzu.
- Po udanym wysłaniu przekierowanie na `/dziekujemy/` (`noindex`): „Dziękujemy. Odezwiemy się w dni robocze, zwykle w ciągu 2 dni.” Ta strona jest celem pomiaru.
- Treść formularza trafia tylko na skrzynkę fundacji (info@yellowscarf.eu). Nic z pól nie trafia do GA4 ani do Google Ads.

## 5. Pomiar: GA4, Tag Manager, zgoda
- Nowa właściwość GA4 „yellowscarf.eu” (strefa Europe/Warsaw, waluta PLN); dostęp Edytor dla rafal@yellowscarf.eu.
- Google Tag Manager na całej witrynie; tag GA4 przez GTM.
- Baner zgody z **Consent Mode v2** (certyfikowany CMP, np. CookieYes, Cookiebot lub Complianz; tryb podstawowy minimum, zaawansowany jeśli prosty do wdrożenia). Kategorie: niezbędne / analityczne / reklamowe; domyślnie bez zgody dla analityki i reklam w EOG.
- Zdarzenia:

| Zdarzenie | Kiedy | Parametry |
|---|---|---|
| `generate_lead` | wejście na `/dziekujemy/` po wysłaniu formularza | tylko `page_location`; bez treści pól |
| `click_to_call` | kliknięcie linku `tel:` | — |
| `click_email` | kliknięcie `mailto:` | — |

- W GA4 oznaczyć `generate_lead` jako zdarzenie kluczowe. Połączenie z kontem Google Ads i import konwersji zrobimy po stronie konta, gdy Ad Grants będzie aktywne.
- Sprawdzić, czy w GTM nie ma zmiennych zczytujących wartości pól formularza (np. wybór „czego szukasz”).

## 6. Kolejność i potwierdzenie
1. §1 (noindex, HTTPS) i §5 (GA4, GTM, zgoda) — najpierw, bo warunkują aktywację i pomiar.
2. §2 i §4 (strona docelowa, podziękowanie).
3. §3 (treści pod politykę witryny).
Po zakończeniu: krótka wiadomość do Rafała z listą zrobionych punktów i adresami nowych stron; sprawdzę je przed aktywacją Ad Grants.
