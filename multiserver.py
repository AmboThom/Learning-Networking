import socket
import threading

host = ''
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(f"Socket Error: {e}")

s.listen(5)
conn, addr = s.accept()


