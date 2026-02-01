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
ports = [int(p) for p in input("Enter 5 ports you would like to check, seperated by space: \n").split()]

# port_list = [int(p) for p in ports]


def check_port(website, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = socket.gethostbyname(website)
    s.settimeout(5)

    try:
        s.connect((ip, port))
        message = "This socket is open."

        save_results(website, ip, port, message)
    except socket.timeout:
        message = "The socket timed out."
        save_results(website, ip, port, message)
    except OSError:
        message = "There's an error from the OS."
        save_results(website, ip, port, message)
    except socket.gaierror:
        message = "Couldn't find the hostname."
        save_results(website, ip, port, message)
    except Execption as e:
        return print(f"The error that occurred is: {e}")

def save_results(website, ip, port, message):
    with open('port_results.txt', 'a', newline = '\n') as file:
        file.writelines(website + " : " + ip + " : " + str(port) + "\n" + message + "\n\n")

check_port(website, ports[0])
check_port(website, ports[1])
check_port(website, ports[2])
check_port(website, ports[3])
check_port(website, ports[4])
