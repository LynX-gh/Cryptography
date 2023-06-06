def enc

if __name__ == "__main__":
    pt = input("Enter the plain text - ").lower()
    ct = encrypt(pt)
    print(f"Cipher Text is - {ct}")
    print(f"Decryption is - {decrypt(ct)}")
