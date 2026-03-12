import socket
import os

Host = "127.0.0.1"
Port = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created.\n")
try:
    sock.bind((Host, Port))
    print("Socket Binded.\n")
    print(f"Address: {Host}, Port: {Port}")
except socket.error as e:
    print("Socket error: ", e)

sock.listen(5)
#TODO: Create while loop
while True:
    connection, address = sock.accept()
    process_id = os.fork()
    if process_id == 0:
        data = connection.recv(1024)
        message = data.decode()
        print(f"Received: {message}")
        if not data:
            break
        connection.send(data)
        connection.close()
    elif process_id > 0:
        print(f"A child was born!")
    else:
        print(f"Fork Failed.")


#TODO: Create child process
#TODO: Have check if current process is a child or parent
#TODO: If in child, do recv and send
#TODO: If in parent log that child created successfully
#TODO: If child created failed, log child failed


#connection, address = sock.accept()
#
#print(f"Got connection from: {address}\n")

#data = connection.recv(1024)
#connection.send(data)

print(f"Server Got: {data.decode()}\n")
