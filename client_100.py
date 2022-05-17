from http.client import ImproperConnectionState
from os import times
import socket
import sys
import re
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
for i in range(0,100):
    # start at 0
    # send data
    send_data = ("A")
    SENDTIME  = time.time()
    s.sendto(send_data.encode('utf-8'), (UDP_IP, UDP_PORT))
    print(f"{i}.", send_data)

    ELAPSEDTIME   = round((SENDTIME - STARTTIME)*(10**3),4) # return time in ms
    print(f"time to send and recieve: {ELAPSEDTIME} ms\n")
    timestamps.append(ELAPSEDTIME)
    time.sleep(0.5)

print("saving..")
pd.DataFrame(np.asarray(timestamps)).to_excel("data/testdata.xlsx",index = False)
np.savetxt(np.asarray(timestamps))
# close the socket
s.close()