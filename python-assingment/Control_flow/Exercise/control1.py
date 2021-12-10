# loops
# for loops

l = ["python", "for", "machine learning"]
for i in l:
    print(i)


l = ("python", "khushilal","Mahato", "machine learning")
for i in l:
    print(i)
print("singh")

s = "Python"
for i in s:
    print(i)

# Loop Control Statements
# continue

for letter in 'pythonformachinelearning':
    if letter == 'e' or letter == 'u':
        print(letter)
        continue
print(f'Current Letter : {letter}')

# break

for  letter in "pythonprogramming":
    if letter == 'e' or letter == 'u':
        break
print(f'Current Letter : {letter}')



for  letter in "pythonprogramming":
    print(letter)
    if  letter == 'n':
        break


for letter in 'python':
    pass
print(f'Last Letter : {letter}')

for i in range(10):  #printing the valu from 0 to 1 less thge f=given number the toal number is equal to number which was prescribed
    print(i)


for i in range(0,5):  #printing the valu from 0 to 1 less thge f=given number the toal number is equal to number which was prescribed
    print(i)


for i in range(1,10,2):
    print(i)


l = [15,6,7,6,8,7 ,30, 40]
a=len(l)
print(f"the lenght of the list be:{a}")
for i in range(a):
    print(l[i], end=" ")




l = [15,6,7,6,8,7 ,30, 40]
a=len(l)
print(f"the lenght of the list be:{a}")
for i in range(a):
    print(l[i])



n=int(input("Enter teh value of n:"))
sum = 0
for i in range(0,n+1):
    sum = sum + i
print(f"Sum of first 10 numbers : {sum}")


# for loop with else

for i in range(1, 4):
    print(i)
else: # Executed because no break in for
    print("No Break\n")

# while Loop

count = 0
while (count < 3):
    count = count + 1
print("Hello there")


count = 0
while (count < 3):
    count = count + 1
    print("Hello there")
print("Hello there")



a = [1, 2, 3, 4]
b = 1
while b < len(a):
    b = b + 1
print(f"{b}")


a = [1, 2, 3, 4]
b = 2
while b < len(a):
    print(b)
print(f"{b}")


# Loop Control Statement
a=[1,2,3,4,5,6,7]
b=1
while b<len(a):
    print(f"{b}")
    b=b+1

i=0
a="pytehosn"
while i<len(a):
    if a[i]=="e" or a[i]=="s":
        i=i+1
        continue
    print(f"curent letter: {a[i]}")
    i=i+1



i=0
a="pytehosn"
while i<len(a):
    if a[i]=="e" or a[i]=="s":
        i=i+1
        break
    print(f"curent letter: {a[i]}")
    i=i+1




n=int(input("Enter the no that  the sum up to which needed:"))    
i=0
sum=0
while(i<n):
    i=i+1
    sum=sum+i
print(sum)





i=0
a="pythonsoftawrefoundation"

while i<len(a):
    if a[i]=="n" or a[i]=="f":
        continue
    print(a[i])

    i=i+1
