#!/usr/bin/python3

#importing Module 
import Output
from scapy.layers.inet import IP, ICMP, sr1
from os import system

try:
    system('clear')
    # program to find OS in a network
    target = input("Enter the Ip address or Host: ")
    if '/24' in target:
        pass
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
                a = f'\n\n*{os}* Operating System is Detected \n\n'
                Output.osdata(a)
                print(a)
        back = input("Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./scanning/main.py')
except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./scanning/osscanning.py')
    else:
        print("Exiting...")
except:
    print("Unexpected error occured try again")