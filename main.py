#!/usr/bin/python3

#module import
import time
import pyfiglet
import datetime
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
    1. Reconnaissance
    2. Scan
    3. Gain Access
"""

print(a)
try:
    a = int(input("Enter here: "))
    if a==1:
        system('./recon/main.py')
    elif a==2:
        system('./scanning/main.py')
    elif a==3:
        system('./Attacking/main.py')
    else:
        print("Wrong Entry")

except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./main.py')

    else:
        print("Exiting...")
except TypeError:
    print("Invalid Type   Exiting....")
except:
    print("Unexpected error occured try again")
