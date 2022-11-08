import sys
import nmap
import socket
import time


def ping(host):
    # Check if host is valid
    try:
        ip = socket.gethostbyname(host)
        print(f"Pinging {host} ({ip})")
        nm = nmap.PortScanner()

        # Ping host 4 times
        for i in range(4):
            # The switch -sn disables port scan and is used for ping hosts
            nm.scan(hosts=ip, arguments='-sn')
            hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

            for host, status in hosts_list:
                print(f'Reply from {host} time={nm.scanstats()["elapsed"]}s')
            time.sleep(1)

    except socket.gaierror:
        print("Ping: Unknown host")
    except KeyboardInterrupt:
        print("Ping: Interrupted")
        sys.exit(0)


if __name__ == '__main__':
    # Get args or show prompt
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = input("ping > ")

    ping(host)
