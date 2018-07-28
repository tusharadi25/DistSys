from socket import socket,timeout,AF_INET, SOCK_DGRAM
import _thread as th
from random import randrange
from tkinter import *
import time
debug,server=True,False
ip,id=[['172.20.106.',0]],randrange(0,1000,1)
serverIP=""
if debug: print(id)

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
	if debug: print(ip)                       
	s = socket()
	te=time.time()
	print(te-ts)
	s.bind(('', port))
	s.listen(5)
	print ("socket is listening")            
	while True:
		
		c, addr = s.accept()     
		i=addr[0]
		c.send(str(id).encode())
		resp=c.recv(1024)
		ip.append([i,int(resp.decode())])
		server=bully()
		c.close()
		if server: 
			test = socket(AF_INET, SOCK_DGRAM)
			test.connect(("8.8.8.8", 80))
			th.start_new_thread(serve,(test.getsockname()[0],))
			test.close()	
		if debug: print(ip)

def serve(name):
	serverIP=name
	print('Server now',serverIP)
	for x in ip:
		brodcast=socket()
		brodcast.connect((str(x[0]),5555))
	th.start_new_thread(app,(6665,))

def app(awp):
	print('get request from other and store it to server')
	aw = socket()
	aw.bind(('', awp))
	aw.listen(5)
	while True:
		sr,sip = aw.accept()     
		resp=sr.recv(1024)
		l=Label(root,text=resp.decode())
		l.grid(row=2,sticky=W)
		print(resp,sip)
		sr.send('success')
		sr.close()

def brodRecive(p):
	BR = socket()
	print('abcd')
	BR.bind(('', p))
	BR.listen(5)
	while True:
		sr,sip = BR.accept()     
		serverIP=sip[0]
		print('new co-ordinator',serverIP)
		sr.close()	

def bully():
	li=[]
	for i in ip:
		li.append(i[1])
	print(li)
	if id > max(li): x=True
	else: x=False
	return x

th.start_new_thread(listener,(6666,))
th.start_new_thread(brodRecive,(5555,))

def share():
	msg=e.get()
	print(msg)
	l=Label(root,text=e.get())
	l.grid(row=2,sticky=W)
	try:
		sharing=socket()
		sharing.settimeout(1)
		sharing.connect((serverIP,6665))
		sharing.send(msg.encode())
		ack=sharing.recv(1024)
		print(ack)
		sharing.close()
	except timeout:
		server=bully()
		if server: 
			test = socket(AF_INET, SOCK_DGRAM)
			test.connect(("8.8.8.8", 80))
			th.start_new_thread(serve,(test.getsockname()[0],))
			test.close()	

#UI code

root = Tk()
msg=StringVar()
root.title("Book Ticket Online")
root.geometry("720x360")
e=Entry(root)
e.grid(row=0,sticky=W)
b=Button(root,text='Broadcast',command=share)
b.grid(row=1,sticky=W)

#f.pack()
root.mainloop()

