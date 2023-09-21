from tkinter import *

interface = Tk()
interface.geometry("600x600")
data = StringVar()
e1 = Entry(interface, textvariable=data)
e1.place(x=110,y=50,height=50,width=100)


def func():
    l2.config(text="your name is :"+data.get())
l1 = Label(interface, text="enter your name")
l1.place(x=10,y=50,height=50,width=100)
l2 = Label(interface)
l2.place(x=120,y=250,height=50,width=250)
b = Button(interface,text="press",command=func)
b.place(x=10,y=150,height=50,width=100)
def counter():
    l2.config(bg="red",text="changed")
r = Radiobutton(interface,text="select",command=counter)
r.place(x=300,y=300,height=50,width=100)
interface.mainloop()

conn =  pymysql.connec
cursor = connection.cursor
try:
    cursor.exec