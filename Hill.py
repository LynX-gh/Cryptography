import numpy as np


def keyMatrixGen(key: str) -> list:
    res = []
    k = 0
    for _ in range(3):
        tmpres = []
        for j in range(3):
            tmpres.append(ord(key[k]) - 97)
            k += 1
        res.append(tmpres)
    return res


def mulMatrix(pt: str, keyMatrix: list) -> np.ndarray:
    ptMatrix = list(ord(i) - 97 for i in pt)
    res = np.dot(keyMatrix, ptMatrix)
    return res


def encrypt(pt: str, key: str) -> str:
    res = ""
    keyMatrix = keyMatrixGen(key)
    for i in range(0, len(pt), 3):
        resMatrix = mulMatrix(pt[i:i + 3], keyMatrix)
        for j in range(3):
            res += chr(resMatrix[j] % 26 + 97)
    return res


if __name__ == '__main__':
    pt = input("Enter the plain text - ").lower()
    key = input("Enter the key - ").lower()
    if len(pt) % 3 != 0:
        pt += 'x' * (3 - len(pt) % 3)
    ct = encrypt(pt, key)
    print(f"The encrypted text is - {ct}")
