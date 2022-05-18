import tkinter as tk
from tkinter import Tk, messagebox
from tkinter import ttk
import time
import numpy as np
import pandas as pd
import re
import socket
from datetime import datetime

class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=450, width=626)  # this is the background
        main_frame.pack(fill="both", expand="true")

        self.geometry("626x431")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen
        self.title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        self.text_styles = {"font": ("Verdana", 14),
                       "background": "blue",
                       "foreground": "#E1FFFF"}

        self.win_main = tk.Frame(main_frame, bg="blue", relief="groove", bd=2)  # this is the frame that holds all the login details and buttons
        self.win_main.place(rely=0.30, relx=0.17, height=225, width=400)

        # create labels
        self.label_title = tk.Label(self.win_main, self.title_styles, text="UDP Sender")
        self.label_title.grid(row=0, column=1, columnspan=1)

        label_IP = tk.Label(self.win_main, self.text_styles, text="IP:")
        label_IP.grid(row=1, column=0)

        label_PORT = tk.Label(self.win_main, self.text_styles, text="Port:")
        label_PORT.grid(row=2, column=0)

        label_MSG = tk.Label(self.win_main, self.text_styles, text="Message:")
        label_MSG.grid(row=3, column=0)

        label_NUM = tk.Label(self.win_main, self.text_styles, text="N (send):")
        label_NUM.grid(row=4, column=0)

        label_DELAY = tk.Label(self.win_main, self.text_styles, text="Delay (s):")
        label_DELAY.grid(row=5, column=0)

        # create entry cells (IP, port, msg, number of msgs)
        # assing self. to call values later 
        self.entry_IP = ttk.Entry(self.win_main, width=45, cursor="xterm")
        self.entry_IP.grid(row=1, column=1)

        self.entry_PORT = ttk.Entry(self.win_main, width=45, cursor="xterm")
        self.entry_PORT.grid(row=2, column=1)
        
        self.entry_MSG = ttk.Entry(self.win_main, width=45, cursor="xterm")
        self.entry_MSG.grid(row=3, column=1)

        self.entry_NUM = ttk.Entry(self.win_main, width=45, cursor="xterm")
        self.entry_NUM.grid(row=4, column=1)

        self.entry_DELAY = ttk.Entry(self.win_main, width=45, cursor="xterm")
        self.entry_DELAY.grid(row=5, column=1)

        # label to display information: 
        self.label_status=tk.Label(self.win_main, text="", font=("Courier 22 bold"))
        self.label_status.grid(row=6,column=1,columnspan=1)

        # button
        button = ttk.Button(self.win_main, text="Send", command=lambda: self.run())
        button.place(rely=0.70, relx=0.50)

    def run(self):
        self.gettarget()
        self.createsocket()
        self.sendpacket()

    def gettarget(self):
        # collect entry information
        self.IP = self.entry_IP.get()
        self.PORT = self.entry_PORT.get()
        self.NUM = self.entry_NUM.get()
        self.DELAY = self.entry_DELAY.get()
        self.MSG = self.entry_MSG.get()
        print(self.IP,self.PORT,self.NUM,self.DELAY)
        # self.display_info()
        return

    def createsocket(self):
        # Create socket for server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    def sendpacket(self):
        STARTTIME = time.time()
        self.imestamps = []
        for i in range(0,self.NUM):
            # send data
            SENDTIME  = time.time()
            self.s.sendto(self.MSG.encode('utf-8'), (self.UDP_IP, self.UDP_PORT))

            # save timestamp
            ELAPSEDTIME   = (SENDTIME - STARTTIME) # return time in ms
            self.timestamps.append(ELAPSEDTIME)
            print(f"{i}:", self.MSG, "time:", ELAPSEDTIME)
            time.sleep(0.2)
        
        self.savetocsv()
        return 

    def display_intro(self):
        # update menu
        string = "this is the intro string."
        self.label_title = tk.Label(self.win_main, self.title_styles, text=string)
    
    def display_info(self):
        string = f"Sending: {self.NUM} UDP packets to {self.IP}:{self.PORT} with time delay {self.DELAY} seconds "
        self.label_title = tk.Label(self.win_main, self.title_styles, text=string)

    def display_text(self,string):
        self.label_status.configure(text=string)

    def updategui(self):
        # call on a thread to check this every ms and update gui
        self.label_status.configure(text = "")

    def savetocsv(self,path = "data/"):
        filename = datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ".xlsx" # file with today's datetime
        filename = re.sub(r"\s",'_',filename) # sub any whitespace with underscore
        filename = re.sub(r":",'-',filename) # HH:MM:SS in .csv name causes github fetch request error
        filename = path + filename
        arr = np.asarray(self.timestamps) # HH:MM:SS in .csv name causes github fetch request error
        pd.DataFrame(arr).to_excel(filename,index=False)
        return 0

# top = App()
# top.title("Tkinter App Template - Login Page")
root = MyApp()
root.mainloop()
