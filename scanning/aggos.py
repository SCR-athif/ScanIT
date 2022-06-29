#!/usr/bin/python3

#importing modules
import aggressive
from scapy.layers.inet import IP, ICMP, sr1
from os import system

try:
    # find os and redirect to aggressive
    system('clear')
    os = ''
    target = input("Enter the Ip address or Host: ")
    pack = IP(dst=target) / ICMP()
    resp = sr1(pack, timeout=3)
    if resp:
        if IP in resp:
            ttl = resp.getlayer(IP).ttl
            if ttl <= 64:
                print(ttl)
                os = 'Linux'
                aggressive
            elif ttl > 64:
                os = 'Windows'
                s = os
                aggressive
            else:
                print('Not Found')
except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./scanning/aggos.py')
    else:
        system('./scanning/main.py')
except:
    print("Unexpected error occured try again")

