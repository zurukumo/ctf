import hashlib

username = b"SCHOFIELD"
hashed = hashlib.sha256(username).hexdigest()

dec = "picoCTF{1n_7h3_|<3y_of_"
for i in [4, 5, 3, 6, 2, 7, 1, 8]:
    dec += hashed[i]
dec += "}"
print(dec)
