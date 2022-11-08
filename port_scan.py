import nmap
import sys
import socket


def port_scan(host):
    try:
        # Resolve host to ip
        ip = socket.gethostbyname(host)
        print(f"Scanning {host} ({ip})")

        # Find open ports of host
        nm = nmap.PortScanner()

        # Add -sU makes it scan UDP ports and -sS makes it scan TCP ports
        # Also, -Pn disables host discovery to make scanning faster
        # -O enables OS fingerprint scan
        nm.scan(hosts=ip, arguments='-n -sU -sS -Pn -p 1-1024')

        # Print open ports
        if 'tcp' in nm[ip]:
            for i in nm[ip]['tcp']:
                print(f"Port {i} -> {nm[ip]['tcp'][i]['state']}/tcp")
        if 'udp' in nm[ip]:
            for i in nm[ip].get('udp'):
                print(f"Port {i} -> {nm[ip]['udp'][i]['state']}/udp")

    except socket.gaierror:
        print("Port scan: Unknown host")
    except KeyboardInterrupt:
        print("Port scan: Interrupted")
        sys.exit(0)


if __name__ == '__main__':
    # Get args or show prompt to get host
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = input("port_scan > ")

    port_scan(host)
