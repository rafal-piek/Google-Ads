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

- **Instalacja zależności:** _(np. `pip install -r requirements.txt` lub `npm install`)_
- **Uruchomienie:** _(do uzupełnienia)_
- **Testy:** _(do uzupełnienia)_
- **Lint / formatowanie:** _(do uzupełnienia)_

## Konwencje i decyzje

> Zapisuj tu ważne ustalenia, żeby nie powtarzać ich w każdej sesji
> (struktura katalogów, styl kodu, sposób obsługi sekretów/credentials itp.).

- _(brak — do uzupełnienia)_

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
