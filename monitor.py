#!/usr/bin/python3
import argparse, socket, time, json, datetime, platform, psutil, requests, pprint, uuid
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from os import system,name
from tqdm import tqdm

if name=='nt':
    system('cls')
else:
    system('clear')
# parse args
parser = argparse.ArgumentParser(description='Monitoring script to send system info to a tracking server')
parser.add_argument('-d', '--dest', default='http://127.0.0.1', help='API Endpoint for Monitoring Data (Defaults to http://localhost:8080/)')
parser.add_argument('-i', '--interval', default=5, type=int, help='Interval between checks (Seconds. Defaults to 5 seconds)')
parser.add_argument('-a', '--attempts', default=30, type=int, help='Attempts to send data when sending failes (Defaults to 30)')
parser.add_argument('-t', '--timeout', default=5, type=int, help='Timeout between resend attempts (Seconds. Defaults to 60. If attempts is reached script will die)')
args = parser.parse_args()

# Factor in sleep for bandwidth checking
if args.interval >= 2:
    args.interval -= 2

def main():
    # Hostname Info
    hostname = socket.gethostname()
    print("\nHostname:", hostname)

    # Platform Info
    system = {
        "name" : platform.system(),
        "version" : platform.release()
    }
    global ans
    ans=system["name"]+' '+' '+system["version"]
    print("\nOS:", ans)

    # Time Info
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    uptime = int(time.time() - psutil.boot_time())
    print("\nSystem Uptime:",uptime)
    print('\n')

    # CPU Info
    cpu_count = psutil.cpu_count()
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU:\n\tCount:", cpu_count, "\n\tUsage:", cpu_usage)
    print('\n')

    # Memory Info
    memory_stats = psutil.virtual_memory()
    memory_total = memory_stats.total
    memory_used = memory_stats.used
    memory_used_percent = memory_stats.percent
    print("Memory:\n\tPercent:", memory_used_percent, "\n\tTotal:", memory_total / 1e+6, "MB", "\n\tUsed:", memory_used / 1e+6, "MB")
    print('\n')

    # Disk Info
    disk_info = psutil.disk_partitions()
    print("Disks:")
    disks = []
    for x in disk_info:

        # Try fixes issues with connected 'disk' such as CD-ROMS, Phones, etc.
        try:
            disk = {
                "name" : x.device,
                "mount_point" : x.mountpoint,
                "type" : x.fstype,
                "total_size" : psutil.disk_usage(x.mountpoint).total,
                "used_size" : psutil.disk_usage(x.mountpoint).used,
                "percent_used" : psutil.disk_usage(x.mountpoint).percent
            }

            disks.append(disk)

            print("\tDisk name",disk["name"], "\n\tMount Point:", disk["mount_point"], "\tType",disk["type"], "\n\tSize:", disk["total_size"] / 1e+9,"\n\tUsage:", disk["used_size"] / 1e+9, "\n\tPercent Used:", disk["percent_used"])
        except:
            print("")
    print('\n')

    # Bandwidth Info
    network_stats = get_bandwidth()
    print("Network:\n\tTraffic in:",network_stats["traffic_in"] / 1e+6,"\n\tTraffic out:",network_stats["traffic_out"] / 1e+6)
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
        print("\tNIC:",nic["name"], "\tMAC:", nic["mac"], "\tIPv4 Address:",nic["address"], "\tIPv4 Subnet:", nic["netmask"], "\tIPv6 Address:", nic["address6"])
    print('\n')

    try:
        # System UUID
        sys_uuid = uuid.getnode()

        # Set Machine Info
        machine = {
            "hostname": hostname,
            "uuid": sys_uuid,
            "system": ans,
            "uptime": uptime,
            "cpu_count": cpu_count,
            "cpu_usage": cpu_usage,
            "memory_total": memory_total,
            "memory_used": memory_used,
            "memory_used_percent": memory_used_percent,
            "network_up": network_stats["traffic_out"],
            "network_down": network_stats["traffic_in"],
            "timestamp": timestamp
        }

        data = json.dumps(machine)
        print("Data:")
        for k, v in machine.items():
            print('\t', k, ': ', v)

        send_data(data)
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

    network = {"traffic_in" : current_in, "traffic_out" : current_out}
    return network

def send_data(data):
    # Attempt to send data up to 30 times
    for attempt in range(args.attempts):
        try:
            # endpoint = monitoring server
            endpoint = args.dest
            response = requests.post(url = endpoint, data = data)
            print("\nPOST:")
            print("\n\tResponse:", response.status_code)
            print("\n\tHeaders:")
            pprint.pprint(response.headers)
            print("\n\tContent:", response.content)
            # Attempt printing response in JSON if possible
            try:
                print("JSON Content:")
                pprint.pprint(response.json())
            except:
                print("No JSON content")
            break
        except requests.exceptions.RequestException as e:
            print("\n POST ERROR (Use -d <API URL> ):\n",e)
            # Sleep 1 minute before retrying
            exit()
    else:
        # If no connection established for attempts*timeout, kill script
        exit(0)


main()
for i in tqdm(range(10), 'Data Gathering completed', colour='green'):
    time.sleep(.1)
#graph
try:
    frame_len = 200
    y = []
    fig = plt.figure(figsize=(6,2))


    def animation(i):
        y.append(psutil.cpu_percent())
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y, 'r', label='CPU usage(%)')
        else:
            plt.cla()
            plt.plot(y[-frame_len:], 'r', label='cpu usage(%)')
        plt.xlabel('Time (s)')
        plt.ylabel('CPU usage(%)')
        plt.title("REAL-TIME CPU Usage in percentage")
        plt.legend(loc='upper right')


    animate = FuncAnimation(plt.gcf(), animation, interval=1000)
    plt.show()
except KeyboardInterrupt:
    print("Ctrl + C Entered. Exiting....")


time.sleep(args.interval)
