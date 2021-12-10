
# Program to Read a Number n and Compute n+nn+nnn
n=int(input("Enter the value of n:"))  #typecasting the str into int
t1=str(n)+str(n)   #typecasting str in int and concatenate
t2=str(n)+str(n)+str(n)
com=n+int(t1)+int(t2) 

print(com)