#!/usr/bin/python

from os import system,name
import os
if name=='nt':
	if os.path.exists('a.vbs'):
		system('cscript a.vbs')
		print("Message has been sent")
	
	else:
		system('type nul > a.vbs')
		print('Enter msg to victim (Eg: msgbox "type msg") and enter "CTRL+C"')
		system('copy con a.vbs')
		
else:
	print('OS is not support for this action')
