
print("Save your Name and phone number")
Name=[]
Number=[]
n=int(input("Enter the number of person you want  to add\n"))
i=0
for  i in range(n):
    name=input("Enter your name \n")
    number=input("Enter your number \n")
    Name.append(name)
    Number.append(number)
print("\n")

x=input("Do you want to see all the detail that you enter?yes/no")
while(x=="yes" or x=="y"):
    for i in range(n):
        print(Name[i] )
        print(Number[i] )
        break

    

print("Do you want to search your name!!")
search=input("Enter your name to search")
if (search in Name):
    print(f"{Name[i]} be :")
else:
    print("name not fond")

    