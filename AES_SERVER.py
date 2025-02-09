import socket
from Crypto.Cipher import AES
import base64

Key = b"SrmapUniversity1"
IV = b"pqrstuvwxyzabcde"

def Decrypt(encrypted_msg):
   cipher=AES.new(Key, AES.MODE_CBC, IV)
   dec_msg=cipher.decrypt((encrypted_msg))
   return dec_msg

def Encrypt(msg):
    cipher = AES.new(Key, AES.MODE_CBC, IV)
    message_padded = msg + (16 - len(msg) % 16) * "\0"
    enc_msg = cipher.encrypt(message_padded.encode())
    return enc_msg


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 5000))
    print("Server started")

    while True:
        message, addr = server_socket.recvfrom(1024)
        print(f"Client_encrypted: {message}")
        dec_msg = Decrypt(message).decode()
        print(f"Decrypted message: {dec_msg}")
        reply = input("Server: ")
        reply=Encrypt(reply)
        server_socket.sendto(reply, addr)

start_server()
