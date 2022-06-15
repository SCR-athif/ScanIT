#!/usr/bin/python3
import os
import time
import pyfiglet
import datetime

import Output
import scan
from termcolor import colored

print('-'*65)
scanit=colored(pyfiglet.figlet_format("S c a n I T"),'cyan')
for i in scanit:
    print(i,end='')
    time.sleep(.001)
print('-'*60)
date=datetime.datetime.now()
print("date",date.date())
print("time",date.time())
print('-'*60,"\n")


print("Choose option: \n 1. Simple Port Scan \n 2. Web Scanning \n 3. Version Scanning")
a=int(input("Enter here: "))

if (a==1):
    scan.portscan()
elif (a==2):
    scan.webscan()
elif (a==3):
    scan.version()
else:
    print("Wrong Entry")
