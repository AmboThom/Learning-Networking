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
        # finally:
            # s.close()
            # print(f"Socket closed.\n")

# port = int(input("Enter the port that you would like to scan.\n"))
# sites = [web for web in input(f"Enter websites that you would like to scan at port {port}\n").split()]

port = 80
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


site = input("Enter the webite to banner grab:\n")
banner_grab(site, port)
