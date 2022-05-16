import socket
import sys
import re
import time


# read file to extract IP and connections
with open('address/address_server.txt') as fh:
    fstring = fh.readlines()
# declaring the regex pattern for IP addresses
pattern_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
# initializing the list object
UDP_IP = pattern_ip.search(fstring[0])[0] # find ip
UDP_PORT = int(re.findall('[0-9]+', fstring[1])[0]) # find port num
# Create a UDP socket
print(f"Host IP: {UDP_IP}\nHost Port: {UDP_PORT}" )
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (UDP_IP, UDP_PORT)
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

while True:
    print("####### Server is listening #######") 
    data, address = s.recvfrom(4096)
    RECVTIME = time.time()
    # print recvd data
    print("\n\n 2. Server received: ", data.decode('utf-8'), "\n")
    # send back same packet to confirm. 
    ELAPSEDTIME = round((time.time() - RECVTIME)*(10**3),4) # return time in ms
    s.sendto(data, address)
    print("\n\n 1. Server sent : ", data,"\n",
    f"time to recieve and send: {ELAPSEDTIME} ms")