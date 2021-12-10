'''print("Demonstrating the tuple")
#craeting the empty tuple

tuple=()
print("the empty tupple be:")
print(tuple)


tuple=("mohan",'ram')
print("\nTuple with the use of string")
print(tuple)


list =[3,4.7,67]
print(list)

#conversion of list into tuple
print(tuple(list))

tuple=(3,4,5,6)
print(list[tuple])


# Creating a Tuple with the
# use of built-in function
a=tuple("python")
b=list[a]
print(a)
print(b)

tuple=(3,4,5,6)
print(tuple)
print(list[tuple])
'''
# Creating a Tuple
# with nested tuples

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'programming')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)


#Accessing elements of Tuple
# Python program to
# demonstrate accessing tuple
tuple1 = tuple([1, 2, 3, 4, 5])
# Accessing element using indexing
print("First element of tuple")
print(tuple1[0])
# Accessing element from last
# negative indexing
print("\nLast element of tuple")
print(tuple1[-1])
print("\nThird last element of tuple")
print(tuple1[-3])