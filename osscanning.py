#!/usr/bin/python3
import Output
from scapy.layers.inet import IP, ICMP, sr1
from os import system
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
        elif ttl > 64:
            os = 'Windows'
        else:
            print('Not Found')
        a = f'\n\n*{os}* Operating System is Detected \n\n'
        Output.osdata(a)
        print(a)

