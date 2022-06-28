#!/usr/bin/python3

#module import
import time
import pyfiglet
import datetime
import scan
from os import system
from termcolor import colored

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
    1. Live host hunt
    2. OS Detection Scan
    3. Simple Port Scan
    4. Version Scan
    5. Aggressive Scanning 
    6. Host Max Data Gathering 
    7. CVE scan 
    8. Script Scan
    9. Web Scan
    
    Enter 0 to Main Menu
"""

print(a)
try:
    a = int(input("Enter here: "))
    if a==3:
        scan.portscan()
    elif a==1:
        scan.Total()
    elif a==4:
        scan.version()
    elif a==2:
    	#Runs OSscanning With sudo previlage
        system('sudo ./scanning/osscanning.py')
    elif a==5:
    	#Runs aggressive scan With sudo previlage
        system('sudo ./scanning/aggos.py')
    elif a==6:
    	#Runs datagathering With sudo previlage
        system('sudo ./scanning/dataos.py')
    elif a==7:
        scan.cve_scan()
    elif a==8:
	    scan.scriptscan()
    elif a==9:
        scan.webscan()
    elif a==0:
        system('./main.py')
    else:
        print("Wrong Entry")

except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./scanning/main.py')

    else:
        print("Exiting...")
except TypeError:
    print("Invalid Type   Exiting....")
except:
    print("Unexpected error occured try again")