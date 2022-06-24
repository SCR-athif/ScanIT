#!/usr/bin/python3
#functions to save scanning data into a txt file
try:
    def newline():
        with open("history.txt", "a") as m:
            for i in range(100):
                m.write("-")
            m.write("\nnew scan\n")
            for i in range(100):
                m.write("-")


    def dosdata(a, b):
        with open("history.txt", "a") as m:
            m.write(f"\nDos Attack into {a} for {b} times\n")


except:
    print("Unexpected error occured try again")