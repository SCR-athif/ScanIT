#!/usr/bin/python3
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil
#graph
try:
    frame_len = 200
    y = []
    fig = plt.figure(figsize=(6,2))


    def animation(i):
        y.append(psutil.cpu_percent())
        if len(y) <= frame_len:
            plt.cla()
            plt.plot(y, 'r', label='CPU usage(%)')
        else:
            plt.cla()
            plt.plot(y[-frame_len:], 'r', label='cpu usage(%)')
        plt.xlabel('Time (s)')
        plt.ylabel('CPU usage(%)')
        plt.title("REAL-TIME CPU Usage in percentage")
        plt.legend(loc='upper right')


    animate = FuncAnimation(plt.gcf(), animation, interval=1000)
    plt.show()
except KeyboardInterrupt:
    print("Ctrl + C Entered. Exiting....")
except:
    print("Unexpected error occured try again")