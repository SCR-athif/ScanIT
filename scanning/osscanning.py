#!/usr/bin/python

import Output
import scapy.all as scapy
from scapy.layers.inet import IP, ICMP
from termcolor import colored
from os import system

try:
    system('clear')

    def createPacket(ip):
        arp_request = scapy.ARP(pdst=ip)  # create a ARP request object by scapy
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # We have set the destination
        arp_request_broadcast = broadcast / arp_request
        return (arp_request_broadcast)


    def transmitPacket(packet):
        success_list, failure_list = scapy.srp(packet, timeout=2)
        return success_list


    def getOS(ip_addr):
        ttl_values = {32: "Windows", 60: "MAC OS", 64: "Linux", 128: "Windows", 255: "Linux 2.4 Kernal"}
        ans = scapy.sr1(IP(dst=str(ip_addr)) / ICMP(), timeout=2, verbose=0)

        if ans:
            if ans.ttl in ttl_values:
                return ttl_values.get(ans.ttl)
            else:
                return "OS detection blocked"
        else:
            return "Packets transmitting failed"


    def parseResponse(success_list):
        targets = []
        for success in success_list:
            entry = {'ip': success[1].psrc, 'mac': success[1].hwsrc}
            targets.append(entry)
        return targets


    def print_analysis(element_entries):
        Output.newline()
        h = colored("\nIP\t\t\tMAC Address\t\t\tOPERATING SYSTEM", 'red')
        print(h)
        Output.osdata(h)
        print("." * 100)
        for element in entries:
            a = colored("\n" + element["ip"] + "\t\t" + element['mac'] + "\t\t" + getOS(element["ip"]) + "\n", 'white')
            Output.osdata(a)
            print(a)

        back = input("\n\nDo you want scan again (Y/N): ")
        if back == 'y' or back == 'Y':
            system('./scanning/osscanning.py')
        else:
            system('./scanning/main.py')


    options = input("Enter IP or Host (eg:- 192.168.1.1) : ")

    if options is not None:
        broadcast_packets = createPacket(options)
        success_packets = transmitPacket(broadcast_packets)
        entries = parseResponse(success_packets)
        print_analysis(entries)

except KeyboardInterrupt:
    print("\n\n")
    back = input("Do you want to EXIT (y/n): ")
    if back == 'n' or back == 'N':
        system('./scanning/osscanning.py')

    else:
        system('./scanning/main.py')

