import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Client: ")
    client_socket.sendto(message.encode(), ('localhost', 5001))
    data, _ = client_socket.recvfrom(1024)
    print(f"Server: {data.decode()}")

client_socket.close()
