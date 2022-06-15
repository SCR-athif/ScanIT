#!/usr/bin/python3

def ptopen(IP,port):
    with open("history.txt", "a") as m:
        m.write("\n{} {} {} {}\n".format(IP, ':port', port, 'is open'))
def ptclose(IP,port):
    with open("history.txt", "a") as m:
        m.write("\n{} {} {} {}\n".format(IP, ':port', port, 'is closed'))
def newline():
    with open("history.txt", "a") as m:
        for i in range(100):
            m.write("-")
        m.write("\nnew scan\n")
        for i in range(100):
            m.write("-")
def tdata(key,value):
    with open("history.txt","a") as m:\
        m.write('\n{} {} {}\n'.format(key,":",", ".join(value)))
def wldata(a):
    with open("history.txt","a") as m:
        for i in range(100):
            m.write("-")
        m.write("\nnew scan\n")
        for i in range(100):
            m.write("-")
        m.write('\n{}\n'.format(a))
def bdata(a):
    with open("history.txt", "a") as m:
        m.write('\n{}\n'.format(a))
