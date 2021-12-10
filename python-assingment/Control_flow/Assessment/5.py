#  5. Program to Find the Sum of n Natural Numbers
# solution 1 using while loop

n=int(input("Enter the value of n up to which sum needed to calculate:\n"))
sum=0
i=0
while(i<n):
    i=i+1
    sum=sum+i
print(f"The sum of {n} natural number is {sum}")


# solution 1 using for loop


n=int(input("Enter the value of  n natural number  which sum neede to find\n"))
i=0
sum=0
for i in range(1,n+1):
    sum=sum+i
    i=i+1
print(f"The sum of {n} natural number is {sum}")
