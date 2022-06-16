#!/usr/bin/python3
import socket
import Output
import builtwith
import whois
import pyfiglet
import datetime
from termcolor import colored
from scapy.all import *
from scapy.layers.inet import IP, ICMP
from os import system

def portscan():                                                         #port scan
    system('clear')
    print("-" * 60)
    txt=colored(pyfiglet.figlet_format("ScanIT", 'banner'), 'red')
    for i in txt:
        print(i, end='')
        time.sleep(.001)
    print("-" * 60)
    print("Choose option: \n 1. Single Entry \n 2. Range Entry")
    a=int(input("Enter here: "))
    if a==1:
        IP = input('Enter victims IP: ')
        Output.newline()
        spt(IP)
    elif a==2:
        rpt()


def rpt():
    IP = input('Enter victims IP: ')
    n1 = int(input('starting port '))
    n2 = int(input('Ending port '))
    try:
        Output.newline()
        print('port     Status       service')
        for port in range(n1, n2):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            if s.connect_ex((IP, port)):
                pass
            else:
                serv=socket.getservbyport(int(port))
                Output.ptopen(IP,port,serv)
                print(f"{port}         open       {serv}")

    except KeyboardInterrupt:
        print("unwanted input")

    except socket.gaierror:
        print('Hostname seems down')

    except socket.error:
        print("Couldn't connect to server")


def spt(IP):
    try:
        port=str(input("Enter your port "))
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        print('port     Status       service')
        if s.connect_ex((IP, int(port))):
            Output.ptclose(IP, port)
            print(f"{port}         close")
            spt(IP)
        else:
            serv = socket.getservbyport(int(port))
            Output.ptopen(IP, port, serv)
            print(f"{port}         open       {serv}")

    except KeyboardInterrupt:
        print("unwanted input")

    except socket.gaierror:
        print('Hostname seems down')

    except socket.error:
        print("Couldn't connect to server")


def webscan():                                                                      #webscan
    system('clear')
    print("-" * 60)
    txt=colored(pyfiglet.figlet_format("ScanIT", 'banner'), 'green')
    for i in txt:
        print(i, end='')
        time.sleep(.001)
    print("-" * 60)
    print("Choose option: \n 1. Website Techology Scan \n 2. Website Whois Lookup")
    a = int(input("Enter here: "))
    if (a==1):
        tlook()
    elif (a==2):
        wlook()


def tlook():
    url = (input("Enter URL: "))
    a = builtwith.parse(url)
    Output.newline()
    for key, value in a.items():
        Output.tdata(key, value)
        print(key, ":", ", ".join(value))


def wlook():
    host = input("Enter a host: ")
    a=whois(host)
    Output.wldata(a)
    print(a)


def version():                                                                                      #version scanning
    system('clear')
    print("-" * 60)
    txt=colored(pyfiglet.figlet_format("S c a n I T",'arrows'),'blue')
    for i in txt:
        print(i, end='')
        time.sleep(.001)
    print("-" * 60)
    IP = input("Enter Victims IP:")
    print("Choose option: \n 1. Version scanning with range entry \n 2. Version Scanning with single entry")
    a=int(input("Enter your option: "))
    if (a==2):
        sbs(IP)
    elif (a==1):
        rbs(IP)


def sbs(IP):
    s = socket.socket()
    host = IP
    port = input("Enter Port: ")
    if s.connect_ex((host, int(port))):
        sbs(IP)
    else:
        Output.newline()
        if s.settimeout(5):
            print("service scanning is not possible")
        else:
            a = str("port {} is open\n\t version and service running or port {} : {}".format(port, port, socket.getservbyport(int(port))))
            print(a)
            Output.bdata(a)


def rbs(IP):
    host = IP
    n1 = input("Enter starting port: ")
    n2 = input("Enter Ending port: ")
    Output.newline()
    try:
        for port in range(int(n1), int(n2)):
            s = socket.socket()
            s.settimeout(5)
            if s.connect_ex((host, int(port))):
                pass
            else:
                a = str("port {} is open\n\t version and service running or port {} : {}\n".format(port, port, s.recv(1024)))
                print(a)
                Output.bdata(a)
    except TimeoutError:
        print("Timeout retry")

def osscanning():                                                   #os detection scannin
    system('clear')
    print("-" * 60)
    txt=colored(pyfiglet.figlet_format("S c a n I T"), 'yellow')
    for i in txt:
        print(i, end='')
        time.sleep(.001)
    print("-" * 60)
    os = ''
    target = input("Enter the Ip address:")
    pack = IP(dst=target) / ICMP()
    resp = sr1(pack, timeout=3)
    if resp:
        if IP in resp:
            ttl = resp.getlayer(IP).ttl
            if ttl <= 64:
                print(ttl)
                os = 'Linux'
            elif ttl > 64:
                os = 'Windows'
            else:
                print('Not Found')
            a = f'\n\nTTL = {ttl} \n*{os}* Operating System is Detected \n\n'
            Output.osdata(a)
            print(a)


def Total():
    system('clear')
    print("-" * 60)
    txt = colored(pyfiglet.figlet_format("S c a n I T", 'arrows'), 'blue')
    for i in txt:
        print(i, end='')
        time.sleep(.001)
    print("-" * 60)
    net = input("Enter the IP address: ")
    net1 = net.split('.')
    a = '.'
    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = int(input("Starting host: "))
    en1 = int(input("Enting host: "))
    en1 = en1 + 1
    t1 = datetime.now()

    def sscan(addr):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr, int(port)))
        if result == 0:
            return 1
        else:
            return 0

    def rscan(addr, aport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.01)
        result = s.connect_ex((addr, int(aport)))
        if result == 0:
            return 1
        else:
            return 0

    def run1():
        print('Choose option:\n 1. Scan with one port \n 2. Scan with range of port: ')
        a = int(input("Enter here: "))
        if (a == 1):
            global port
            port = input("Enter port number :")
            for ip in range(st1, en1):
                addr = net2 + str(ip)
                if (sscan(addr)):
                    print(addr, "is up")
        elif (a == 2):
            n1 = input("Enter starting range:")
            n2 = input("Enter ending range:")
            for ip in range(st1, en1):
                addr = net2 + str(ip)
                for port1 in range(int(n1), int(n2)):
                    if (rscan(addr, port1)):
                        print(addr, "is up")

    run1()
    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in: ", total)

