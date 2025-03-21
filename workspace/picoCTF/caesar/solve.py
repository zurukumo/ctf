dec = "gvswwmrkxlivyfmgsrhnrisegl"


def shift(c, k):
    return chr((ord(c) - ord("a") - k) % 26 + ord("a"))


for i in range(26):
    print(f"key: {i}, flag: {''.join([shift(c, i) for c in dec])}")
