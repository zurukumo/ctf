import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


def b16_decode(plain):
    dec = ""
    for i in range(0, len(plain), 2):
        c1 = ALPHABET.index(plain[i])
        c2 = ALPHABET.index(plain[i + 1])
        dec += chr(c1 * 16 + c2)
    return dec


enc = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"
for key in ALPHABET:
    b16 = ""
    for c in enc:
        b16 += unshift(c, key)
    flag = b16_decode(b16)

    print(f"when key is {key}, flag is {flag}")
