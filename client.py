import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

while True:
    message = input("Client: ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

client_socket.close()
