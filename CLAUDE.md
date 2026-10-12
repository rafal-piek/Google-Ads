# CLAUDE.md

Ten plik jest czytany przez Claude Code na **początku każdej sesji**. Służy jako
trwały kontekst projektu — to, co tu zapiszesz, będę „wiedział" w każdej kolejnej
rozmowie, nawet jeśli nie pamiętam poprzednich sesji. Aktualizuj go w miarę
rozwoju projektu.

> Status: repozytorium dopiero powstaje. Technologia i zakres nie są jeszcze
> ustalone. Sekcje poniżej są szkieletem do uzupełnienia.

## Język komunikacji

- Rozmawiaj ze mną (właścicielem repo) **po polsku**.
- Kod, nazwy zmiennych i komentarze techniczne — zgodnie z konwencją wybranego
  języka (zwykle po angielsku), chyba że ustalimy inaczej.

## O projekcie

- **Nazwa:** Google-Ads
- **Cel:** _(do ustalenia)_ — projekt związany z Google Ads: potencjalnie
  automatyzacja kampanii, integracja z Google Ads API, raportowanie/analiza
  danych lub skrypty. Doprecyzujemy, gdy kierunek się wyklaruje.
- **Stack:** _(jeszcze nie wybrany)_

## Jak pracować w tym repo

> Uzupełnij, gdy pojawią się pierwsze pliki. Przykładowe miejsca na komendy:

- **Instalacja zależności:** `pip install -r requirements-dev.txt`
- **Uruchomienie:** `gads_audit.audit.run_audit("osrodek" | "fundacja" | "mental", ads, snapshot)`
  (CLI i pobieranie danych z API — do zrobienia)
- **Testy:** `python3 -m pytest`
- **Lint / formatowanie:** _(do uzupełnienia)_

## Konwencje i decyzje

> Zapisuj tu ważne ustalenia, żeby nie powtarzać ich w każdej sesji
> (struktura katalogów, styl kodu, sposób obsługi sekretów/credentials itp.).

- Kod w `src/gads_audit/`. Trzy profile kont w `accounts.py` (Osrodek, Fundacja,
  Mental) — każdy audyt działa na jednym profilu; dane z innego customer ID
  przerywają audyt, a URL z cudzej domeny to błąd „pomieszanie kont”.
- Reguły Ad Grants (`checks/ad_grants.py`) działają tylko dla Fundacji. Daty
  i źródła weryfikacji są w docstringu — sprawdzaj zasady ponownie przy każdej
  pracy nad kontem i aktualizuj datę.
- Słowniki CTA i zakazanych sformułowań dla usług terapeutycznych (PL i en-GB)
  w `therapy_vocab.py`; słowniki e-commerce celowo usunięte.
- W repo tylko identyfikatory kont (customer ID, domena), bez e-maili logowania.

## Bezpieczeństwo / dane wrażliwe

- **Nigdy nie commituj** kluczy API, tokenów OAuth ani plików z poświadczeniami
  Google Ads (np. `google-ads.yaml`, `client_secret*.json`, `.env`).
- Trzymaj sekrety poza repo (zmienne środowiskowe / menedżer sekretów) i dodaj je
  do `.gitignore`.

## Środowisko zdalne (Claude Code on the web)

- Sesje mogą działać w **tymczasowym kontenerze w chmurze** — repo jest klonowane
  na świeżo, a kontener bywa usuwany po okresie nieaktywności.
- Dlatego **każdą zmianę wartą zachowania trzeba zacommitować i wypchnąć**
  (`git push`), inaczej przepadnie.
- Nie tworzę pull requestów bez wyraźnej prośby.
