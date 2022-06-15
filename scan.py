#!/usr/bin/python3
import socket
import Output
import builtwith
import whois

def rpt():
    IP = input('Enter victims IP: ')
    n1 = int(input('starting port '))
    n2 = int(input('Ending port '))
    try:
        Output.newline()
        for port in range(n1, n2):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            if s.connect_ex((IP, port)):
                Output.ptclose(IP,port)
                pass
            else:
                Output.ptopen(IP,port)
                print("port ",port,"is open")

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
        if s.connect_ex((IP, int(port))):
            Output.ptclose(IP, port)
            print("port",port,"is closed")
            spt(IP)
        else:
            Output.ptopen(IP, port)
            print("port",port,"is open")

    except KeyboardInterrupt:
        print("unwanted input")

    except socket.gaierror:
        print('Hostname seems down')

    except socket.error:
        print("Couldn't connect to server")
def portscan():
    print("Choose option: \n 1. Single Entry \n 2. Range Entry")
    a=int(input("Enter here: "))
    if (a==1):
        IP = input('Enter victims IP: ')
        Output.newline()
        spt(IP)
    elif (a==2):
        rpt()


def tlook():
    url=(input("Enter URL: "))
    a=builtwith.parse(url)
    Output.newline()
    for key,value in a.items():
        Output.tdata(key,value)
        print(key,":",", ".join(value))
def wlook(q):
    a=whois.whois(q)
    a.server
    a.state
    Output.wldata(a)
    return a
def webscan():
    print("Choose option: \n 1. Website Techology Scan \n 2. Website Whois Lookup")
    a = int(input("Enter here: "))
    if (a==1):
        tlook()
    elif (a==2):
        print(wlook(input("Enter Domian: ")))

def version():
    IP = input("Enter Victims IP:")
    print("Choose option: \n 1. Version scanning with range entry \n 2. Version Scanning with single entry")
    a=int(input("Enter your option: "))
    if (a==2):
        sbs(IP)
    elif (a==1):
        rbs(IP)
def sbs(IP):
    s = socket.socket()
    s.settimeout(5)
    host = IP
    port = input("Enter Port: ")
    if s.connect_ex((host, int(port))):
        sbs(IP)
    else:
        Output.newline()
        a = str("port {} is open\n\t version and service running or port {} : {}".format(port, port, s.recv(1024)))
        print(a)
        Output.bdata(a)
def rbs(IP):
    host = IP
    n1 = input("Enter starting port: ")
    n2 = input("Enter Ending port: ")
    Output.newline()
    for port in range(int(n1), int(n2)):
        s = socket.socket()
        s.settimeout(5)
        if s.connect_ex((host, int(port))):
            pass
        else:
            a=str("port {} is open\n\t version and service running or port {} : {}\n".format(port,port,s.recv(1024)))
            print(a)
            Output.bdata(a)

