# Zlecenie dla Seltena – yellowscarf.org (Fundacja, Yellow Scarf CIO) – uzupełnienie z 14.11.2026

Uzupełnia zlecenie z 2.11.2026 (`2026-11-02_zlecenie-selten-yellowscarf-org.md`). Dotyczy wyłącznie strony **yellowscarf.org** i konta Google Ad Grants **798-577-2656** (Yellow Scarf CIO, charity 1190615). Nie dotyczy osrodek.uk, yellowscarftherapy.co.uk ani yellowscarf.eu.

**Dlaczego to pilne.** Konto grantowe musi mieć co najmniej jedną konwersję w miesiącu i CTR powyżej 5%. Dziś reklamy o wsparciu przy hazardzie prowadzą na ogólną stronę „Our projects”, formularze wymagają zbyt wielu danych, a zgłoszenia nie są mierzone. Odczyt strony z 14.11.2026 pokazał, że punkty ze zlecenia z 2.11 nie są jeszcze wdrożone.

## Kolejność prac

| Nr | Zadanie | Priorytet | Szacowany nakład |
|---|---|---|---|
| 1 | Nowa podstrona EN `/en-gb/gambling-support.html` (tekst niżej) | wysoki | 2–3 godz. |
| 2 | Krótsze formularze PL i EN + strona potwierdzenia | wysoki | 1–2 godz. |
| 3 | Zdarzenia GA4: `generate_lead`, `click_to_call`, `click_email` | wysoki | 1–2 godz. |
| 4 | Strona PL o grupach: termin, opłata, zdanie o misji (tekst niżej) | średni | 1 godz. |
| 5 | Rozdzielenie treści Gambling Support i Yellow CAT na „Our projects” | średni | 30 min |

Proponowany termin: 21.11.2026 (dzień kontroli konta).

## 1. Nowa podstrona: `/en-gb/gambling-support.html`

Zasady dla tej strony:
- mówimy o **grupach wsparcia** (support groups, peer support), nie o leczeniu (bez „treatment”, „rehab”, „recovery programme”, „cure”),
- na tej podstronie nie ma treści o alkoholu, narkotykach ani substancjach (to obszar objęty w UK ograniczeniami Google dla reklam),
- żadnych obietnic efektów,
- dane w nawiasach kwadratowych uzupełnia Rafał.

**Title (do 60 znaków):** Gambling Support Groups in Worcestershire | Yellow Scarf

**Meta description (do 155 znaków):** Confidential peer support groups for people affected by gambling, and for their families. Run by Yellow Scarf, a registered charity in Worcestershire.

**Treść strony (gotowa do wklejenia):**

> # Gambling Support Groups
>
> ## A confidential space to talk about gambling
>
> Gambling can affect money, relationships, work and how you feel about yourself. It can also be hard to talk about. Our support groups offer a calm, confidential space to share what is happening and to listen to others who understand.
>
> You do not need to have everything figured out before you get in touch.
>
> ## Who the groups are for
>
> - Adults who are worried about their own gambling
> - Partners, parents and other family members affected by someone else's gambling
> - People who have stopped gambling and would like ongoing peer support
>
> ## How the groups work
>
> - Small groups led by a trained facilitator
> - Where: [Worcester – venue and address] and [Evesham – venue and address]
> - When: [day and time, e.g. Tuesdays 6.30–8.00 pm]
> - Language: [English / English and Polish]
> - Cost: [no charge / £X per session – to be confirmed]
> - What you share stays in the group. You decide how much you say.
>
> ## How to join
>
> 1. Send us a short message using the form below, or call 07340 634326 ([days and hours]).
> 2. We will get back to you within [2] working days to arrange a short introductory conversation.
> 3. You join the next available group.
>
> [Button: Get in touch → /en-gb/i-need-help.html]
>
> ## Support for families
>
> If someone close to you gambles, you may be carrying worry, debt or secrecy on your own. Family members are welcome to contact us and to join a group in their own right.
>
> ## If you need help right now
>
> Our groups are not an emergency service. If you need to talk to someone today, the National Gambling Helpline is open 24 hours a day on 0808 8020 133. If you feel unable to keep yourself safe, call Samaritans on 116 123, or 999 in an emergency.
>
> ## About Yellow Scarf
>
> Yellow Scarf is a registered charity in England and Wales (no. 1190615), based in Evesham, Worcestershire. [One sentence on how the project is funded, e.g. “This project is supported by …”.]

Po publikacji proszę o informację. Zmienimy wtedy adres docelowy reklam o hazardzie na nową podstronę (po akceptacji Rafała).

## 2. Formularze

Dotyczy `/en-gb/i-need-help.html` i `/pl/potrzebuje-pomocy.html`.

| Pole | Dziś | Ma być |
|---|---|---|
| Imię | obowiązkowe | obowiązkowe |
| Nazwisko | obowiązkowe (PL) | usunąć albo opcjonalne |
| E-mail | obowiązkowy | obowiązkowy e-mail **lub** telefon (jedno z dwóch) |
| Telefon | obowiązkowy | jak wyżej |
| Opis sytuacji / „Describe Your Situation” | obowiązkowy (EN) | opcjonalny, z dopiskiem poniżej |

Dopisek przy polu opisu:
- PL: „Nie musisz podawać szczegółów. Wystarczy, że napiszesz, że chcesz porozmawiać.”
- EN: “You do not need to give details. It is enough to say you would like to talk.”

Po wysłaniu formularza osobna strona potwierdzenia:
- PL `/pl/dziekujemy.html`: „Dziękujemy za wiadomość. Odezwiemy się w ciągu [2] dni roboczych.”
- EN `/en-gb/thank-you.html`: “Thank you for your message. We will get back to you within [2] working days.”

Powód: dane o zdrowiu psychicznym to szczególna kategoria danych (UK GDPR, zasada minimalizacji). Każde dodatkowe pole obowiązkowe obniża też liczbę zgłoszeń.

## 3. Pomiar (GA4 538419573)

| Zdarzenie | Kiedy | Parametry |
|---|---|---|
| `generate_lead` | wyświetlenie strony potwierdzenia (nie kliknięcie „Wyślij”) | tylko `form_id`, `page_location` |
| `click_to_call` | kliknięcie linku `tel:` | brak |
| `click_email` | kliknięcie linku `mailto:` | brak |

- `generate_lead` oznaczyć w GA4 jako zdarzenie kluczowe.
- Do GA4 ani do Google Ads nie trafia żadna treść pól formularza, imię, e-mail, telefon ani temat zgłoszenia.
- Tagi uruchamiane dopiero po zgodzie (Consent Mode v2).
- Import zdarzenia do Google Ads zrobimy po stronie konta.

## 4. Strona PL o grupach (`/pl/jak-pomagamy.html`)

Dopisać w sekcji o grupach (dane w nawiasach uzupełnia Rafał):

> **Grupy wsparcia po polsku**
>
> Spotykamy się w małych grupach, od 6 do 8 osób, z prowadzącym. Grupa jest miejscem, w którym można spokojnie porozmawiać o tym, co trudne: o samotności na emigracji, kryzysie, napięciu w rodzinie.
>
> - Najbliższa grupa: [data rozpoczęcia], [dzień tygodnia i godzina], [online / miejsce]
> - Liczba spotkań: [liczba]
> - Opłata: [kwota] za spotkanie
> - Zapisy: formularz poniżej lub telefon 07340 634326
>
> Opłaty za udział w grupach w całości wspierają działalność statutową Yellow Scarf CIO (organizacja charytatywna zarejestrowana w Anglii i Walii, nr 1190615). Jeśli opłata jest dla Ciebie przeszkodą, napisz do nas. Poszukamy rozwiązania.

Zdanie o przeznaczeniu opłat jest wymogiem programu Ad Grants dla organizacji prowadzących działalność odpłatną.

## 5. Strona „Our projects”

Opis Gambling Support skrócić do dwóch zdań z linkiem do nowej podstrony i oddzielić nagłówkiem od opisu Yellow CAT, tak aby treści o hazardzie i o substancjach nie znajdowały się w jednym bloku.

## Do uzupełnienia przez Rafała przed wysłaniem

1. Miejsca, dni i godziny grup w Worcester i Evesham.
2. Koszt udziału w grupach o hazardzie oraz źródło finansowania projektu.
3. Termin, opłata i forma najbliższej grupy po polsku.
4. Godziny pracy infolinii 07340 634326.
5. Czas odpowiedzi na zgłoszenie (proponuję 2 dni robocze).
