#!/usr/bin/python3

#module import
import time
import pyfiglet
import datetime
import gain
from os import system
from termcolor import colored

# Title Portion
system('clear')	#clears the screen
print('-'*60)
scanit = colored(pyfiglet.figlet_format("S c a n I T",'arrows'), 'cyan')
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
    1. DOS attack
    2. Eternal Blue
    3. Host Server
    4. RDP connection
    
    
    Enter 0 to main menu
"""

print(a)
try:
    a = int(input("Enter here: "))
    if a==1:
        gain.dos()
    elif a==2:
        system('clear')
        ip = input("Enter victim ip (eg:- 192.168.1.1): ")
        system('./Attacking/blue.py '+ip)
    if a==3:
        gain.server()
    if a==4:
        gain.rdp()
    elif a==0:
        system('./main.py')
    else:
        print("Wrong Entry")

except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./Attacking/main.py')
    else:
        system('./main.py')
except TypeError:
    print("Invalid Type   Exiting....")
except:
    print("Unexpected error occured try again")