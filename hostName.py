import socket

# Prints the IP Address of 3 websites that the user inputs

"""
i = 3

while i > 0:
    ips = input("Enter a website: ")

    hostname = socket.gethostbyname(ips)

    print(f"{hostname}\n")

    i -= 1
"""

website = input("Enter a website: \n")
port = int(input("Enter the port you would like to check: \n"))

def check_port(website, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = socket.gethostbyname(website)
    s.settimeout(10)

    if s.connect((ip, port)):
        return print("This port is open.")
    else:
        return print("This port is closed.")


check_port(website, port)
