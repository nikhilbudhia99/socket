#!/usr/bin/python

#senders code
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(5):
        msg=raw_input("enter your message :  ")
        s.sendto(msg,("192.168.122.1",9876))

#receivers code
#!/usr/bin/python2

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.122.1',9876))

for i in range(5):
	print s.recvfrom(10000)



~                                                                               
~                                       
