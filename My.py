import socket

host = 'localhost'
port = 12345
sock_addr = (host, port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(sock_addr)

payload = "Hey server, I am a client"

try:
    while True:
        client_socket.send(payload.encode('utf-8'))

        data = client_socket.recv(4096)
        print(f"Received from the server: {data.decode('utf-8')}")

        more = input("Want to send more data to the server [y/n]:")
        if more.lower() =='y':
            payload = input("Enter the payload you want to send!")
        else:
            break
except KeyboardInterrupt:
    print("Exited by the user")
    client_socket.close()