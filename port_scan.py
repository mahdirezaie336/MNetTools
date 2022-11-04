import nmap
import sys
import socket


# Get args or show prompt to get host
if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = input("port_scan > ")

try:
    # Resolve host to ip
    ip = socket.gethostbyname(host)
    print("Scanning " + host + " (" + ip + ")")

    # Find open ports of host
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments='-n -p 1-1024')
    ports_list = [(x, nm[ip]['tcp'][x]['state']) for x in nm[ip]['tcp']]
    ports_list = sorted(ports_list, key=lambda x: x[0])

    # Print open ports
    for port, status in ports_list:
        print('{0}:{1}'.format(port, status))
except socket.gaierror:
    print("Port scan: Unknown host")
except KeyboardInterrupt:
    print("Port scan: Interrupted")
    sys.exit(0)
