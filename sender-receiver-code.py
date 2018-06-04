#user's code
#!usr/bin/python2

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#choice=raw_input("do you want to enter a command")
#s.sendto(choice,("192.168.43.235",9876))

choice='y'
while choice=='y':
	
	msg=raw_input("enter command :  ")
	s.sendto(msg,("192.168.43.235",9876))
	print s.recvfrom(50)[0]
	choice=raw_input("do you want to continue (y/n) : ")
	s.sendto(choice,("192.168.43.235",9876))
	print s.recvfrom(50)[0]
	

#receiver's code
#!usr/bin/python2
	
import socket
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.43.235",9876))

choice='y'

while choice=='y':
	msg=s.recvfrom(10000)
	#os.system(msg[0])
	data=os.system(msg[0])
	if data==0 :
		s.sendto("yes it is a command ",msg[1])
	else :
		s.sendto("no it is not a command : ",msg[1])
	choice=s.recvfrom(2)[0]
	if choice=='y':
		print "waiting for next command "
	else :
		print "exiting"

	s.sendto("getting next command ",msg[1])




	
