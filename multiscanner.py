import socket

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
        finally:
            s.close()
            print(f"Socket closed.\n")

port = int(input("Enter the port that you would like to scan.\n"))
sites = [web for web in input(f"Enter websites that you would like to scan at port {port}\n").split()]

check_ips(sites, port)
