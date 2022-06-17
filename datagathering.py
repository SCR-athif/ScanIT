#!/usr/bin/python3
import socket
import map
import time
from tqdm import tqdm
from os import system
from termcolor import colored
import pyfiglet
import dataos
import Output
from datetime import datetime


if dataos.os=='Windows':
    system('clear')
    print("-" * 60)
    txt = colored(pyfiglet.figlet_format("ScanIT", 'banner4'), 'green')
    for i in txt:
        print(i, end='')
        time.sleep(.001)
    print("-" * 60)
    p=colored('+','red')
    t1 = datetime.now
    IP = dataos.target
    Output.newline()
    Output.adata(dataos.os)
    print('\n\n',p,'OS : Windows')
    print("\n\nport        status         service           version")
    for port in range(1, 1024):
        s = socket.socket()
        s.settimeout(5)
        if s.connect_ex((IP, int(port))):
            pass
        else:
            nm = map.nmap.PortScanner()
            a = nm.scan(IP, str(port), arguments='-sV')
            serv = socket.getservbyport(int(port))
            ver = a.get('scan', {}).get(IP, {}).get('tcp', {}).get(int(port), {}).get('version')
            g = (f'{port}           open           {serv}              {ver}')
            print(g)
            Output.gdata(g)
    print('\n\n')


    result = nm.scan(hosts=IP, arguments='-p 1-1000 -Pn  -sV --script vuln')
    p = colored('+', 'red')
    Output.newline()
    for i in result['scan'][IP]['hostscript']:
        Output.cdata(i)
        print('\n', p, i)

    print('\n\n')
    for i in tqdm(range(10), 'Scanning success', colour='green'):
        time.sleep(.1)

    exit()

elif dataos.os=='Linux':

    system('clear')
    print("-" * 60)
    txt = colored(pyfiglet.figlet_format("ScanIT", 'banner'), 'green')
    for i in txt:
        print(i, end='')
        time.sleep(.001)
    print("-" * 60)
    p = colored('+', 'red')
    IP = dataos.target
    print('\n\n',p,'OS : Linux')
    Output.newline()
    Output.adata(dataos.os)
    print("\n\nport        status         service           version")
    for port in range(1, 1024):
        s = socket.socket()
        s.settimeout(5)
        if s.connect_ex((IP, int(port))):
            pass
        else:
            nm = map.nmap.PortScanner()
            a = nm.scan(IP, str(port), arguments='-sV')
            serv = socket.getservbyport(int(port))
            ver = a.get('scan', {}).get(IP, {}).get('tcp', {}).get(int(port), {}).get('version')
            g = (f'{port}           open           {serv}              {ver}')
            print(g)
            Output.gdata(g)
    print('\n\n')
    for i in tqdm(range(10),'Scanning success',colour='green'):
        time.sleep(.1)
    exit()

