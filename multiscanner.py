import socket
import threading

def check_ips(websites, port):
    for website in websites:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip = socket.gethostbyname(website)
            s.settimeout(5)

            s.connect((website, port))
            print(f"{website} : {ip} : {port}")
            print(f"The port at {website} is open.\n")
        except Exception as e:
            print(f"There is an error at {e}\n")
        # finally:
            # s.close()
            # print(f"Socket closed.\n")

# port = int(input("Enter the port that you would like to scan.\n"))
# sites = [web for web in input(f"Enter websites that you would like to scan at port {port}\n").split()]

# port = 80
# check_ips(sites, port)

def banner_grab(website, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(website)
        s.settimeout(5)

        s.connect((website, port))
        s.send("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n".encode())
        banner = s.recv(1024).decode().strip()
        print(f"The port at {website} : {ip} : {port}\n\n")
        print(f"Banner: {banner}\n")
    except socket.error as e:
        print(f"Error: {e}")
    finally:
        s.close()


# site = input("Enter the webite to banner grab:\n")
# banner_grab(site, port)

website = input("Enter a website: \n")
ports = [int(p) for p in input("Enter 3 ports you would like to check, seperated by space: \n").split()]

# port_list = [int(p) for p in ports]


def check_port(website, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = socket.gethostbyname(website)
    s.settimeout(5)

    try:
        s.connect((ip, port))
        message = "This socket is open."
        print(message)
    except socket.timeout:
        message = "The socket timed out."
        print(message)
    except OSError:
        message = "There's an error from the OS."
        print(message)
    except socket.gaierror:
        message = "Couldn't find the hostname."
        print(message)
    except Execption as e:
        return print(f"The error that occurred is: {e}")

threads = []
for p in ports:
    thread = threading.Thread(target = check_port, args = (website, p))
    threads.append(thread)

for t in threads:
    t.start()

for t in threads:
    t.join()
