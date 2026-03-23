import socket
import os
import sys
import signal

Host = "127.0.0.1"
Port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created.\n")

def signal_handler(sig, frame):
    sock.close()
    print(" Program Ended.")
    sys.exit(0)

try:
    sock.bind((Host, Port))
    print("Socket Binded.\n")
    print(f"Address: {Host}, Port: {Port}")
except socket.error as e:
    print("Socket error: ", e)

sock.listen(5)

signal.signal(signal.SIGINT, signal_handler)

# Client connects to Server
while True:
    connection, address = sock.accept()
    # Child Process is created
    process_id = os.fork()
    # Checks if current process is child
    if process_id == 0:
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        # Keeps the connection open
        while True:
            data = connection.recv(1024)
            message = data.decode()
            print(f"Received: {message}")
            if not data:
                break
            connection.send(data)
        connection.close()
    # Parent logs Child created
    elif process_id > 0:
        print(f"A child was born!")
    else:
        print(f"Fork Failed.")
