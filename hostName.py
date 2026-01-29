import socket

i = 3

while i > 0:
    ips = input("Enter a website: ")

    hostname = socket.gethostbyname(ips)

    print(f"{hostname}\n")

    i -= 1
