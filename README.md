# udpcomm
UDP server and client example. Sends UDP (client to server) packet (must be on same network) and recieves (server to client) confirmation packet.

```client.py``` outputs time elapsed to send and receieve packet. 
```server.py``` outputs time elapsed to receive and send packet. 


# Outputs: 


```
# client.py

Do Ctrl+c to exit the program !!
Connecting to:
 IP: 127.0.0.1
 Port: 5678
Type some text to send => test!
1. Client Sent :  test!
2. Client received :  test!
 time to send and recieve: 39.9439 ms
```
```
# server.py

Host IP: 127.0.0.1
Host Port: 5678
Do Ctrl+c to exit the program !!
Server is listening...

2. Server received:  test!
1. Server sent :  b'test!' 
 time to recieve and send: 0.2725 ms
```

# How to run: 
I ran ```server.py``` on my Raspberry Pi on and ran ```client.py``` on my personal computer. 

# address/address.txt
- ```UDP IP:``` Add server (host) IP address. You can find this in network settings. Windows > Network settings, Linux ```ifconfig``` on terminal. 
- ```UDP Port:``` Self-determined port. 
