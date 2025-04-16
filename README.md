# MyClientServerProject
# Simple Python TCP Client-Server

This is a simple client-server project in Python using sockets.

## 🖥 Files

- `server.py`: Listens for incoming client connections and replies.
- `client.py`: Connects to the server and sends a message.

## ⚙️ How it Works

1. The **server** binds to `127.0.0.1` on port `12345` and waits for a connection.
2. The **client** connects to the server and sends a message.
3. The server receives it and sends back a reply.

## ▶️ Run the Program

1. Open two terminals.
2. Run the server in the first terminal: python server.py
3. Run the client in the second terminal: python client.py
