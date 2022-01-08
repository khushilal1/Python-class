'''from tkinter import *

main_window=Tk()#makjing the objectnof tk class

#using the pack method
# Label(main_window,text="hellow world").pack()#using pack method
# Label(main_window,text="this is tkinter").pack()


#using the grid meyhhod
Label(main_window,text="hellow world").grid(row=0,column=5)#using grid method
Label(main_window,text="this is tkinter").grid(row=7,column=5)

#text input
Entry(main_window, width=50,borderwidth=5).grid(row=0,column=1)
Entry(main_window, width=50,borderwidth=5).grid(row=1,column=1)

main_window.mainloop()








from tkinter import *

main_window=Tk()#makjing the objectnof tk class
#using the grid meyhhod
Label(main_window,text="Enetr your name").grid(row=0,column=0)#using grid method
Label(main_window,text="Age").grid(row=1,column=0)

#text input
my_name=Entry(main_window, width=50,borderwidth=5).grid(row=0,column=1)
my_age=Entry(main_window, width=50,borderwidth=5).grid(row=1,column=1)

#defining the function
def on_click():
    #using get method
    print(f"myname is {my_name.get()}, and myage be{my_age.get()}")
#button
Button(main_window,text="Click me" ,command="on_click").grid(row=3,column=1)

main_window.main


l=[1,2,3,4]
s=0
for i in l:
    s=s+i

print(s)


'''

#displayig the text and ima

from tkinter import *

main_window=Tk()

Label(main_window,
text="hello",
background="red",
foreground="blue",
width=10,
height=10
).grid(row=0,column=0)


Button(main_window,
text="click me",
background="green",
foreground="blue"
).grid(row=3,column=2)


Entry(main_window,
background="yellow",
foreground="purple",
).grid(row=2,column=1)


Entry.delete(0,END)

main_window.mainloop()
