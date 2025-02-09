import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 5001))
print("UDP Server listening on port 5001...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Client: {data.decode()}")
    response = input("Server: ")
    server_socket.sendto(response.encode(), addr)
