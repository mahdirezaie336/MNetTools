import sys
import nmap


# Get args or show prompt to get ip range
if len(sys.argv) > 1:
    ip_range = sys.argv[1]
else:
    ip_range = input("ip_scan > ")


try:
    # Find active hosts
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    # Sort hosts by ip
    hosts_list = sorted(hosts_list, key=lambda x: x[0])

    # Print active hosts
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))
except KeyboardInterrupt:
    print("IP scan: Interrupted")
    sys.exit(0)
