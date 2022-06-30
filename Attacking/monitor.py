#!/usr/bin/python3
import argparse, socket, time, json, datetime, platform, psutil, requests, pprint, uuid
from tqdm import tqdm
from os import system,name
from tabulate import tabulate

try:
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    # parse args
    parser = argparse.ArgumentParser(description='Monitoring script to send system info to a tracking server')
    parser.add_argument('-d', '--dest', default='http://127.0.0.1',
                        help='API Endpoint for Monitoring Data (Defaults to http://localhost:8080/)')
    parser.add_argument('-i', '--interval', default=5, type=int,
                        help='Interval between checks (Seconds. Defaults to 5 seconds)')
    parser.add_argument('-a', '--attempts', default=30, type=int,
                        help='Attempts to send data when sending failes (Defaults to 30)')
    parser.add_argument('-t', '--timeout', default=5, type=int,
                        help='Timeout between resend attempts (Seconds. Defaults to 60. If attempts is reached script will die)')
    args = parser.parse_args()

    # Factor in sleep for bandwidth checking
    if args.interval >= 2:
        args.interval -= 2


    def main():

        # Hostname Info
        hostname = socket.gethostname()


        # Platform Info
        system = {
            "name": platform.system(),
            "version": platform.release()
        }
        global ans
        ans = system["name"] + ' ' + ' ' + system["version"]


        # Time Info
        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        uptime = int(time.time() - psutil.boot_time())
        print("\n\nHost details:")
        table_data = {
            'Hostname': [hostname],
            'OS': [ans],
            'System Uptime': [uptime]
        }
        print(tabulate(table_data, headers="keys", tablefmt="psql", showindex="True"))
        print('\n')

        # CPU Info
        cpu_count = psutil.cpu_count()
        cpu_usage = psutil.cpu_percent(interval=1)
        print("CPU:")
        cpu_tb={"Count":[cpu_count], "Usage":[cpu_usage]}
        print(tabulate(cpu_tb,headers='keys',tablefmt='psql'))
        print('\n')

        # Memory Info
        memory_stats = psutil.virtual_memory()
        memory_total = memory_stats.total
        memory_used = memory_stats.used
        memory_used_percent = memory_stats.percent
        print("Memory:")
        memory_tb={"Percent":[memory_used_percent],"Total":[memory_total / 1e+6,"MB"],"Used":[memory_used / 1e+6, "MB"]}
        print(tabulate(memory_tb,headers='keys',tablefmt='psql'))
        print('\n')

        # Disk Info
        disk_info = psutil.disk_partitions()
        print("Disks:")
        disks = []
        for x in disk_info:

            # Try fixes issues with connected 'disk' such as CD-ROMS, Phones, etc.
            try:
                disk = {
                    "name": [x.device],
                    "mount_point": [x.mountpoint],
                    "type": [x.fstype],
                    "total_size": [psutil.disk_usage(x.mountpoint).total],
                    "used_size": [psutil.disk_usage(x.mountpoint).used],
                    "percent_used": [psutil.disk_usage(x.mountpoint).percent]
                }

                disks.append(disk)
                print(tabulate(disk, headers='keys', tablefmt='psql'))

            except:
                print("")
        print('\n')

        # Bandwidth Info
        network_stats = get_bandwidth()
        print("Network:\n")
        network_tb={"Traffic in":[network_stats["traffic_in"] / 1e+6],
                    "Traffic out":[network_stats["traffic_out"] / 1e+6]
                    }
        print(tabulate(network_tb,headers='keys',tablefmt='psql'))
        print('\n')

        # Network Info
        nics = []
        print("NICs:")
        for name, snic_array in psutil.net_if_addrs().items():
            # Create NIC object
            nic = {
                "name": name,
                "mac": "",
                "address": "",
                "address6": "",
                "netmask": ""
            }
            # Get NiC values
            for snic in snic_array:
                if snic.family == -1:
                    nic["mac"] = snic.address
                elif snic.family == 2:
                    nic["address"] = snic.address
                    nic["netmask"] = snic.netmask
                elif snic.family == 23:
                    nic["address6"] = snic.address
            nics.append(nic)

            nic_data = {"NIC": [nic["name"]],
                        "MAC": [nic["mac"]],
                        "IPv4 Address": [nic["address"]],
                        "IPv4 Subnet": [nic["netmask"]],
                        "IPv6 Address": [nic["address6"]]
                        }
            print(tabulate(nic_data, headers='keys', tablefmt='psql'))
        print('\n')

        try:
            # System UUID
            sys_uuid = uuid.getnode()

            # Set Machine Info
            machine = {
                "hostname": [hostname],
                "uuid": [sys_uuid],
                "system": [ans],
                "uptime": [uptime],
                "cpu_count": [cpu_count],
                "cpu_usage": [cpu_usage],
                "memory_total": [memory_total],
                "memory_used": [memory_used],
                "memory_used_percent": [memory_used_percent],
                "network_up": [network_stats["traffic_out"]],
                "network_down": [network_stats["traffic_in"]],
                "timestamp": [timestamp]
            }

            data = json.dumps(machine)
            print("Data:")
            print(tabulate(machine,headers='keys',tablefmt='psql'))



        except:
            print("")


    def get_bandwidth():
        # Get net in/out
        net1_out = psutil.net_io_counters().bytes_sent
        net1_in = psutil.net_io_counters().bytes_recv

        time.sleep(1)

        # Get new net in/out
        net2_out = psutil.net_io_counters().bytes_sent
        net2_in = psutil.net_io_counters().bytes_recv

        # Compare and get current speed
        if net1_in > net2_in:
            current_in = 0
        else:
            current_in = net2_in - net1_in

        if net1_out > net2_out:
            current_out = 0
        else:
            current_out = net2_out - net1_out

        network = {"traffic_in": current_in, "traffic_out": current_out}
        return network


    def send_data(data):
        # Attempt to send data up to 30 times
        for attempt in range(args.attempts):
            try:
                # endpoint = monitoring server
                endpoint = args.dest
                response = requests.post(url=endpoint, data=data)
                print("\nPOST:")
                print("\n\tResponse:", response.status_code)
                print("\n\tHeaders:")
                pprint.pprint(response.headers)
                # Attempt printing response in JSON if possible
                try:
                    print("JSON Content:")
                    pprint.pprint(response.json())
                except:
                    print("No JSON content")
                break
            except requests.exceptions.RequestException as e:
                print("\n POST ERROR (Use -d <API URL> ):\n", e)
                print("\n Completed ....\n", e)
                # Sleep 1 minute before retrying
                exit()
        else:
            # If no connection established for attempts*timeout, kill script
            exit(0)

    main()
    print("\n\n")
    for i in tqdm(range(10), 'Data Gathering completed', colour='green'):
        time.sleep(.1)

    if name == 'nt':
        system('python gnet.py &  gcpu.py')
    else:
        system('./gcpu.py & ./gnet.py')

    print("-" * 200)
    time.sleep(args.interval)
except:
    print("Unexpected error occured try again")