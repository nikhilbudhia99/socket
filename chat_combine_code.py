#!/usr/bin/python2

#code for 1st sender
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('192.168.122.203',9000))


for i in range(5):
        msg=raw_input('enter message:')
        s.sendto(msg,("192.168.122.1",9876))
        print s.recvfrom(10000000)

#code for second sender

#!/usr/bin/python2

import socket 


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.122.1",9876))

for i in range(5):
	print s.recvfrom(10000000)
	x=raw_input("enter message ")
	s.sendto(x,("192.168.122.203",9000))




