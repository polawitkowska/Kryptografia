"""
Autorem tego zadania jest Pola Witkowska
"""

import hashlib
import os

def count_diff_bits(hex1, hex2):
    val1 = int(hex1, 16)
    val2 = int(hex2, 16)
    diff = val1 ^ val2
    return bin(diff).count('1')

def create_personal_files():
    name = "Jan Kowalski"
    
    # 1. personal.txt - tylko imię i nazwisko
    with open("personal.txt", "w", encoding="utf-8") as f:
        f.write(name + "\n")
        
    # 2. personal_.txt - to samo + dodatkowa pusta linia
    with open("personal_.txt", "w", encoding="utf-8") as f:
        f.write(name + "\n\n")

def run_task():
    pdf_filename = "hash-.pdf"
    
    # Sprawdzenie czy plik PDF istnieje (jest wymagany do drugiej części zadania)
    if not os.path.exists(pdf_filename):
        print(f"Błąd: Nie znaleziono pliku {pdf_filename}. Upewnij się, że jest w katalogu.")
        return

    create_personal_files()

    # Lista algorytmów (nazwa_hashlib, nazwa_bash, bity)
    # Kolejność jest już od najkrótszego (MD5) do najdłuższego (Blake2/SHA512)
    algos = [
        ('md5', 'md5sum', 128),
        ('sha1', 'sha1sum', 160),
        ('sha224', 'sha224sum', 224),
        ('sha256', 'sha256sum', 256),
        ('sha384', 'sha384sum', 384),
        ('sha512', 'sha512sum', 512),
        ('blake2b', 'b2sum', 512) 
    ]

    # --- CZĘŚĆ 1: Generowanie pliku hash.txt (tylko personal.txt) ---
    print("Generowanie pliku hash.txt...")
    
    with open("personal.txt", "rb") as f:
        personal_bytes = f.read()

    with open("hash.txt", "w", encoding="utf-8") as out_hash:
        for hash_name, cmd_name, _ in algos:
            h = hashlib.new(hash_name)
            h.update(personal_bytes)
            out_hash.write(f"{h.hexdigest()}\n")
    
    print("Zapisano wyniki do hash.txt.")

    # --- CZĘŚĆ 2: Generowanie pliku diff.txt (PDF + personal) ---
    print("Generowanie pliku diff.txt (analiza bitowa)...")
    
    with open(pdf_filename, "rb") as f:
        pdf_bytes = f.read()
        
    with open("personal_.txt", "rb") as f:
        personal_mod_bytes = f.read()

    diff_results = []

    for hash_name, cmd_name, bit_len in algos:
        # Oblicz dla: PDF + personal.txt
        h1 = hashlib.new(hash_name)
        h1.update(pdf_bytes + personal_bytes)
        d1 = h1.hexdigest()

        # Oblicz dla: PDF + personal_.txt
        h2 = hashlib.new(hash_name)
        h2.update(pdf_bytes + personal_mod_bytes)
        d2 = h2.hexdigest()

        # Porównaj bity
        diff_bits = count_diff_bits(d1, d2)
        percentage = int((diff_bits / bit_len) * 100)

        # Formatowanie raportu diff.txt
        entry = []
        entry.append(f"cat {pdf_filename} personal.txt | {cmd_name}")
        entry.append(f"cat {pdf_filename} personal_.txt | {cmd_name}")
        entry.append(d1)
        entry.append(d2)
        entry.append(f"Liczba różniących się bitów: {diff_bits} z {bit_len}, procentowo: {percentage}%.")
        
        diff_results.append("\n".join(entry))

    # Zapis raportu różnic
    with open("diff.txt", "w", encoding="utf-8") as f:
        f.write("\n\n".join(diff_results))
        
    print("Zapisano wyniki do diff.txt.")
    print("Zadanie zakończone sukcesem.")

if __name__ == "__main__":
    run_task()