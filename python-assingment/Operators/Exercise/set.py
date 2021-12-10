
print("DEMONSTRATING SETS")
# Python program to demonstrate
# Creation of Set in Python
# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)
# Creating a Set with
# the use of a String
set1 = set("Python Programming")
print("\nSet with the use of String: ")
print(set1)
# Creating a Set with
# the use of a List
set1 = set(["Python", "For", "Machine Learning"])

#Basic Datatypes 6
print("\nSet with the use of List: ")
print(set1)
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
set1 = set([1, 2, 'Python', 4, 'For', 6, 'Machie Learning'])
print("\nSet with the use of Mixed Values")
print(set1)

# Python program to demonstrate
# Accessing of elements in a set
# Creating a set
set1 = set(["Python", "For", "Programming"])
print("\nInitial set")
print(set1)
# Accessing element using
# for loop
print("\nElements of set: ")
for i in set1:
 print(i, end =" ")
# Checking the element
# using in keyword
print("Python" in set1)