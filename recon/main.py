#!/usr/bin/python3

#module import
import time
import pyfiglet
import datetime
import gather
from os import system
from termcolor import colored

# Title Portion
system('clear')	#clears the screen
print('-'*60)
scanit = colored(pyfiglet.figlet_format("S c a n I T",'3-d'), 'cyan')
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
    1. Web Scan
    2. Data-gathering
    
    Enter 0 to main menu
"""

print(a)
try:
    a = int(input("Enter here: "))
    if a==1:
        gather.webscan()
    elif a==2:
        system('sudo ./recon/dataos.py')
    elif a==0:
        system('./main.py')
    else:
        print("Wrong Entry")

except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./recon/main.py')

    else:
        print("Exiting...")
except TypeError:
    print("Invalid Type   Exiting....")
except:
    print("Unexpected error try again")