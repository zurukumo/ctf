import base64

with open("enc_flag", "r") as f:
    enc = f.read().strip()

print(enc)

dec_first = base64.b64decode(enc).decode()
dec_first = dec_first[2:-2]
print(dec_first)

dec_second = base64.b64decode(dec_first).decode()
print(dec_second)

for i in range(26):
    dec_third = ""
    for c in dec_second:
        if c.islower():
            dec_third += chr((ord(c) - ord("a") + i) % 26 + ord("a"))
        elif c.isupper():
            dec_third += chr((ord(c) - ord("A") + i) % 26 + ord("A"))
        else:
            dec_third += c
    print(f"when i is {i}, flag is {dec_third}")
