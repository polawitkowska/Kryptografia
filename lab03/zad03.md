# Uwagi do rozwiązania:

Program należy uruchomić wpisując w terminal:

```bash
python block.py
```

- Program potrzebuje pliku `plain.bpm` aby działać.

# Treść zadania

Na wykładzie (slajdy 7–14) przedstawiono kilka trybów szyfrów blokowych, z czego nas będzie interesować w tej chwili:

- tryb ECB (książki kodowej)
- tryb CBC (dodawania zaszyfrowanego bloku do szyfrowania kolejnego bloku)

Pierwszy tryb jest zbyt prosty, by być odporny na wielokrotne szyfrowanie czy na atak z tekstem jawnym. Celem tego ćwiczenia będzie unaocznienie tej prostoty w sposób wizualny.

---

## Opis zadania

W zadaniu należy zaprojektować „szyfrowanie” obrazu graficznego. Obraz powinien być czarno-biały i mieć rozmiar rzędu kilkuset pikseli w pionie i w poziomie. Obraz taki należy podzielić na małe bloki, np. 8×8 pikseli – w ten sposób każdy blok grafiki zostaje potraktowany jako blok szyfru blokowego. Cały obraz należy potraktować jako ciąg małych bloków, np. przeglądanych kolejnymi wierszami.

W naszym przypadku nie dysponujemy własną implementacją szyfru blokowego, w celu wykonania zadania można przyjąć dowolne przekształcenie, bez konieczności „odszyfrowywania” kryptogramu – jest istotne, by takie same bloki były identycznie szyfrowane. Np. można zastosować jakąkolwiek funkcję skrótu, `md5sum` czy `sha1sum`.

> **Uwaga:** celem zadania jest zrozumienie działania trybów blokowych, a nie tylko ich nazw. W związku z tym w rozwiązaniu nie można stosować gotowych bibliotek wywołujących szyfrowanie w jakimkolwiek trybie szyfru blokowego.

---

## Wymagania

Program powinien:

- wczytać plik graficzny
- wyprodukować dwa pliki graficzne:
  - kryptogram zaszyfrowany w trybie **ECB**
  - kryptogram zaszyfrowany w trybie **CBC**

Należy pamiętać, że obrazek powinien być maksymalnie nieskomplikowany, np. jakiś znak firmowy albo powiększona do dużych rozmiarów czcionka.

Przykłady: obrazek jest przekształcany w trybie ECB oraz CBC i drugi obrazek, ECB i CBC.

---

## Szczegóły techniczne

- Program `block` powinien czytać pliki:
  - graficzny `plain.bmp`
  - opcjonalnie tekstowy `key.txt` z kluczem
- Powinien zapisywać dwa pliki graficzne:
  - `ecb_crypto.bmp`
  - `cbc_crypto.bmp`

W rozwiązaniu należy przesłać:

- program w wersji źródłowej i skompilowanej
- testowy plik graficzny
- ewentualnie plik z kluczem

> **Uwaga:**  
>  W programie nie wolno stosować wbudowanych bibliotek kryptograficznych z wywołaniem funkcji szyfrowania w wybranym trybie blokowym – należy te tryby zaimplementować własnoręcznie.
