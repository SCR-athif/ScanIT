#!/usr/bin/python3

#importing modules 
import socket
import Output
import builtwith
from package import wlookup
import pyfiglet
import time
from datetime import datetime
from os import system
from termcolor import colored
from tqdm import tqdm

try:
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
        print("Choose option: \n\n 1. Website Techology Scan \n\n 2. Website Whois Lookup")
        a = int(input("\nEnter here: "))
        if (a == 1):
            tlook()
        elif (a == 2):
            wlook()
        print('\n\n')
        for i in tqdm(range(10)):
            time.sleep(.01)
        t2 = datetime.now()
        total = t2 - t1
        print("Scanning completed in: ", total)
        back = input("Do you want scan again (y/n): ")
        if back == 'y' or back == 'Y':
            system('./recon/main.py')

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
        system('./recon/main.py')
    else:
        print("Exiting...")
except:
    print("Unexpected error try again")