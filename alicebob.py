def generate_public_key(prime, base, private_key):
    return pow(base, private_key, prime)

def generate_shared_secret(public_key, private_key, prime):
    return pow(public_key, private_key, prime)

prime = int(input("Enter a large prime number (recommended > 2048 bits): "))
base = int(input("Enter a base (primitive root modulo of prime): "))

alice_private = int(input("Enter your private key (a random integer less than prime): "))
alice_public = generate_public_key(prime, base, alice_private)
print("Alice public key:", alice_public)

bobs_private = int(input("Enter your private key (a random integer less than prime): "))
bobs_public = generate_public_key(prime, base, bobs_private)
print("Bob's public key:", bobs_public)

alice_shared = generate_shared_secret(bobs_public, alice_private, prime)
bobs_shared = generate_shared_secret(alice_public, bobs_private, prime)

print("Alice shared key:", alice_shared)
print("Bob's shared key:", bobs_shared)

if alice_shared == bobs_shared:
    print("Success: The shared key is", alice_shared)
else:
    print("Error: Shared key doesn't match")
