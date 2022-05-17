import socket
import sys
import re
from datetime import datetime
import time
import numpy as np
import pandas as pd

# read file to extract IP and connections
with open('address/address.txt') as fh:
    fstring = fh.readlines()

# declaring the regex pattern for IP addresses
pattern_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# initializing the list object
UDP_IP = pattern_ip.search(fstring[0])[0] # find ip
UDP_PORT = int(re.findall('[0-9]+', fstring[1])[0]) # find port num

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program !!")
print("\nConnecting to:\n",f"IP: {UDP_IP}\n Port: {UDP_PORT}\n" )

# start UDP 
# (type msg > collect time > send > recv > collect time > output elapsed time)
STARTTIME = time.time()
timestamps = []
for i in range(0,50):
    # send data
    send_data ="A"
    SENDTIME  = time.time()
    s.sendto(send_data.encode('utf-8'), (UDP_IP, UDP_PORT))
    ELAPSEDTIME   = (SENDTIME - STARTTIME) # return time in ms
    timestamps.append(ELAPSEDTIME)
    print(f"{i} : ", send_data)
    print(ELAPSEDTIME)
    time.sleep(0.2)
# close the socket
print("saving to csv...")


filename = datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ".xlsx" # file with today's datetime
filename = re.sub(r"\s",'_',filename) # sub any whitespace with underscore
filename = re.sub(r":",'-',filename) # HH:MM:SS in .csv name causes github fetch request error
arr = np.asarray(timestamps) # HH:MM:SS in .csv name causes github fetch request error
pd.DataFrame(arr).to_excel(filename,index=False)
s.close()