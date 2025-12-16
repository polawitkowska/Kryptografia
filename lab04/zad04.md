# Uwagi do rozwiązania

### Zadanie 1:

Program należy uruchomić komendą:

```bash
bash ./skrypt.sh
```

Program potrzebuje pliku `personal.txt`, aby działać.

Za zadanie otrzymałam **20/20 pkt**.

---

### Zadanie 2:

Program należy uruchomić komendą:

```bash
python diff.py
```

Program potrzebuje plików `hash-.pdf` oraz `personal.txt`, aby działać.

---

# Treść zadań

Dwie najpopularniejsze i najczęściej używane funkcje skrótu to **md5** oraz **sha-1**. Na wielu systemach są one dostępne bez dodatkowych instalacji, na komputerze sigma polecenia brzmią `md5sum` oraz `sha1sum`. Pierwsza z tych funkcji zwraca skrót 128-bitowy, druga 160-bitowy. Standard SHA udostępnia wiele dalszych funkcji: `sha224sum`, `sha256sum`, `sha384sum`, `sha512sum`, dających coraz dłuższe skróty. Inna funkcja skrótu to `b2sum`. Skróty zapisywane są w systemie szesnastkowym (bez dodatkowych wyjaśnień, że chodzi o ten system zapisu).

Argumentem funkcji jest nazwa pliku, można używać wyrażeń regularnych. Np.:

```bash
[amb@sigma ~]$ md5sum bookmarks.*
cbeb720b717f7e25791f6c4ed5523d7d bookmarks.html
2cc3f5956f0a6ec662b0f15452d435ec bookmarks.zip
```

Podobnie dla funkcji SHA. Komunikat ten można zapisać do pliku, np. poprzez przekierunkowanie. Pozwala to w przyszłości sprawdzić, czy zaszła zmiana:

```bash
[amb@sigma ~]$ md5sum -c plik
bookmarks.html: NIEPOWODZENIE
bookmarks.zip: DOBRZE
md5sum: UWAGA: 1 z 2 wyliczonych sum kontrolnych się NIE zgadza
```

Funkcje skrótu mogą również czytać dane wejściowe ze standardowego wejścia, np.:

```bash
[andrzej@sigma]$ cat hash-.pdf | sha1sum
2af2bbc4c91bcc13dafbea711f9ffa1afa1bb1d0 -
[andrzej@sigma]$ sha1sum hash-.pdf
2af2bbc4c91bcc13dafbea711f9ffa1afa1bb1d0 hash-.pdf
```

---

## Zadania

1. Przygotuj plik `personal.txt` zawierający imię i nazwisko. Oblicz wszystkie funkcje skrótu na tym pliku, wyniki zapisz do pliku `hash.txt` w kolejności coraz dłuższych skrótów.

2. Przygotuj drugą wersję pliku `personal_.txt`, różniącą się jedynie dodatkowym pustym wierszem na końcu. Oblicz wartość wszystkich funkcji skrótu dla obu wersji pliku połączonego z tym samym plikiem wykładu `hash-.pdf` (tzn. wykonaj polecenia:)

   ```bash
   cat hash-.pdf personal.txt | md5sum >> hash.txt
   cat hash-.pdf personal_.txt | md5sum >> hash.txt
   # itd. dla obu wersji pliku z danymi osobowymi
   ```

   Następnie sprawdź liczbę bitów (nie bajtów) różnych w obu wynikach. Należy się spodziewać, że w każdej parze ok. połowa bitów będzie różna.

3. Jako rozwiązanie prześlij oba pliki `personal.txt` oraz plik `diff.txt` zawierający pary wyników dla każdej z funkcji skrótu i liczbę bitów różniących te wyniki.

4. Prześlij też program o nazwie `diff` liczący różniące się bity. Program może odczytywać plik `hash.txt` zawierający pary skrótów i wytworzony za pomocą powyższych poleceń. Może też działać niezależnie, tzn. zapisywać i plik `hash.txt` i `diff.txt`.

---

Przykładowy plik z wynikami: `diff.txt`.
