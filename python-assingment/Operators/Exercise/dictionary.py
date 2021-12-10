# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Python', 2: 'For', 3: 'Machine Learning'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Python', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Python', 2: 'For', 3:'Web Development'})
print("\nDictionary with the use of dict(): ")
print(Dict)
# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Python'), (2, 'Programming')])
print("\nDictionary with each item as a pair: ")
print(Dict)

#Accessing elements of Dictionary

# Python program to demonstrate
# accessing a element from a Dictionary
# Creating a Dictionary
Dict = {1: 'Python', 'name': 'For', 3: 'Web Development'}
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))