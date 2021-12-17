# copy()

d = {1: 'python', 'name': 'c++', 3: 'javascript'}
print(f"Original dictionary be :{d}")
D = d.copy()
print(f"The copied dictionary be :{D}")

# dictionary_name.values()
# stores name and corresponding salaries
salary = {"A" : 50000, "B" : 60000, "C" : 5000}
# stores the salaries only
list1 = salary.values()
print(list1)
print(type(list1))
# print(sum(list1)) # prints the sum of all salariestr()

list2 = salary.items()
print(list2)
print(type(list2))


# setdefault()
salary = {"A" : 50000, "B" : 60000, "C" : 5000}
default_value=salary.setdefault(a["Mohan"])
print(default_value)
print(salary)


# keys() ***
value= {"A" : 50000, "B" : 60000, "C" : 5000}
# print(income.keys())
c=value.keys()
print(c)

#updating to the set
value.update({"c":"mohan"})
value.update({"C":"mohan"})
print(value)



#using the keys
value_keys=""
value= {"A" : 50000, "B" : 60000, "C" : 5000}
for ele in value.keys():
    value_keys=value_keys+ele
    print(ele)
print(value_keys)
 #items()
for i in value.items():
    print(i)