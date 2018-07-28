
from tkinter import Tk,Button,Frame

class b:
    i=int()
    j=int()
    def press(self,i,j):
        print(i,j)
    def __init__(self,f,i,j):
        self.i=i
        self.j=j
        Button(f,text=chr(i+65)+str(j),height=2,width=6,command=lambda: self.press(self.i,self.j)).grid(row=i,column=j)

root = Tk()
root.title("Button Array")
root.geometry("720x360")
f=Frame(root)
li=[]
for i in range(4):
    for j in range(7):
        li.append(b(f,i,j))
f.pack()
root.mainloop()
