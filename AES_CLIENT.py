import socket
from Crypto.Cipher import AES


Key = b"SrmapUniversity1"
IV = b"pqrstuvwxyzabcde"

def Encrypt(msg):
    cipher = AES.new(Key, AES.MODE_CBC, IV)
    message_padded = msg + (16 - len(msg) % 16) * "\0"
    enc_msg = cipher.encrypt(message_padded.encode())
    return enc_msg


def Decrypt(encrypted_msg):
    cipher = AES.new(Key, AES.MODE_CBC, IV)
    dec_msg = cipher.decrypt((encrypted_msg))
    return dec_msg


def Client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("Client: ")
        encrypted_msg = Encrypt(message)
        client_socket.sendto(encrypted_msg, ('localhost', 5000))
        reply, _ = client_socket.recvfrom(1024)
        decrypted_reply = Decrypt(reply).decode()
        print(f'Server_encrypted: {reply}')
        print(f"Server: {decrypted_reply}")

Client()
