import sys
from port_scan import port_scan
from ip_scan import ip_scan
from ping import ping


def main(command, host):
    while True:
        if command == 'port_scan':
            port_scan(host)
        elif command == 'ip_scan':
            ip_scan(host)
        elif command == 'ping':
            ping(host)
        else:
            print("Invalid command")


if __name__ == '__main__':
    # Get args or show prompt
    if len(sys.argv) > 2:
        command = sys.argv[1]
        host = sys.argv[2]
    else:
        command, host = input("mnettools > ").split()

    main(command, host)
