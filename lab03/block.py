""" 
Autorem tego zadania jest Pola Witkowska
"""

import os
import hashlib
from PIL import Image

BLOCK_SIZE = 16

def get_key(filename='key.txt'):
    # Wczytuje klucz z pliku lub używa domyślnego.

    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return f.read().strip()
    return b'SecretKey123'  # Domyślny klucz

def xor_bytes(b1, b2):
    # Pomocnicza funkcja do operacji XOR na dwóch blokach bajtów.
    return bytes(x ^ y for x, y in zip(b1, b2))

def pseudo_encrypt_block(key, data_block):
    """
    Symuluje funkcję szyfrującą F(k, m).
    Zamiast prawdziwego algorytmu blokowego (jak AES), używamy MD5
    zgodnie z pozwoleniem w treści zadania.
    Zwraca zawsze 16 bajtów.
    """
    h = hashlib.md5()
    h.update(key)
    h.update(data_block)
    return h.digest()

def pad_data(data):
    #Dopełnia dane, aby ich długość była wielokrotnością BLOCK_SIZE (PKCS#7).
    padding_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    padding = bytes([padding_len] * padding_len)
    return data + padding

def run_ecb(image_data, key):
    """
    Implementacja trybu ECB (Electronic Code Book).
    Każdy blok szyfrowany jest niezależnie: c_j = Enc(k, m_j).
    """
    encrypted_data = bytearray()
    
    # Przetwarzanie blok po bloku
    for i in range(0, len(image_data), BLOCK_SIZE):
        # Pobranie bloku tekstu jawnego (m_j)
        block = image_data[i : i + BLOCK_SIZE]
        
        # Jeśli to ostatni, niepełny blok - dopełniamy go (padding)
        if len(block) < BLOCK_SIZE:
            block = pad_data(block)
            
        # Szyfrowanie bloku: c_j = Enc(k, m_j)
        enc_block = pseudo_encrypt_block(key, block)
        
        encrypted_data.extend(enc_block)
        
    # Przycinamy wynik do długości oryginału, aby zachować wymiary obrazka
    # (W prawdziwej kryptografii byśmy to zostawili, ale tutaj musimy wyrenderować BMP)
    return bytes(encrypted_data[:len(image_data)])

def run_cbc(image_data, key):
    """
    Implementacja trybu CBC (Cipher Block Chaining).
    c_j = Enc(k, m_j XOR c_{j-1})
    """
    encrypted_data = bytearray()
    
    # Wektor inicjujący IV (dla uproszczenia same zera lub hash klucza)
    iv = hashlib.md5(b'initial_vector').digest()
    prev_cipher_block = iv
    
    for i in range(0, len(image_data), BLOCK_SIZE):
        block = image_data[i : i + BLOCK_SIZE]
        
        if len(block) < BLOCK_SIZE:
            block = pad_data(block)
            
        # Krok 1: XOR z poprzednim szyfrogramem (m_j XOR c_{j-1})
        xor_input = xor_bytes(block, prev_cipher_block)
        
        # Krok 2: Szyfrowanie wyniku (Enc(...))
        enc_block = pseudo_encrypt_block(key, xor_input)
        
        encrypted_data.extend(enc_block)
        
        # Aktualizacja poprzedniego bloku dla następnej iteracji
        prev_cipher_block = enc_block

    return bytes(encrypted_data[:len(image_data)])

def main():
    input_filename = 'plain.bmp'
    
    if not os.path.exists(input_filename):
        print(f"Błąd: Nie znaleziono pliku {input_filename}")
        return

    # 1. Wczytanie obrazu
    try:
        img = Image.open(input_filename)
        # Konwersja do bajtów (raw pixel data)
        img_bytes = img.tobytes()
    except Exception as e:
        print(f"Błąd przy otwieraniu obrazu: {e}")
        return

    key = get_key()
    print(f"Używany klucz: {key}")
    print(f"Rozmiar danych obrazu: {len(img_bytes)} bajtów")

    # 2. Szyfrowanie ECB
    print("Przetwarzanie w trybie ECB...")
    ecb_bytes = run_ecb(img_bytes, key)
    
    # Tworzenie obrazu z bajtów zaszyfrowanych (z zachowaniem trybu i rozmiaru oryginału)
    ecb_img = Image.frombytes(img.mode, img.size, ecb_bytes)
    ecb_img.save('ecb_crypto.bmp')
    print("Zapisano ecb_crypto.bmp")

    # 3. Szyfrowanie CBC
    print("Przetwarzanie w trybie CBC...")
    cbc_bytes = run_cbc(img_bytes, key)
    
    cbc_img = Image.frombytes(img.mode, img.size, cbc_bytes)
    cbc_img.save('cbc_crypto.bmp')
    print("Zapisano cbc_crypto.bmp")

if __name__ == "__main__":
    main()