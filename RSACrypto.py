import math


def gcd(n1: int, n2: int) -> int:
    if n2 == 0:
        return abs(n1)
    else:
        return gcd(n2, n1 % n2)


def encrypt(pt: int, p: int, q: int) -> float:
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1
    k = 2
    d = (1 + (k * phi)) / e
    return math.fmod(pow(pt, e), n)


if __name__ == '__main__':
    p = int(input("Enter a prime no - "))
    q = int(input("Enter another prime no - "))
    pt = int(input("Enter the message - "))
    ct = encrypt(pt, p, q)
    print(f"The encrypted text is {ct}")
