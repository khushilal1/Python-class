s1="khuShilal"
print(s1.capitalize())  #capitalize function change  the firsyt letter of any string in upper case
print(s1.casefold())


s1="pythoNN"
print(s1.casefold()) #casfole change all the case in lowewrecase




s2="pyhton.program"
print(s2.capitalize())


# find("string",beg,end)
str = "khushilalpythonforpython is for python"
str2 = "lal"
print(str.find(str2,5)) #find()  function find the  str where that is lies in the give big string
# print(str.rfind(str2)) 
print(str.rfind(str2)) 


# startswith(“string”, beg, end)
s1='python programmer'
# islower(“string”)
print(s1.islower())

s1='python Programmer'
print(s1.islower())


# isupper(“string”)
s1="python"
print(s1.isupper()) #isuppr()give the value true if all the   word of the string is of upper

s1="PYTHON"
print(s1.isupper())


s1=input("put a string")
if (s1.isupper()):
    print(f"{s1} is of the upper")
else:
    print(f"{s1} is not of the uppercase letter")


# lower()

s1=input("put a string\n")
s2=s1.lower()  #lower() rteurn the all yyje letter in the istr corresponding lowercase
print(f"{s1} is converterd into their lower case: {s2} ")


# 8. upper()


s1=input("put a string\n")
s2=s1.upper()  #lower() rteurn the all yyje letter in the istr corresponding 
print(f"{s1} is converterd into their uppercase: {s2} ")


# swapcase()

s1=input("put a string\n")
s2=s1.swapcase()  #lower() rteurn the all yyje letter in the istr corresponding 
print(f"{s1} is converterd into their corespondingcase: {s2} ")


# 10. title()
s1=input("put a string\n")
print(s1.title())


# count(“string”, beg, end)
str = "python for Automation append and Scripting"

# a=len(str)
# print(a)
print(str.count("a"))  #count function the count occocurance of the of the ente ed string

x=["apple","apple","apple","mango","cherry","cherry"]
# a=x.count("cherry")
# print(a)
print(x.count("apple"))


# isalpha()
s1=input("Enter the string\n")
if(s1.isalpha()):
    print(f"{s1}  contain only aplphabets")
else:
    print(f"{s1}: does not contain every elemn tof alphabet")

    # 17. isalnum()


s1=input("Enter the string\n")
if(s1.isalnum()):
    print(f"{s1}  contain only aplphabets and numerical value also")
else:
    print(f"{s1}: does not contain every elemn tof alphabet and numeriacvls value only")


# isspace()

s1=input("Enter the string\n")
if(s1.isspace()):
    print(f"{s1}  contain sapce")
else:
    print(f"{s1}: does not contain any space")




# 19.join()
s1="***"
s2="python"#JOIN() join two  string together
print(s1.join(s2))



# 20.strip()
s1="        python programmer     "
print("s1:",s1.strip())

# 21.lstrip()
s1="        python programmer    "
print("s1:",s1.lstrip())
print("s1:",s1.rstrip())

# 27. replace()

str = "C++ is a programming language"
str1 = "C++"
str2 = "Python"

print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2))

text = 'python for artificial intelligence'
print(text.split())

word = 'python, for, artificial,intelligence'
print(word.split())

# partition()
string = "python is best proggramming language"
print(string.partition("best"))