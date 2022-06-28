#!/usr/bin/python3

#importing module
import socket
import time
import pyfiglet
import dataos
import Output
import requests
from datetime import datetime
from tqdm import tqdm
from os import system
from termcolor import colored
try:
    # data gathering function
    def func(oper):
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner'), 'green')
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        p = colored('+', 'red')
        IP = dataos.target
        print('\n\n This may more time that expected, Sit back and relax :)')
        print('\n\n', p, 'OS : ', oper)
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

        # code for get location of IP
        def get_location():
            ip_address = (dataos.target)
            response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
            location_data = {
                "ip": ip_address,
                "city": response.get("city"),
                "region": response.get("region"),
                "country": response.get("country_name")
            }
            print('\n\n')
            for key, value in location_data.items():
                print(key, ':', value)

        # code for get location of IP
        get_location()


    # if os is windows ruun this part
    if dataos.os == 'Windows':
        oper = 'Windows'
        func(oper)
        print('\n\n')
        IP = dataos.target
        nm = map.nmap.PortScanner()
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
            system('./recon/main.py')
        exit()
    # if os is linux Runs this part
    elif dataos.os == 'Linux':
        oper = 'Linux'
        func(oper)
        print("\n\n")
        for i in tqdm(range(10), 'Scanning success', colour='green'):
            time.sleep(.1)
        back = input("Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./recon/main.py')
        exit()
except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./recon/main.py')
    else:
        print("Exiting...")
except:
    print("Unexpected error try again")