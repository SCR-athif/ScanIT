#!/usr/bin/python3
try:
    # functions to save scanning data into a txt file
    def ptopen(IP, port, ser):
        with open("history.txt", "a") as m:
            m.write("\n{} {} {} {} {} {}\n".format(IP, ':port', port, 'is open', ":", ser))


    def ptclose(IP, port):
        with open("history.txt", "a") as m:
            m.write("\n{} {} {} {}\n".format(IP, ':port', port, 'is closed'))


    def newline():
        with open("history.txt", "a") as m:
            for i in range(100):
                m.write("-")
            m.write("\nnew scan\n")
            for i in range(100):
                m.write("-")


    def tdata(key, value):
        with open("history.txt", "a") as m: \
                m.write('\n{} {} {}\n'.format(key, ":", ", ".join(value)))


    def wldata(a):
        with open("history.txt", "a") as m:
            for i in range(100):
                m.write("-")
            m.write("\nnew scan\n")
            for i in range(100):
                m.write("-")
            m.write('\n{}\n'.format(a))


    def bdata(a):
        with open("history.txt", "a") as m:
            m.write('\n{}\n'.format(a))


    def osdata(a):
        with open("history.txt", "a") as m:
            m.write(f'{a}')

    def fdata(a, b):
        with open("history.txt", "a") as m:
            m.write(f'\n{a} is {b} \n')


    def total(a):
        with open("history.txt", "a") as m:
            m.write(f'\n{a} is up\n')


    def cdata(a):
        with open("history.txt", "a") as m:
            m.write(f"\n{a}\n")


    def adata(a):
        with open("history.txt", "a") as m:
            m.write(f"\n{a}\n")


    def gdata(a):
        with open("history.txt", "a") as m:
            m.write(f"\n{a}\n")
except:
    print("Unexpected error occured try again")