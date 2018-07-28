from socket import socket,timeout,AF_INET, SOCK_DGRAM
import _thread as th
from random import randrange
from tkinter import Tk,Frame,Button
import time
debug,server=True,False
ip,id=[],randrange(0,1000,1)
serverIP=''
if debug: print(id)

def listener(port,nw='192.168.1.'):
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
	s.listen()
	print ("socket is listening")            
	while True:
		c, addr = s.accept()     
		i=addr[0]
		c.send(str(id).encode())
		resp=c.recv(1024)
		ip.append([i,int(resp.decode())])
		c.close()
		server=bully()
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
		brodcast.send('0'.encode())
	th.start_new_thread(app,(7777,))

def app(awp):
	print('get request from other and store it to server')
	aw = socket()
	aw.bind(('', awp))
	aw.listen()
	while True:
		sr,sip = aw.accept()     
		resp=sr.recv(1024)
		print(resp,sip)
		#process
		sr.send('success')
		sr.close()

def brodRecive(p):
	BR = socket()
	BR.bind(('', p))
	BR.listen()
	while True:
		sr,sip = BR.accept()     
		resp=sr.recv(1024)
		if resp.decode() is '0': serverIP=sip[0]
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

def book(i,j):
	print('Booking..',i,j)
	'''try:
		booking=socket()
		booking.connect((serverIP,7777))
		booking.send(str(chr(i+65)+str(j)).encode())
		ack=booking.recv(1024)
		print(ack)
		booking.close()
	except timeout:
		server=bully()
		if server: 
			test = socket(AF_INET, SOCK_DGRAM)
			test.connect(("8.8.8.8", 80))
			th.start_new_thread(serve,(test.getsockname()[0],))
			test.close()	
    '''

#UI code
root = Tk()
root.title("Book Ticket Online")
root.geometry("720x360")
f=Frame(root)
b=[]
for i in range(0,4):
	for j in range(0,7):
		b.append(Button(f, text=chr(i+65)+str(j),height=2,width=6,command=lambda :book(i,j)).grid(row=i,column=j))
f.pack()
root.mainloop()