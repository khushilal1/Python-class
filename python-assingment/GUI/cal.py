from tkinter import *
from tkinter import font
root=Tk()
root.title("khushilal")

scvalue=StringVar()
scvalue.set("")

screen=Entry(root,textvar=scvalue,font="lucid 40 bold")
screen.pack(fill=X ,padx=10,pady=10)

f=Frame(root,background="grey")
b=Button(f,text="9",padx=28,pady=22)
b.pack()
f.pack()



root.mainloop()