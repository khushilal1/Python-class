
# operator and operand
a=2
b=5
sum=a+b
b+=4    #b+=4------->b=b+4         
print(sum)
print(b)

# ADDITION
# INT+INT=INT 
a=3
b=5              
b=5            
b=5
print(a+b)

#   int+float=float
a=3
b=5.57
print(a+b)
# float+int=float

a=3.65
b=5
print(a+b)
# in subtraction and multiplication  same as n addition





# division


a=5
b=3.0
# /  as normal  division give the float Value
print(a/b)
# // as  floore dividion give the int value
print(a//b)

# # modulo division give the int value
print(a%b)
  
#   # exception:
# #   foored division  and mosulo division also give the float value if the denominator or numerator  or both are float 
print(a//b)
print(a%b)

a=-5
b=-3
print(a%b)
# pythons modulo oerator(%)  always retur a number of sane sign of denominator have



# Use of
# a.\t  
string="python \t guides"   #give the gap of two white space
print(string)

# b.\b  
string="python \b guides"    #give the gap of one white space
print(string)

#  c.\\ 
string="python \\ guides"   # give the gap of one white space
print(string)

#  d.\f 
string="python \f guides"   # give the gap of one white space
print(string)


a=5
print(type(a))
print(f"the vakue of  a:{a}")

a="string"
print(a[0])
print(a[3])
print(a[-1])
print(a[-2])

# list

list=[]
print(f"The empty list is :{list}")
print(type(list))

a=[]
print(type(a))

a=[2,4,5,6]
print(a)
print(type(a))


a=["python programing",.54]
print(a)
print(type(a)) 

a=[4,5,6,["pthon",5],"programming"]
print(a)
print(type(a))


# Accessing elements of List
a=[2,["pyhton"],5]
print(a[0])
print(a[1])
print(a[2])
print()

a[2]="progarm"
a[1]=6435
print(a[-1])
print(a[-2])
print(a[-3])


# 3.Tuple
a=()
print(f"The empty of tuple:{a}")
print(type(a))

a=(3,["python"],4)
print(a)
print(type(a))

a=[3,4,56]
print(a)
print(type(a))

b=tuple(a)
print(b)
print(type(b))



# Accessing elements of Tuple

a=(1,2,3,4,5,6,7)
b=("python","progarm","khushilal")
c=(a,b)
print(c)

print(c[0])
print(c[-1])
print(a[1])


# 4. Set
a={2,3,4,5}
print(a)
print(type(a))

a={2,"python",3,4,5}
print(a)
print(type(a))


a={"python",3,4,5}
print(a)


a={"python",3,4,5,1,0}
print(a)


a={2,"python",3,4,5,1,0}
print(a)


a={"aython",63,64,657,910,0}
print(a)

# loops
a=[1,2,3,4,5]
for item in a:  # for loop
    print(item)

list1=[1,2,3,4,5]
for item in list1:
 print(item)

a=[1,2,"python",("hello",4,5,6),5]
for item in a:  # for loop
    print(item)


# Accessing elements of Sets

a={2,3,4,5,6,7}
for item in a:
 print(item)

a={2,3,4,5,6}
for _2 in a:
 print(_2)



a={2,3,4,5,6,7}
for item in a:
 print(item,end="  khushilal  ")


set1 = set(["Python", "For", "Programming"])
# print(set1)
print("Python","for" in set1)

# 5. Dictionary

dict={}
print(f"The empty dictionary be:{dict}")
print(type(dict))


a={}
print(type(a))


dict={23,4}
print(type(dict))



a={1:"python"}
print(type(a))
a=dict([2,3,4])
print(a)