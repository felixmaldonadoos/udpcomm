import socket
import sys
import re

# algorithm: 
# 1. connect

# read file to extract IP and connections
with open('address.txt') as fh:
    fstring = fh.readlines()
# declaring the regex pattern for IP addresses
pattern_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
# initializing the list object
UDP_IP = pattern_ip.search(fstring[0])[0] # find ip
UDP_PORT = int(re.findall('[0-9]+', fstring[1])[0]) # find port num

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program !!")

# Let's send data through UDP protocol
while True:
    send_data = input("Type some text to send =>");
    s.sendto(send_data.encode('utf-8'), (ip, port))
    print("\n\n 1. Client Sent : ", send_data, "\n\n")
    data, address = s.recvfrom(4096)
    print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
# close the socket
s.close()