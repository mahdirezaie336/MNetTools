import sys
from port_scan import port_scan
from ip_scan import ip_scan
from ping import ping


def main(command, host):
    if command == 'port_scan':
        port_scan(host)
    elif command == 'ip_scan':
        ip_scan(host)
    elif command == 'ping':
        ping(host)


if __name__ == '__main__':
    # Get args or show prompt
    if len(sys.argv) > 2:
        command = sys.argv[1]
        host = sys.argv[2]
        main(command, host)
    else:
        while True:
            inputs = input("mnettools > ").split()
            if len(inputs) == 1:
                command = inputs[0]
                if command == 'exit':
                    sys.exit(0)
                elif command == 'help':
                    print("Commands: port_scan, ip_scan, ping, help, exit")
                else:
                    print("Invalid command")
            elif len(inputs) == 2:
                command, host = inputs[0], inputs[1]
                if command in ['port_scan', 'ip_scan', 'ping']:
                    main(command, host)
                else:
                    print("Invalid command")
            else:
                print("Invalid Input")
