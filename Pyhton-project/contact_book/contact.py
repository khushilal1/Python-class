
print("Save your Name and phone number")
Name=[]
Number=[]
n=int(input("Enter the number of person you want  to add\n"))
i=0
for  i in range(n):
    name=input("Enter your name \n")
    number=(input("Enter your number \n"))
    Name.append(name)
    Number.append(number)
print("\n")

x=input("Do you want to see all the detail that you enter?yes/no\n")
if(x=="yes" or x=="y"):
    print(f"The name you saved be: {tuple(Name)}")
    print(f"The number you saved be: {tuple((Number))}")
    
elif(x=="no" or x=="n"):
    pass
   


search=input("Do you want to search?yes/no\n")
if(search=="yes" or search=="y"):  
    search=input("Enter your name/number to search")
    if (search in (Name or Number) ):
        print(f"The name you search be:{Name[i]}\nThe number be:{Number[i]} ")
else:
        print("name not found")

    