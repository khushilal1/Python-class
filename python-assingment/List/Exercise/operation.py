#fonding the lenght of list using the for loop
l1=[1,2,23,3,4,5,6,7,7,8,8]
count=0

for ele in l1:
    count=count+1

print(f"the lenghth of list {l1} is:{count}")
#direct methos
print(len(l1))

#   Iteration
# loop using the range and for loop
l1=[1,2,23,3,4,5,6,7,7,8,8]
for ele in range(len(l1)):
    # print(ele)
    print(l1[ele])
    


    # using thhe while Loop

l1=[1,2,23,3,4,5,6,7,7,8,8]
length=len(l1)
i=0
while(i<length):
    print(l1[i])
    i=i+1


l1=[1,2,23,3,4,5,6,7,7,8,8]
i=0
while(i<len(l1)):
    print(l1[i])
    i=i+1

#using the enumerat


l1=[1,2,23,3,4,5,6,7,7,8,8]
for i,v in enumerate(l1):
    print(f"At {i} the value is {v}")



l1=[1,2,34,5]
l2=[3,4,7,8,"hello"]
a=[l1,l2]  #method of concatenating
print(a)


#using the * operator

l1=[1,2,34,5]
l2=[3,4,7,8,"hello"]
a=[*l1,*l2]  #method of concatenating
print(a)


