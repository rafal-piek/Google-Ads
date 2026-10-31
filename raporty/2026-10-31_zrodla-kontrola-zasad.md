# Kontrola zasad i źródeł — audyt kontrolny 3 kont, 2026-10-31 (odczyt 08:30–08:50 UTC)

## Oficjalne Google
- Limited ad serving — update sierpień 2026 (support.google.com/adspolicy/answer/17344822, wpis 5.08.2026): polityka rozszerzona na wszystkie produkty Ads, wdrożenie stopniowe do 2028; na Search od 12.06.2026. Kryteria „qualified advertiser”: atrybuty konta, zgłoszenia użytkowników, dojrzałość konta, formaty, historia zgodności, branża, weryfikacja. Zalecenia Search: marka w reklamie i na LP, konkretny tekst, przypięcie domeny/marki na pozycji 1 nagłówka (zwłaszcza nowe marki). Bez odrzuceń pojedynczych reklam; powiadomienie w koncie; apelacja formularzem.
- AI Max for Search (support.google.com/google-ads/answer/15909989): domyślnie WŁ. w nowych kampaniach Search; w istniejących opt-in. Komponenty: search term matching (kampania/grupa), text customization, final URL expansion (zależne od text customization), URL inclusions/exclusions, brand inclusions/exclusions. Wyłączenie całości: Campaigns → Settings → AI Max → opt out.
- Auto-upgrade do AI Max od 1.09.2026 (Search Engine Land 484428; ppc.land 6.08.2026; ppcnewsfeed 10.08.2026): kampanie Search z Automatically Created Assets (ACA) i/lub z ustawieniem broad match na poziomie kampanii zostały automatycznie przełączone na AI Max (ACA → search term matching + text customization; broad match setting → search term matching). Konta bez tych ustawień: bez zmian. DSA → AI Max przesunięte na luty 2027. DO SPRAWDZENIA na 733 i 311: czy któraś kampania miała ACA lub campaign-level broad match i dostała search term matching po 1.09.
- Addiction services (support.google.com/adspolicy/answer/15598649): nadal tylko AU, CA, FR, IE, NZ, US. UK NIE. Bez zmian wobec 24.10.
- Healthcare & medicines: ostatnie zmiany X.2025 (terminy leków w kontekście niepromocyjnym) i III.2025; nic nowego dla psychoterapii w UK. Personalised advertising: update I.2026 (answer 16828044) — bez zmian dla zdrowia psychicznego (zakaz targetowania po stanie zdrowia utrzymany).
- Child Safety policy (ogłoszona 22.10.2026, egzekwowanie od 11.01.2027): zastępuje CSAE jako osobna polityka; dla naszych kont bez znaczenia, o ile reklamy/LP nie zawierają wizerunków dzieci w niewłaściwym kontekście (DZIECIĘCY na 733: sprawdzić grafiki PMax pod kątem zwykłej przyzwoitości — ryzyko minimalne).
- Ad Grants account management (support.google.com/grants/answer/117827, en-GB): bez zmian — CTR 5%/mies. na poziomie konta (2 mies. z rzędu = deaktywacja), ≥1 konwersja/mies. dla kont od 22.04.2019, conversion-based Smart Bidding obowiązkowy (Max Conv / Max Conv Value / tCPA / tROAS; niezgodne kampanie mogą być przestawione automatycznie; po deaktywacji wolno zacząć od Max clicks do 15–30 konw./30 dni), geotargeting tylko tam, gdzie usługi, ≥2 sitelinki, ankieta programowa obowiązkowa, e-mail powiadomień opt-in. Automatyczne zawieszenie bez powiadomienia.

## Branżowe (≤12 mies.)
1. ppc.land 7.08.2026 — Limited ad serving: brak progów liczbowych, brak terminów reaktywacji; pinowanie domeny ogranicza kombinacje RSA.
2. Search Engine Roundtable 15.06.2026 — Limited ad serving na Search: generyczne reklamy bez marki i reklamy z cudzymi markami = ryzyko ograniczenia emisji dla całego konta.
3. Connective Web Design (2026) — egzekwowanie: 17.03.2026 wycofanie starych polityk formatów; 31.03.2026 reorganizacja Help Center (bez zmiany egzekwowania); obserwacje: „Enhanced Review” 24–72 h, retroaktywne odrzucenia, absolutne sformułowania („100%”, „guaranteed”) jako clickbait; reklamy w WSTRZYMANYCH kampaniach nadal zbierają naruszenia (final URL) → sprawdzić Policy Manager i wstrzymane kampanie (311 „Google AI Test”, 733 WR).
4. Accelerated Digital Media 27.08.2026 — zasady zdrowia 2026: LegitScript tylko apteki/telemedycyna/uzależnienia; dla terapii/counsellingu brak certyfikacji; zakaz targetowania po stanie zdrowia i treści o traumie/przemocy jako „negatywnych”; nic nowego dla mental health w 2026.
5. Levitate 1.04.2026 — Ad Grants 2026: wymogi bez zmian (login co miesiąc, CTR 5%, brak jednowyrazowych, konwersje, geo).
6. Third Sector Lab / Manchester Community Central (webinar 2.07.2026) — „grant zmienił się mocno w ostatnim roku, nowe funkcje” (PMax, Maps, shop visits) — potwierdza wiedzę z 24.10.
7. Web Tonic 26.09.2026 (upd. 9.10.2026) za LocaliQ 2026 — mental health US: CPL $141,17 (najwyższy z 16 podkategorii), CVR 1,85%, CPC $4,22 (+42% r/r), CTR 4,46%; healthcare avg CPL $66, CVR 8,09%.
8. Visionary Marketing UK (6.05.2026, upd. 29.05.2026; dane 1.03.2025–28.02.2026, 16 kont healthcare, 14 charity): Healthcare CPC £6,94, CTR 6,18%, CVR 7,18%, koszt/konw. £96,74; Charity CPC £1,96, CTR 8,18%, CVR 7,42%, koszt/konw. £26,42.
9. Weir Digital Media UK 2026 (I.2025–IV.2026, SME £1–25k/mies.): Healthcare & dental Google Ads CPC £4,20, CTR 4,2%, CVR 5,8%, CPL £72.
10. Audit Socials 22.10.2026 — Child Safety policy od 11.01.2027.
11. Cause Inspired Media — historia zmian Ad Grants (2018): QS<3 pauza, single-word, misja, ankieta — nadal obowiązuje.
12. (z 24.10, nadal aktualne) Medico Digital UK 2025: mental health CPC £1,02, CTR 6,28%, CVR 4,69%, CPA £21,74; Ridley UK 2026 healthcare CPL £51,80; Seer AIO CTR; Yext/SOCi GEO; BACP 2026; ASA Gary Baron 12.08.2026.

## Wnioski dla audytu kontrolnego
- Nowe od 24.10: nic, co zmienia zasady dla naszych kont. Potwierdzone: UK bez Addiction services; AI Max domyślnie w nowych kampaniach; auto-upgrade od 1.09 dotyczy tylko ACA/broad-match-setting — sprawdzić obie komercyjne kampanie.
- Limited ad serving: dla 311 (nowa marka, generyczne hasła) realne ryzyko — pinowanie „Yellow Scarf Therapy” / domeny na H1 i marka na LP; 733 ma dojrzałe konto.
- Benchmark UK koszt/lead: £22 (Medico mental health) … £52–72 (Ridley/Weir healthcare) … £97 (Visionary healthcare). Nasze progi Rafała: 733 £32–63, 311 £31–78.
- Policy Manager i wstrzymane kampanie: sprawdzić, czy reklamy w pauzach nie mają naruszeń final URL.
