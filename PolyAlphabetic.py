def generateKey(pt: str, key: str):
    key = list(key)
    if len(pt) == len(key):
        return key
    else:
        for i in range(len(pt) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encrypt(pt: str, key: str) -> str:
    res = []
    for i in range(len(pt)):
        x = (ord(pt[i]) + ord(key[i])) % 26
        x += ord('A')
        res.append(chr(x))
    return "".join(res)


if __name__ == '__main__':
    pt = input("Enter the plain text - ")
    key = input("Enter the key - ")
    ct = encrypt(pt, key)
    print(f"")