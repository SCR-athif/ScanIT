#!/usr/bin/python3

#module import
import time
import pyfiglet
import datetime
import scan
from os import system
from termcolor import colored
import os.path

if os.path.exists('Intro.py'):
    system('./Intro.py')
    system('rm Intro.py')
# Title Portion
system('clear')	#clears the screen
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


#options of Choosing scan method
a="""
Choose option:
    1. Simple Port Scan
    2. Live host hunt
    3. Version Scan
    4. OS Detection Scan
    5. Aggressive Scanning
    6. Host Max Data Gathering
    7. CVE scan
    8. Script Scan
    9. Web Scan
    10. Dos Attack
"""

print(a)
try:
    a = int(input("Enter here: "))
    if a==1:
        scan.portscan()
    elif a==2:
        scan.Total()
    elif a==3:
        scan.version()
    elif a==4:
        scan.sudo()
    elif a==5:
        scan.agg()
    elif a==6:
        scan.data()
    elif a==7:
        scan.cve_scan()
    elif a==8:
	    scan.scriptscan()
    elif a==9:
        scan.webscan()
    elif a==10:
        scan.dos()
    else:
        print("Wrong Entry")

except KeyboardInterrupt:
    print("unwanted input. Exiting...")
except TypeError:
    print("Invalid Type   Exiting....")
