#!/usr/bin/python3

import time
import pyfiglet
import datetime
import scan
from termcolor import colored


print('-'*60)
scanit = colored(pyfiglet.figlet_format("S c a n I T"), 'cyan')
for i in scanit:
    print(i, end='')
    time.sleep(.001)

print('-'*60)
date = datetime.datetime.now()
print("date", date.date())
print("time", date.time())
print('-'*60, "\n")

print("Choose option: \n 1. Simple Port Scan \n 2. Web Scanning \n 3. Version Scanning \n 4. OS Scanning \n 5. Total Hosts finding")
try:
    a = int(input("Enter here: "))
    if a == 1:
        scan.portscan()
    elif a == 2:
        scan.webscan()
    elif a == 3:
        scan.version()
    elif a == 4:
        scan.sudo()
    elif a == 5:
        scan.Total()
    else:
        print("Wrong Entry")

except KeyboardInterrupt:
    print("unwanted input. Exiting...")
