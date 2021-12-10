# 4. Program to Take in the Marks of 5 Subjects and Display the Grade using function
# 4. Program to Take in the Marks of 5 Subjects and Display the Grade
print("       NEPAL GPA SYSTEM OF EDUCATION!!!   \n")
x=input("press Y for yes\n")
while(x=="Y"):
    print("please!!! Enter the marks that you obtained in seveseral subject")
    a=float(input("Enter the marks of English subject:\n"))
    b=float(input("Enter the marks of Sciece subject:\n"))
    c=float(input("Enter the marks of Nepali subject:\n"))
    d=float(input("Enter the marks of Mathematics subject:\n"))
    e=float(input("Enter the marks of Computer subject:\n"))

    def gpa(a,b,c,d,e):
        t=a+b+c+d+e
        print(f"Your total marks be:{t}")
        p=t/500*100
        print(f"your percentage {p}")
        g=p/25
        print(f"your gpa garde is:{g}")


        if (g<=4):
            if(g > 3.6 and g<=4):
               print(f"you have got  gradde A+ for your garde {g}\n")
        elif(g >3.2 and g <=3.6):
            print(f"you have got  grade A for your garde {g}\n")
        elif(g >2.8 and g<=3.2):
            print(f"you have got  grade B+ for your garde {g}\n")
        elif(g >2.4 and g <=2.8):
            print(f"you have got  grade B for your garde {g}\n")
        elif(g >2.0 and g <=2.4):
            print(f"you have got  grade C+ for your garde {g}\n")
        elif(g >1.6 and g <=2.0):
            print(f"you have got  grade C for your garde {g}\n")
        elif(g>1.2 and g <=1.6):
            print(f"you have got  grade D+ for your garde {g}\n")
        elif(g >.8 and g <=1.2):
                print(f"you have got  grade D for your garde {g}\n")
        elif(g <=0.8):
            print(f"you have got  grade E for your garde {g}\n")
        else:
         print("Please!!! Reacheck your GPA once more....\n")
    gpa(a,b,c,d,e)
    x=input("please enter Y for yes and other to exit\n")