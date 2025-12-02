import hashlib
import os
import binascii

def count_diff_bits(hex1, hex2):
    # Konwersja hex -> int
    val1 = int(hex1, 16)
    val2 = int(hex2, 16)
    # XOR znajduje różnice (ustawione bity tam, gdzie wartości są różne)
    diff = val1 ^ val2
    # Zliczenie ustawionych bitów
    return bin(diff).count('1')

def create_personal_files():
    name = "Jan Kowalski"
    
    # personal.txt - imię i nazwisko + nowa linia (standard w edytorach)
    with open("personal.txt", "w", encoding="utf-8") as f:
        f.write(name + "\n")
        
    # personal_.txt - to samo + dodatkowa pusta linia
    with open("personal_.txt", "w", encoding="utf-8") as f:
        f.write(name + "\n\n")

def run_diff_tool():
    pdf_filename = "hash-.pdf"
    output_filename = "diff.txt"

    # Sprawdzenie czy plik PDF istnieje
    if not os.path.exists(pdf_filename):
        print(f"Błąd: Nie znaleziono pliku {pdf_filename}. Upewnij się, że jest w tym samym katalogu.")
        return

    # Tworzenie plików z danymi osobowymi
    create_personal_files()

    # Wczytanie zawartości PDF (binarnie)
    with open(pdf_filename, "rb") as f:
        pdf_bytes = f.read()

    # Lista algorytmów do sprawdzenia
    # (nazwa w hashlib, nazwa w poleceniu cat, długość w bitach)
    algos = [
        ('md5', 'md5sum', 128),
        ('sha1', 'sha1sum', 160),
        ('sha224', 'sha224sum', 224),
        ('sha256', 'sha256sum', 256),
        ('sha384', 'sha384sum', 384),
        ('sha512', 'sha512sum', 512),
        ('blake2b', 'b2sum', 512) # blake2b w hashlib domyślnie ma 64 bajty (512 bitów), jak b2sum
    ]

    results = []

    for hash_name, cmd_name, bit_len in algos:
        # Obliczenie skrótu dla personal.txt
        with open("personal.txt", "rb") as f:
            p1_bytes = f.read()
        
        h1 = hashlib.new(hash_name)
        h1.update(pdf_bytes + p1_bytes)
        d1 = h1.hexdigest()

        # Obliczenie skrótu dla personal_.txt
        with open("personal_.txt", "rb") as f:
            p2_bytes = f.read()
        
        h2 = hashlib.new(hash_name)
        h2.update(pdf_bytes + p2_bytes)
        d2 = h2.hexdigest()

        # Porównanie
        diff_bits = count_diff_bits(d1, d2)
        percentage = int((diff_bits / bit_len) * 100)

        # Formatowanie wyniku zgodnie z wzorem z diff.txt
        entry = []
        entry.append(f"cat {pdf_filename} personal.txt | {cmd_name}")
        entry.append(f"cat {pdf_filename} personal_.txt | {cmd_name}")
        entry.append(d1)
        entry.append(d2)
        entry.append(f"Liczba różniących się bitów: {diff_bits} z {bit_len}, procentowo: {percentage}%.")
        
        results.append("\n".join(entry))

    # Zapis do pliku diff.txt
    final_output = "\n\n".join(results)
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(final_output)
    
    print(f"Wygenerowano plik {output_filename}")
    print(final_output)

if __name__ == "__main__":
    run_diff_tool()