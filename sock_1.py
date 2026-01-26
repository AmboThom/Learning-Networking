import socket

Host = "127.0.0.1"
Port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created.")
try:
    sock.bind((Host, Port))
    print("Socket Binded.")
    print(f"Address: {Host}, Port: {Port}")
except socket.error as e:
    print("Socket error: ", e)

sock.listen(5)
connection, address = sock.accept()
print(f"Got connection from: {address}")

data = connection.recv(1024)
connection.send(data)

print(f"Server Got: {data.decode()}")
