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
    2. Datagathering
"""

print(a)
try:
    a = int(input("Enter here: "))
    if a==1:
        scan.portscan()
    elif a==2:
        gather.()
    else:
        print("Wrong Entry")

except KeyboardInterrupt:
    print("unwanted input. Exiting...")
except TypeError:
    print("Invalid Type   Exiting....")
