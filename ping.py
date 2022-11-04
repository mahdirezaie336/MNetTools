import sys
import nmap
import socket


# Get args or show prompt
if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = input("ping > ")

# Check if host is valid
try:
    ip = socket.gethostbyname(host)
    print("Pinging " + host + " (" + ip + ")")
    nm = nmap.PortScanner()

    # Ping host 4 times
    for i in range(4):
        nm.scan(hosts=ip, arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print('{0}:{1}'.format(host, status))

except socket.gaierror:
    print("Ping: Unknown host")
except KeyboardInterrupt:
    print("Ping: Interrupted")
    sys.exit(0)
