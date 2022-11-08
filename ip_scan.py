import sys
import nmap


def ip_scan(ip_range):
    try:
        # Find active hosts
        nm = nmap.PortScanner()

        # Adding -n disables DNS resolution which makes it faster
        # Ip range scan uses -sn to disable port scan
        nm.scan(hosts=ip_range, arguments='-n -sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

        # Sort hosts by ip
        hosts_list = sorted(hosts_list, key=lambda x: [int(i) for i in x[0].split('.')])

        # Print active hosts
        for host, status in hosts_list:
            print(f'{host} -> LIVE')
    except KeyboardInterrupt:
        print("IP scan: Interrupted")
        sys.exit(0)


if __name__ == '__main__':
    # Get args or show prompt to get ip range
    if len(sys.argv) > 1:
        ip_range = sys.argv[1]
    else:
        ip_range = input("ip_scan > ")

    ip_scan(ip_range)
