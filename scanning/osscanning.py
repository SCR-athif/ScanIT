#!/usr/bin/python3

#importing Module 
import Output
from scapy.layers.inet import IP, ICMP, sr1
from os import system
from package import map
try:
    system('clear')
    # program to find OS in a network
    target = input("Enter the Ip address or Host: ")
    nm = map.nmap.PortScanner()
    if '/24' in target:
        nm.scan(hosts=target, arguments='-n -sP')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        Output.newline()

        for host in hosts_list:
            t=host[0]
            os = ''
            pack = IP(dst=t) / ICMP()
            resp = sr1(pack, timeout=3)
            if resp:
                if IP in resp:
                    ttl = resp.getlayer(IP).ttl
                    if ttl <= 64:
                        print(ttl)
                        os = 'Linux'
                    elif ttl > 64:
                        os = 'Windows'
                    else:
                        print('Not Found')
                    print('-'*100)
                    a = f'\n\n*{t} : {os}* Operating System is Detected \n\n'
                    Output.osdata(a)
                    print(a)
                    print('-'*100)
                    print('\n\n')
        back = input("Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./scanning/osscanning.py')

    else:

        os = ''
        pack = IP(dst=target) / ICMP()
        resp = sr1(pack, timeout=3)
        if resp:
            if IP in resp:
                ttl = resp.getlayer(IP).ttl
                if ttl <= 64:
                    print(ttl)
                    os = 'Linux'
                elif ttl > 64:
                    os = 'Windows'
                else:
                    print('Not Found')
                a = f'\n\n*{target} : {os}* Operating System is Detected \n\n'
                Output.newline()
                Output.osdata(a)
                print(a)
        back = input("Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./scanning/osscanning.py')
except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./scanning/osscanning.py')
    else:
        system('./scanning/main.py')
