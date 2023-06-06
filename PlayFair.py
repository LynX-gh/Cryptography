def genKeyMatrix(key: str) -> list:
    res = []
    usedChar = set('j')
    for ch in key:
        if ch not in usedChar:
            res += ch
            usedChar.add(ch)
    for i in range(97, 123):
        if chr(i) not in usedChar:
            res += chr(i)
            usedChar.add(chr(i))
    return [res[i:i + 5] for i in range(0, 25, 5)]


def splitPt(pt: str):
    res = ""
    i = 0
    while i + 1 < len(pt):
        if pt[i] == pt[i + 1]:
            res += pt[i] + "x"
            i += 1
        else:
            res += pt[i]
            res += pt[i + 1]
            i += 2
    if i < len(pt):
        res += pt[i]+"z"
    return [res[i:i + 2] for i in range(0, len(res) - 1, 2)]


def charPos(ch: chr, keyMatrix: list) -> list:
    for i in range(5):
        for j in range(5):
            if keyMatrix[i][j] == ch:
                return [i, j]


def encrypt(pt: str, key: str) -> str:
    res = ""
    keyMatrix = genKeyMatrix(key)
    ptPair = splitPt(pt)
    print(keyMatrix)
    print(ptPair)
    for pair in ptPair:
        p1 = charPos(pair[0], keyMatrix)
        p2 = charPos(pair[1], keyMatrix)
        if p1[1] == p2[1]:
            res += keyMatrix[p1[0] + 1][p1[1]] if p1[0] + 1 < 5 else keyMatrix[0][p1[1]]
            res += keyMatrix[p2[0] + 1][p2[1]] if p2[0] + 1 < 5 else keyMatrix[0][p2[1]]
        elif p1[0] == p2[0]:
            res += keyMatrix[p1[0]][p1[1] + 1] if p1[1] + 1 < 5 else keyMatrix[p1[0]][0]
            res += keyMatrix[p2[0]][p2[1] + 1] if p2[1] + 1 < 5 else keyMatrix[p2[0]][0]
        else:
            res += keyMatrix[p1[0]][p2[1]]
            res += keyMatrix[p2[0]][p1[1]]
    return res


if __name__ == '__main__':
    pt = input("Enter the plain text - ").replace("j", "i")
    key = input("Enter the key - ")
    ct = encrypt(pt, key)
    print(f"The encrypted text is {ct}")
