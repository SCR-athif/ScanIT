#!/usr/bin/python3

#importing modules 
import socket
import Output
import builtwith
from package import wlookup
import pyfiglet
from package import map
import time
from datetime import datetime
from os import system
from termcolor import colored
from tqdm import tqdm


try:
    # Option 1 portscaning
    def portscan():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner'), 'red')
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        print(
            "Choose option: \n\n 1. Specific Port Scan\n\n 2. Specific Port Range Scan\n\n 3. Full port Scan (Take more time) \n\n Enter 0 to back ")
        a = int(input("\n\nEnter here: "))
        if a == 1:
            IP = input('\nEnter victims IP (eg: - 192.168.1.1): ')
            Output.newline()
            spt(IP)
        elif a == 2:
            rpt()
        elif a == 3:
            fpt()
        elif a==0:
            system('./scanning/main.py')

    # Range Port scanning
    def rpt():
        IP = input('\nEnter victims IP (eg: - 192.168.1.1): ')
        n1 = int(input('starting port (eg:- 22): '))
        n2 = int(input('Ending port (eg: - 100): '))
        try:
            Output.newline()
            print('port     Status       service')
            for port in range(n1, n2):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                if s.connect_ex((IP, port)):
                    pass
                else:
                    serv = socket.getservbyport(int(port))
                    Output.ptopen(IP, port, serv)
                    t1 = datetime.now()
                    print(f"{port}         open       {serv}")
            print('\n\n')
            for i in tqdm(range(10)):
                time.sleep(.01)
            t2 = datetime.now()
            total = t2 - t1
            print("Scanning completed in ", total)
            back = input("Do you want scan again (y/n): ")
            if back == 'y' or back == 'Y':
                system('./scanning/main.py')


        except socket.gaierror:
            print('Hostname seems down')

        except socket.error:
            print("Couldn't connect to server")


    # Full Port Scan
    def fpt():
        IP = input('\nEnter victims IP (eg: - 192.168.1.1): ')
        try:
            Output.newline()
            print('port     Status       service')
            for port in range(1, 65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                if s.connect_ex((IP, port)):
                    pass
                else:
                    serv = socket.getservbyport(int(port))
                    Output.ptopen(IP, port, serv)
                    t1 = datetime.now()
                    print(f"{port}         open       {serv}")
            print('\n\n')
            for i in tqdm(range(10)):
                time.sleep(.01)
            t2 = datetime.now()
            total = t2 - t1
            print("Scanning completed in: ", total)
            back = input("Do you want scan again (y/n): ")
            if back == 'y' or back == 'Y':
                system('./scanning/main.py')

        except OSError:
            pass
        except socket.gaierror:
            print('Hostname seems down')

        except socket.error:
            print("Couldn't connect to server")
    # Single Port Scanning
    def spt(IP):
        try:
            port = str(input("Enter your port (eg: - 22): "))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            t1 = datetime.now()
            print('port     Status       service')
            if s.connect_ex((IP, int(port))):
                Output.ptclose(IP, port)
                print(f"{port}         close")
                spt(IP)
            else:
                serv = socket.getservbyport(int(port))
                Output.ptopen(IP, port, serv)
                print(f"{port}         open       {serv}")
                print('\n\n')
                for i in tqdm(range(10)):
                    time.sleep(.01)
                t2 = datetime.now()
                total = t2 - t1
                print("Scanning completed in: ", total)
                back = input("Do you want scan again (y/n): ")
                if back == 'y' or back == 'Y':
                    system('./scanning/main.py')

        except socket.gaierror:
            print('Hostname seems down')

        except socket.error:
            print("Couldn't connect to server")


    # Live Host Scanning
    def Total():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("S c a n I T", 'banner4'), 'blue')
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        t1 = datetime.now()

        # Full Host Scan
        def fscan():
            nm = map.nmap.PortScanner()
            IP = input("Enter IP (eg: - 192.168.1.1): ")
            print('\nScanning Intiated\n', '-' * 50, '\n')
            if '/24' in IP:
                nm.scan(hosts=IP, arguments='-n -sP')
                hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
                Output.newline()
                for host, status in hosts_list:
                    print(host + ' is ' + status)
                    Output.fdata(host, status)
            else:
                nm.scan(hosts=IP, arguments='-n -sP')
                hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
                Output.newline()
                for host, status in hosts_list:
                    print(host + ' is ' + status)
                    Output.fdata(host, status)

        # Host scan with specific port running
        def sscan(addr):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((addr, int(port)))
            if result == 0:
                return 1
            else:
                return 0

        # Host scan with specific set of port running
        def rscan(addr, aport):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(.01)
            result = s.connect_ex((addr, int(aport)))
            if result == 0:
                return 1
            else:
                return 0

        def run1():
            a = """
            Choose option:

                1. Fast scan

                2. Scan in specific port

                3. Scan in set of port (Slow Mode)
    
            Enter 0 to go back 
            """
            print(a)
            a = int(input("Enter here: "))
            if a == 1:
                fscan()
            elif a == 2:
                entry()
                global port
                port = input("Enter port number (eg: - 22):")
                Output.newline()
                for ip in range(st1, en1):
                    addr = net2 + str(ip)
                    if (sscan(addr)):
                        Output.total(addr)
                        print(addr, "is up")
            elif a == 3:
                entry()
                n1 = input("Enter starting range (eg: - 1):")
                n2 = input("Enter ending range (eg: - 255):")
                Output.newline()
                for ip in range(st1, en1):
                    addr = net2 + str(ip)
                    for port1 in range(int(n1), int(n2)):
                        if (rscan(addr, port1)):
                            Output.total(addr)
                            print(addr, "is up")
            elif a == 0:
                system('./scanning/main.py')
        def entry():
            global net, net1, l, net2, st1, en1, n1, n2
            net = input("Enter the IP address (eg: - 192.168.1.1): ")
            net1 = net.split('.')
            l = '.'
            net2 = net1[0] + l + net1[1] + l + net1[2] + l
            st1 = int(input("Starting host (eg: - 1): "))
            en1 = int(input("Enting host (eg: - 255): "))
            en1 = en1 + 1

        run1()
        print('\n\n')
        for i in tqdm(range(10)):
            time.sleep(.01)
        t2 = datetime.now()
        total = t2 - t1
        print("Scanning completed in: ", total)
        back = input("Do you want scan again (y/n): ")
        if back=='y' or back=='Y':
            system('./scanning/main.py')

    # Version Scanning
    def version():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("    S c a n I T", 'arrows'), 'blue')
        t1 = datetime.now()
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        print(
            "Choose option: \n\n 1. Version scanning with range entry \n\n 2. Version Scanning with single entry \n\n 3. Version with full port scan (Take more time to complete scan) \n\n Enter 0 to back ")
        a = int(input("\nEnter your option: "))
        if (a == 2):
            IP = input("\nEnter Victims IP (eg: - 192.168.1.1): ")
            sbs(IP)
        elif (a == 1):
            IP = input("\nEnter Victims IP (eg: - 192.168.1.1): ")
            rbs(IP)
        elif a == 3:
            IP = input("\nEnter Victims IP (eg: - 192.168.1.1): ")
            fbs(IP)
        elif a==0:
            system('./scanning/main.py')
        print('\n\n')
        for i in tqdm(range(10)):
            time.sleep(.01)
        t2 = datetime.now()
        total = t2 - t1
        print("Scanning completed in: ", total)
        back=input("\n Do you want to scan again (y/n)")
        if back=='y' or back=='Y':
            system('./scanning/main.py')

    # Version Checking For specific Port
    def sbs(IP):
        s = socket.socket()
        s.settimeout(2)
        host = IP
        port = input("Enter Port: ")
        t1 = datetime.now()
        if s.connect_ex((host, int(port))):
            sbs(IP)
        else:
            print("\n\nport        status         service           version")
            Output.newline()
            nm = map.nmap.PortScanner()
            a = nm.scan(IP, port, arguments='-sV')
            serv = socket.getservbyport(int(port))
            ver = a.get('scan', {}).get(IP, {}).get('tcp', {}).get(int(port), {}).get('version')
            g = (f'{port}           open           {serv}              {ver}')
            print(g)
            Output.bdata(g)


    # Version Checking with Set of Port
    def rbs(IP):
        host = IP
        n1 = input("Enter starting port (eg: - 22): ")
        n2 = input("Enter Ending port (eg: - 100): ")
        t1 = datetime.now()
        print("\n\nport        status         service           version")
        Output.newline()
        try:
            for port in range(int(n1), int(n2)):
                s = socket.socket()
                s.settimeout(2)
                if s.connect_ex((host, int(port))):
                    pass
                else:
                    nm = map.nmap.PortScanner()
                    a = nm.scan(IP, str(port), arguments='-sV')
                    serv = socket.getservbyport(int(port))
                    ver = a.get('scan', {}).get(IP, {}).get('tcp', {}).get(int(port), {}).get('version')
                    g = (f'{port}           open           {serv}              {ver}')
                    print(g)
                    Output.bdata(g)
        except TimeoutError:
            print("Timeout retry")


    # Version Checking All Port
    def fbs(IP):
        host = IP
        t1 = datetime.now()
        print("\n\nport        status         service           version")
        Output.newline()
        try:
            for port in range(1, 65535):
                s = socket.socket()
                s.settimeout(2)
                if s.connect_ex((host, int(port))):
                    pass
                else:
                    nm = map.nmap.PortScanner()
                    a = nm.scan(IP, str(port), arguments='-sV')
                    serv = socket.getservbyport(int(port))
                    ver = a.get('scan', {}).get(IP, {}).get('tcp', {}).get(int(port), {}).get('version')
                    g = (f'{port}           open           {serv}              {ver}')
                    print(g)
                    Output.bdata(g)

        except TimeoutError:
            print("Timeout retry")


    # cve Scaning with an IP
    def cve_scan():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner'), 'green')
        t1 = datetime.now()
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        IP = str(input("\n\nEnter the Ip you want to scan for cves (eg: - 192.168.1.1):  "))
        nm = map.nmap.PortScanner()
        result = nm.scan(hosts=IP, arguments='-p 1-1000 -Pn  -sV --script vuln')
        p = colored('+', 'red')
        Output.newline()
        for i in result['scan'][IP]['hostscript']:
            Output.cdata(i)
            print('\n', p, i)
        print('\n\n')
        for i in tqdm(range(10), 'Scanning in Progress', colour='red'):
            time.sleep(.1)
        t2 = datetime.now()
        total = t2 - t1
        print("Scanning completed in: ", total)
        back = input("Do you want scan again (y/n): ")
        if back=='y' or back=='Y':
            system('./scanning/main.py')

    # Script scan with an IP
    def scriptscan():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner'), 'green')
        t1 = datetime.now()
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        IP = str(input("\n\nEnter the IP for script scan (eg: - 192.168.1.1):  "))
        nm = map.nmap.PortScanner()
        p = colored("+", "green")
        result = nm.scan(hosts=IP, arguments='-p 1-1024 -sC')
        for i in result['scan'][IP]['hostscript']:
            print('\n', p, i)
            Output.cdata(i)
        print('\n\n')
        for i in tqdm(range(10), 'Scanning in Progress', colour='red'):
            time.sleep(.1)
        t2 = datetime.now()
        total = t2 - t1
        print("Scanning completed in: ", total)
        back = input("Do you want scan again (y/n): ")
        if back=='y' or back=='Y':
            system('./scanning/main.py')

    # WebScan Used to gather website data
    def webscan():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner3'), 'blue')
        t1 = datetime.now()
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        print("Choose option: \n\n 1. Website Techology Scan \n\n 2. Website Whois Lookup \n\n Enter 0 to back")
        a = int(input("\nEnter here: "))
        if (a == 1):
            tlook()
        elif (a == 2):
            wlook()
        elif a==0:
            system('./scanning/main.py')
        print('\n\n')
        for i in tqdm(range(10)):
            time.sleep(.01)
        t2 = datetime.now()
        total = t2 - t1
        print("Scanning completed in: ", total)

        back = input("Do you want scan again (y/n): ")
        if back=='y' or back=='Y':
            system('./scanning/main.py')
    # Technology Scan
    def tlook():
        url = (input("Enter URL (eg: - http://google.com): "))
        a = builtwith.parse(url)
        Output.newline()
        print('\n\n')
        for key, value in a.items():
            Output.tdata(key, value)
            print(key, ":", ", ".join(value))


    # Whois Lookup
    def wlook():
        host = input("Enter a host (eg: - google.com): ")
        a = wlookup.whois(host)
        Output.wldata(a)
        print('\n', a)
except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./scanning/main.py')

    else:
        print("Exiting...")
except:
    print("Unexpected error occured try again")
