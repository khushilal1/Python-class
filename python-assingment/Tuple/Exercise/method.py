# Creating tuples
t1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
t2 = ('python', 'c++', 'python',
'php', 'java', 'python')
# count the appearance of 3
a = t1.count(3)
print(a)
# count the appearance of python
result = t2.count('python')
print(result)
#Counting tuples and lists as elements in Tuples
t3 = (0, 1, (2, 3), (2, 3), 1,
[3, 2], 'python', (0,))
# count the appearance of (2, 3)
res = t3.count((2, 3))
print(res)
# count the appearance of [3, 2]
res = t3.count([3, 2])
print(res)

# index(x,start)


t1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# getting the index of 3
res = t1.index(3)
print(res)


# getting the index of 3 after 4th
# index
t5 = (0, 1, 2, 3, 2, 3, 1, 3, 2)

res = t5.index(3, 4) #index(Checking value of occurance,at the index)
print('First occurrence of 3 after 4th index is:', res)