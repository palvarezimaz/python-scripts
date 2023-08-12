import socket


def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port {port} is open at {ipaddress}")
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets to Scan (split them by ,): ")
ports = int(input("[*] Enter how many ports you want to Scan: "))

if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
