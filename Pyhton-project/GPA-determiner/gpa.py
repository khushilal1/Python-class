


print("NEPAL GPA SYSTEM OF EDUCATION!!!\n")


s = float(input("Enter the  your score in GPA:\n"))
if (s<=4):
    if(s > 3.6 and s<=4):
        print(f"you have got  garde A+ for your garde {s}")
    elif(s >3.2 and s <=3.6):
        print(f"you have got  garde A for your garde {s}")
    elif(s >2.8 and s <=3.2):
        print(f"you have got  garde B+ for your garde {s}")
    elif(s >2.4 and s <=2.8):
        print(f"you have got  garde B for your garde {s}")
    elif(s >2.0 and s <=2.4):
        print(f"you have got  garde C+ for your garde {s}")
    elif(s >1.6 and s <=2.0):
        print(f"you have got  garde C for your garde {s}")
    elif(s >1.2 and s <=1.6):
        print(f"you have got  garde D+ for your garde {s}")
    elif(s >.8 and s <=1.2):
        print(f"you have got  garde D for your garde {s}")
    elif(s <=0.8):
        print(f"you have got  garde E for your garde {s}")
else:
    print("Please!!! Reacheck your GPA once more....")



