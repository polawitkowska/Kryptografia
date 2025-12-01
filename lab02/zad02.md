# Uwagi do tego rozwiązania

Program należy uruchomić wpisując w terminal:

```bash
python xor.py [-p | -e | -k]
```

- Aby program działał w pełni poprawnie, trzeba mu dać długi tekst w `orig.txt`.
- Klucz w `key.txt` nie może być powtarzalny (np. "aaaaaaaa" albo "abcabcabcabcabc").

Za zadanie otrzymałam **100/100 pkt**.

---

# Treść zadania

Zasadą szyfru jednorazowego jest niepowtarzalność klucza.  
**E(k, m) = k ⊕ m**  
**D(k, c) = k ⊕ c**

Jeśli dwie wiadomości są zaszyfrowane tym samym kluczem **k**, to można obliczyć:  
**m₁ ⊕ m₂ = c₁ ⊕ c₂**.

Znajomość xor dwu wiadomości niesie już pewne informacje, a każda uzyskana informacja jest z definicji złamaniem szyfru, nawet jeśli nie prowadzi do całkowitego odszyfrowania tekstu.

W zadaniu pokazującym możliwości uzyskania informacji ze znajomości xor założymy, że szyfrowane są wyłącznie litery i spacje (kilka innych znaków można by dopuścić, ale na pewno nie cyfry, nie znaki przestankowe). Założymy też, że cały tekst (angielski) jest kodowany standardowo kodem ASCII, tzn. spacja ma numer 32, a pozostałe znaki 64–126.

W notacji heksagonalnej spacja to `0x20`, a litery `0x40`–`0x7E`. Sposób xor dwóch liter zaczyna się od dwóch zer, a xor litery i spacji ma na początku `01`. Wiedząc, że m₁ ⊕ m₂ ma pierwsze dwa bity `01`, wiemy, że jeden ze znaków jest spacją, więc `m₁ ⊕ m₂ ⊕ 0x20` jest drugim ze znaków, nie wiadomo tylko którym.

Jeśli mamy do dyspozycji m₁ ⊕ m₂ i m₁ ⊕ m₃ i np. pierwsza para ma spację, a druga nie ma, to wiadomo, że spacją jest m₂ i wyliczamy m₁ i m₃. Jeśli obie mają spacje, to prawdopodobnie jest to m₁ i wyliczamy pozostałe znaki. Spacją mogłyby być znaki m₂ i m₃, a nie m₁, ale jest to łatwo wykrywalne, bo m₂ ⊕ m₃ = 0x00.

Jeśli znamy więcej przykładów kryptogramów powstałych z użyciem tego samego klucza, to jest duża szansa na odtworzenie dokładnych tekstów.

---

## Program o nazwie `xor` powinien umożliwiać wywołanie z linii poleceń z następującymi opcjami:

- `-p` – przygotowanie tekstu do przykładu działania
- `-e` – szyfrowanie
- `-k` – kryptoanaliza wyłącznie w oparciu o kryptogram

## Nazwy plików

- `orig.txt` – plik zawierający dowolny tekst (czytelny, może być bez polskich liter)
- `plain.txt` – plik z tekstem zawierającym co najmniej kilkanaście linijek równej długości, np. 64
- `key.txt` – plik zawierający klucz, który jest ciągiem dowolnych znaków podanej wyżej długości (warto założyć, że jest czytelny)
- `crypto.txt` – plik z tekstem zaszyfrowanym; każda linijka to operacja ⊕ z kluczem (nie należy się spodziewać możliwości wyświetlenia tego tekstu)
- `decrypt.txt` – plik z tekstem odszyfrowanym; jeśli litery tekstu jawnego nie można odszyfrować, należy wstawić znak podkreślenia `_`

---

Oceniane będą wyłącznie programy zawierające kryptoanalizę.
