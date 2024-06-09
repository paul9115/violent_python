import socket
import os
import sys

def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect(ip, port)
        banner = s.recv(1024)
        return banner
    except:
        print(f'[-] {ip}:{port} appears to be closed')
        return


def check_vulns(banner, filename):
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line.strip('\n') in banner:
                print(f'[+] Server is vulnerable: {banner.strip("\n")}')


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print(f'[-] {filename} does not exist')
            exit(0)
        if not os.access(filename, os.R_OK):
            print(f'[-] Could not read {filename}: access denied')
            exit(0)
    else:
        print(f'[-] Usage: {sys.argv[0]} <vuln filename>')
        exit(0)
    portlist = [21, 22, 25, 80, 110, 443, ]
    for x in range(1, 255):
        ip = f'10.10.0.{x}'
        for port in portlist:
            banner = ret_banner(ip, port)
            print(f'[+] Checking {ip}:{port}')
            if banner:
                print(f'[+] {ip}: {banner.strip('\n')}')
                check_vulns(banner)


if __name__ == '__main__':
    main()
