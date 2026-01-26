import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("", 8888))

test = "612 Walf Aveune"
client.send(test.encode())
data = client.recv(1024)

print(f"Client Got: {data.decode()}")
