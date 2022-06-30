#!/usr/bin/python3

#importing modules
import socket
from package import map
import time
from tqdm import tqdm
from os import system
from termcolor import colored
import pyfiglet
import aggos
import Output
from datetime import datetime

try:
    # function for version, service and port status
    def func(oper):
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner'), 'blue')
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        p = colored('+', 'red')
        IP = aggos.target
        Output.newline()
        Output.adata(aggos.os)
        print('\n\n This may more time that expected, Sit back and relax :)')
        print('\n\n', p, 'OS :', oper)
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


    # if os is windows run this part
    if aggos.os == 'Windows':
        oper = 'Windows'
        func(oper)
        print('\n\n')
        nm = map.nmap.PortScanner()
        IP = aggos.target
        result = nm.scan(hosts=IP, arguments='-p 1-1000 -Pn  -sV --script vuln')
        p = colored('+', 'red')
        Output.newline()
        for i in result['scan'][IP]['hostscript']:
            Output.cdata(i)
            print('\n', p, i)
        print('\n\n')
        for i in tqdm(range(10), 'Scanning success', colour='green'):
            time.sleep(.1)
        back = input("Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./scanning/main.py')
        exit()
    # if os is windows run this part
    elif aggos.os == 'Linux':
        oper = 'Linux'
        func(oper)
        print('\n\n')
        for i in tqdm(range(10), 'Scanning success', colour='green'):
            time.sleep(.1)
        back = input("Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./scanning/main.py')
        exit()
except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./scanning/aggos.py')
    else:
        system('./scanning/main.py')
except:
    print("Unexpected error occured try again")
