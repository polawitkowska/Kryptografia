# Uwagi do rozwiązania

W zadaniu jest napisane, aby program przetestować dla:

```
6887096822657901972664669
65537
645340213740199857867233
```

I wynikiem powinna być jedna z tych liczb:

```
941629821541
7314017318809
```

Ponieważ iloczyn tych liczb to `6887096822657901972664669`.

Ja przetestowałam również dla liczb `104729` (liczba pierwsza) i `104731` (liczba złożona). Dla `104729` wynik był poprawny - "liczba prawdopodobnie pierwsza". Dla `104731` wynik był "liczba na pewno złożona". Aby uzyskać dzielnik `104731` (czyli 11 lub 9521) wejście powinno zawierać w drugiej linijce `95200`.

---

Program należy uruchomić komendą:

```bash
bash ./rabinmiller.sh
```

Lub, drugi wariant:

```bash
bash ./rabinmiller.sh -f
```

Program potrzebuje pliku `wejscie.txt`, aby działać. Program generuje plik `wyjscie.txt`.

Za zadanie otrzymałam **/100 pkt**.

---

# Treść zadania

Program o nazwie rabinmiller czyta plik `wejscie.txt` zawierający jeden, dwa lub trzy wiersze. W pierwszym wierszu znajduje się liczba `n`. Jeśli jest drugi wiersz, to zawiera on wykładnik uniwersalny, ułatwiający rozkład. Jeśli jest trzeci wiersz, to wykładnikiem uniwersalnym jest iloczyn liczb w drugim i trzecim wierszu minus jeden.

Program zapisuje w pliku `wyjscie.txt` jedną z trzech wiadomości: „prawdopodobnie pierwsza”, „na pewno złożona”, lub liczbę będącą dzielnikiem liczby `n`. Zapis „prawdopodobnie pierwsza” ma prawo się pojawić, jeśli prawdopodobieństwo, że liczba jest złożona jest mniejsza niż `2^(−40)`.

Program rabinmiller wywołany z opcją `-f` będzie dokonywać jedynie testu Fermata, tzn. będzie badać jedynie ostatnią potęgę potencjalnego świadka pierwszości. W szczególności, program nie będzie czytał dalszych wierszy w pliku wejściowym i nie będzie okazji do znalezienia rozkładu.

Testowy plik wejściowy wejscie.txt będzie zawierał liczby

```math
6887096822657901972664669\newline
65537\newline
645340213740199857867233
```

program powinien wyprodukować jeden z dwóch poniższych wyników

```math
941629821541\newline
7314017318809
```

(ich iloczyn jest równy `6887096822657901972664669`, podczas działania programu okaże się, że `2928660113703641594368843` jest pierwiastkiem z `1 mod 6887096822657901972664669`).
Program wywołany z opcją `-f` **nie** odkryje, że `561` (liczba Carmichaela) jest liczbą złożoną, a wywołany w pełnej wersji odkryje, że `561=33\*17`.

```
Uwaga: stosowanie bibliotek do obsługi dużych liczb może być konieczne.
Stosowanie bibliotek z wbudowanym testem Rabina-Millera oczywiście mija się z celem tego zadania.
```
