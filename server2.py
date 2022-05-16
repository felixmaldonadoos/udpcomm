import sys
import re
import socket
import time

# read file to extract IP and connections
with open('address.txt') as fh:
    fstring = fh.readlines()
# declaring the regex pattern for IP addresses
pattern_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
# initializing the list object
UDP_IP = pattern_ip.search(fstring[0])[0] # find ip
UDP_PORT = int(re.findall('[0-9]+', fstring[1])[0]) # find port num
# Create a UDP socket
print(f"IP: {UDP_IP}\nPort: {UDP_PORT}" )
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (UDP_IP, UDP_PORT)
while True:
    print("####### Server is listening #######")
    data, address = s.recvfrom(4096)
    RECVTIME = time.time()
    # print recvd data
    print("\n 2. Server received: ", data.decode('utf-8'), "\n")
    # send back same packet to confirm. 
    #s.sendto(data, address)
    ELAPSEDTIME = round((time.time() - RECVTIME)*(10**3),4) # return time in ms
    print("\n 1. Server sent : ", data,"\n")