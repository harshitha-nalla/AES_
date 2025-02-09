import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(1)
print("Server listening on port 5000...")

conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")
    response = input("Server: ")
    conn.send(response.encode())

conn.close()
server_socket.close()
