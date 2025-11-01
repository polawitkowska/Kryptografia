""" Autorem tego zadania jest Pola Witkowska """

import sys

alfabet = list("abcdefghijklmnopqrstuvwxyz")

# odczytywanie pliku
def read_file(file):
    try:
        with open(file, "r") as f:
            return f.read().lower()
    except FileNotFoundError:
        print("Nie znaleziono pliku", file)
        sys.exit(1)

# zapisywanie tekstu do pliku
def write_file(text, file):
    try:
        with open(file, "w") as f:
            f.write(text)
    except OSError as e:
        print(f"Wystąpił błąd podczas zapisywania tekstu do pliku: {e}")
        sys.exit(1)

# region funkcje cezara
def eCezar(k, x):
    text = []
    for char in x:
        if char in alfabet:
            text.append(alfabet[(alfabet.index(char) + int(k)) % 26])
        else:
            text.append(char)
    write_file("".join(text), "crypto.txt")


def dCezar(k, y):
    text = []
    for char in y:
        if char in alfabet:
            text.append(alfabet[(alfabet.index(char) - int(k)) % 26])
        else:
            text.append(char)
    write_file("".join(text), "decrypt.txt")


def jCezar():
    plain = read_file("plain.txt")
    crypto = read_file("crypto.txt")
    for p, c in zip(plain, crypto):
        if p in alfabet and c in alfabet:
            k = (alfabet.index(c) - alfabet.index(p)) % 26
            write_file(str(k), "key-found.txt")
            dCezar(k, crypto)
            return
    print("Nie udało się znaleźć klucza.")
    sys.exit(1)


def kCezar():
    crypto = read_file("crypto.txt")
    try:
        with open("extra.txt", "w") as extra:
            for k in range(1, 26):
                text = []
                for char in crypto:
                    if char in alfabet:
                        text.append(alfabet[(alfabet.index(char) - k) % 26])
                    else:
                        text.append(char)
                extra.write(f"K={k}: {''.join(text)}\n\n")
    except OSError as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")
        sys.exit(1)
# endregion

# region funkcje afiniczny
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def eAfiniczny(a, b, x):
    text = []
    for char in x:
        if char in alfabet:
            text.append(alfabet[((alfabet.index(char) * int(a)) + int(b)) % 26])
        else:
            text.append(char)
    write_file("".join(text), "crypto.txt")


def dAfiniczny(a, b, y):
    text = []
    a_inv = mod_inverse(int(a), 26)
    if a_inv is None:
        print("Brak multiplikatywnej odwrotności klucza.")
        sys.exit(1)
    for char in y:
        if char in alfabet:
            text.append(alfabet[(a_inv * (alfabet.index(char) - int(b))) % 26])
        else:
            text.append(char)
    write_file("".join(text), "decrypt.txt")


def jAfiniczny():
    plain = read_file("plain.txt")
    crypto = read_file("crypto.txt")

    for p, c in zip(plain, crypto):
        if p in alfabet and c in alfabet:
            index_p = alfabet.index(p)
            index_c = alfabet.index(c)

            for a in range(1, 26):
                if mod_inverse(a, 26) is not None:
                    b = (index_c - a * index_p) % 26
                    if all((a * alfabet.index(px) + b) % 26 == alfabet.index(cx) for px, cx in zip(plain, crypto) if
                           px in alfabet and cx in alfabet):
                        with open("key-found.txt", "w") as key_found:
                            key_found.write(f"{a} {b}")
                        dAfiniczny(a, b, crypto)
                        return

    print("Nie udało się znaleźć klucza.")
    sys.exit(1)


def kAfiniczny():
    crypto = read_file("crypto.txt")
    possible_a = [a for a in range(1, 26, 2) if mod_inverse(a, 26) is not None]
    try:
        with open("extra.txt", "w") as extra:
            for a in possible_a:
                a_inv = mod_inverse(a, 26)
                for b in range(26):
                    text = []
                    for char in crypto:
                        if char in alfabet:
                            text.append(alfabet[(a_inv * (alfabet.index(char) - b)) % 26])
                        else:
                            text.append(char)
                    extra.write(f"a={a}, b={b}: {''.join(text)}\n\n")
    except OSError as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")
        sys.exit(1)
# endregion

# szyfr cezara
if sys.argv[1] == "-c":
    if sys.argv[2] == "-e":
        print("Szyfrowanie cezara")
        eCezar(read_file("key.txt")[0], read_file("plain.txt"))
    elif sys.argv[2] == "-d":
        print("Odszyfrowywanie cezara")
        dCezar(read_file("key.txt")[0], read_file("crypto.txt"))
    elif sys.argv[2] == "-j":
        print("Kryptoanaliza Cezara z tekstem jawnym")
        jCezar()
    elif sys.argv[2] == "-k":
        print("Kryptoanaliza Cezara bez tekstu jawnego (brute force)")
        kCezar()
    sys.exit(0)

# szyfr afiniczny
elif sys.argv[1] == "-a":
    if sys.argv[2] == "-e":
        print("Szyfrowanie afiniczne")
        keys = read_file("key.txt")
        eAfiniczny(keys[0], keys[2], read_file("plain.txt"))
    elif sys.argv[2] == "-d":
        print("Odszyfrowywanie afiniczne")
        keys = read_file("key.txt")
        dAfiniczny(keys[0], keys[2], read_file("crypto.txt"))
    elif sys.argv[2] == "-j":
        print("Kryptoanaliza afiniczna z tekstem jawnym")
        jAfiniczny()
    elif sys.argv[2] == "-k":
        print("Kryptoanaliza afiniczna bez tekstu jawnego (brute force)")
        kAfiniczny()
    sys.exit(0)

else:
    sys.exit(1)
