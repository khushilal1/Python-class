from tkinter import *

root=Tk() #main window as  root
#text arae
e=Entry(root,
width=35,
borderwidth=5).grid(row=0,columnspan=3,padx=30)
#makinnf a list empty



list_of_number=[]

def number_input(number):
    current_value=e.get()
    e.delete(0,END)
    e.insert(0,str(current_value)+str(number))

def sum():
  num1=e.get
  list_of_number.append(num1)
  e.delete(0,END)
  # e.insert(0,int(current_value))

def subtract():
  pass



def product():
  # num1=e.get
  # list_of_number.append(num1)
  pass

def division():
  # num1=e.get
  # list_of_number.append(num1)
  pass


def clear_values():
  list_of_number.clear()
  e.delete(0,END)

def equal():
  num1=e.get()
  list_of_number.append(num1)
  e.delete(0,END)
  e.insert(0,list_of_number)
  # s=0
  # for i in list_of_number:
  #   s=s+i
  # e.insert(s)

  #button from 9-0 ,addbutton,clear,equql
bttn9=Button(root,text="9",padx=40,pady=20,command=lambda:number_input(9)).grid(row=1,column=0)
bttn8=Button(root,text="8",padx=40,pady=20,command=lambda:number_input(8)).grid(row=1,column=1)
bttn7=Button(root,text="7",padx=40,pady=20,command=lambda:number_input(7)).grid(row=1,column=2)


bttn6=Button(root,text="6",padx=40,pady=20,command=lambda:number_input(6)).grid(row=2,column=0)
bttn5=Button(root,text="5",padx=40,pady=20,command=lambda:number_input(5)).grid(row=2,column=1)
bttn4=Button(root,text="4",padx=40,pady=20,command=lambda:number_input(4)).grid(row=2,column=2)


bttn3=Button(root,text="3",padx=40,pady=20,command=lambda:number_input(3)).grid(row=3,column=0)
bttn2=Button(root,text="2",padx=40,pady=20,command=lambda:number_input(2)).grid(row=3,column=1)
bttn1=Button(root,text="1",padx=40,pady=20,command=lambda:number_input(1)).grid(row=3,column=2)


bttn0=Button(root,text="0",padx=40,pady=20,command=lambda:number_input(0)).grid(row=4,column=1)

bttn_add=Button(root,text="+",padx=40,pady=20,command=lambda:sum()).grid(row=5,column=0)
bttn_subtract=Button(root,text="-",padx=40,pady=20,command=lambda:subtract).grid(row=5,column=1)
bttn_product=Button(root,text="*",padx=40,pady=20,command=lambda:product).grid(row=5,column=2)

bttn_divison=Button(root,text="/",padx=40,pady=20,command=lambda:division).grid(row=6,column=0)
bttn_cls=Button(root,text="cls",padx=40,pady=20,command=lambda:clear_values()).grid(row=6,column=1)
bttn_equal=Button(root,text="=",padx=40,pady=20,command=lambda:equal()).grid(row=6,column=2)


root.mainloop()




