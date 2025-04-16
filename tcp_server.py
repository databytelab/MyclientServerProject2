import socket

host = 'localhost'
port = 12345
sock_addr = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(sock_addr)
server_socket.listen(5)

while True:
    print("The server is waiting for the connection!")
    client_socket, addr = server_socket.accept()
    print(f"Client connected from {addr}")

    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        print(f"Received from client: {data.decode('utf-8')}")
        try:
            reply = "Hey client, How can i assist you?"
            client_socket.send(reply.encode('utf-8'))
        except KeyboardInterrupt:
            print("Exited by the user")
    break
server_socket.close()
