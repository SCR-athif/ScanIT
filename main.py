#!/usr/bin/python
import os
import time
import pyfiglet
import datetime

import Output
import scan
from termcolor import colored

print('-'*65)
scanit=colored(pyfiglet.figlet_format("S c a n I T",'arrows'),'cyan')
for i in scanit:
    print(i,end='')
    time.sleep(.001)
print('-'*60)
date=datetime.datetime.now()
print("date",date.date())
print("time",date.time())
print('-'*60,"\n")


print("Choose option: \n 1. Port scanning with range entry \n 2. Port Scanning with single entry \n 3. Website technology scanning \n 4. Website lookup\n 5. Version Scanning")
a=int(input("Enter here: "))

if (a==1):
    scan.rpt()
elif (a==2):
    IP = input('Enter victims IP: ')
    Output.newline()
    scan.spt(IP)
elif (a==3):
    scan.tlook()
elif (a==4):
    print(scan.wlook(input("Enter Domian: ")))
elif (a==5):
    scan.version()
else:
    print("Wrong Entry")
