c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537

# Used factordb.com
p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003

phi = (p - 1) * (q - 1)


def mod_inverse(a, m):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m


d = mod_inverse(e, phi)

m = pow(c, d, n)


def long_to_bytes(n):
    bytes_data = []
    while n > 0:
        bytes_data.insert(0, n & 0xFF)
        n >>= 8
    return bytes(bytes_data)


plaintext = long_to_bytes(m)

print(plaintext)
