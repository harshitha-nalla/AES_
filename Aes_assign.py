import textwrap

 # Adjust width as needed

from Crypto.Cipher import AES

key = b"SrmapUniversity1"
iv = b"pqrstuvwxyzabcde"

def decrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(data).decode().rstrip("\0")

def encrypt_data(text):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = text + (16 - len(text) % 16) * "\0"
    return cipher.encrypt(padded_text.encode())

file = input("Enter the file name: ")

with open(file, "r") as f:
    plaintext = f.read()

encrypted_data = encrypt_data(plaintext)
print("Encrypted Data:", encrypted_data)

decrypted_text = decrypt_data(encrypted_data)
print("Decrypted Data:", decrypted_text)
