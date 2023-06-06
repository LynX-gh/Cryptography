def encrypt(pt: str, k: int) -> str:
    res = ""
    for char in pt:
        res += chr((ord(char) + k - 97) % 26 + 97)
    return res


def decrypt(ct: str, k: int) -> str:
    res = ""
    for char in ct:
        res += chr((ord(char) + 26 - k - 97) % 26 + 97)
    return res


if __name__ == '__main__':
    pt = input("Enter the plain text - ").lower()
    key = int(input("Enter the key - "))
    ct = encrypt(pt, key)
    print(f"Cipher Text is - {ct}")
    print(f"Decryption is - {decrypt(ct, key)}")
