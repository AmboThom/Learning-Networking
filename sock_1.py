import socket

Host = input("Enter Host IP Address: ")
Port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created.")
try:
    sock.bind((Host, Port))
    print("Socket Binded.")
    print(f"Address: {Host}, Port: {Port}")
except socket.error as e:
    print("Socket error: ", e)
