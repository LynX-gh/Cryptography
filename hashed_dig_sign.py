import hashlib
import rsa

# Generate RSA key pair
(public_key, private_key) = rsa.newkeys(512)

# Message to sign
message = b"Digital Signature"

# Generate SHA-256 hash of message
hash_value = hashlib.sha256(message).digest()

# Sign hash with private key
signature = rsa.sign(hash_value, private_key, 'SHA-256')

# Verify signature with public key
verified = rsa.verify(hash_value, signature, public_key)

# Print results
print("Hash value: ", hash_value.hex())
print("Signature: ", signature.hex())
print("Verified: ", verified)
