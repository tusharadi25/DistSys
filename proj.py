from socket import socket,timeout,AF_INET, SOCK_DGRAM
import _thread as th
from random import randrange
from tkinter import *
import time
server=False
ip,id=[],randrange(0,1000,1)
print(id)

def listener(port,nw='172.20.106.'):
	ts=time.time()
	for i in range(0,255):
		try:
			init = socket()
			dest=nw+str(i)
			init.settimeout(0.001)
			init.connect((dest, port))
			init.send(str(id).encode())
			resp=init.recv(1024)
			init.close()
			ip.append([dest,int(resp.decode())])
		except timeout:
			print('',end='')
	print(ip) 
	if len(ip)!=0:
			server=bully()
			if server:
				print("server started")	                      
	s = socket()
	te=time.time()
	print(te-ts)
	s.bind(('', port))
	s.listen()
	print ("socket is listening")            
	while True:
		if len(ip)!=0:
			server=bully()
			if server:
				print("server started")
		c, addr = s.accept()     
		i=addr[0]
		resp=c.recv(1024)
		c.send(str(id).encode())
		ip.append([i,int(resp.decode())])
		c.close()

def bully():
	li=[]
	for i in ip:
		li.append(i[1])
	print(li)
	if id > max(li): x=True
	else: x=False
	return x

th.start_new_thread(listener,(6666,))
root=Tk()
root.mainloop()