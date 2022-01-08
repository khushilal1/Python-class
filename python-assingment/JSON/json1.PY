import json
# from os import pardir
# from typing import TYPE_CHECKING

# loads method =.> CONVERT THE JSON FILKE TO PYHON FILE


x='''{
"name":
"khushilal",
"lastname":"mahato",
"age":20}'''
print(f"this is json string be:\n{x}")



print("\nConversion of the json string to python dict")
#PARSE
y=json.loads(x)
print(f"the value return as dict of python  be :\n{y}")

# #dict mrthod
print(y["age"])
#using get method
print(y.get("lastname"))
# del y["lastname"]
print(y)




people_string = '''
{"people":[
    {"name":"John",
     "lastname":"smith",
     "lisense":false,
     "email":"johan23@gmail.com"
     },

    {"name":"jane",
     "lasname":"doe",
     "license":true
     }

    ]

}

'''
print(f"the above json strng be:\n{people_string}")
print(type(people_string))
data=json.loads(people_string)
print(data)
# print(type(data))
print(data["people"])
print(data["people"][1]["name"])
print(type(data["people"]))


#ACESSING USING FOR LOOP
import time
for detail in data["people"]:
    print(detail)
    time.sleep(1)

# print('conversion of pyhton dict into the json string using the dunps method')


#using the dumps in order to return the python dict into the json sytring

print(data)
print(type(data))
print("changing the pyton dict into json string")

new_string=json.dumps(data,indent=2)
print(new_string)
print(type(new_string))

