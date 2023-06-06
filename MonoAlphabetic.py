key = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n',
       'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}


def encrypt(pt: str) -> str:
    res = ""
    for char in pt:
        res += key[char]
    return res


def decrypt(ct: str) -> str:
    res = ""
    for char in ct:
        res += key[char]
    return res


if __name__ == "__main__":
    pt = input("Enter the plain text - ").lower()
    ct = encrypt(pt)
    print(f"Cipher Text is - {ct}")
    print(f"Decryption is - {decrypt(ct)}")
