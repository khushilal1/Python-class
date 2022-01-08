import json
import time


with open("./zones_with_district_headquater.json",mode="r") as f:
    data=json.load(f)
# print(data)
print(type(data))

zone=input("Enter  the name of zone that you want to know  district and its heaquarter\n")
for dis in range(len(data[zone])):
    print("fetching district....")
    time.sleep(3)
    print(f'''The district of {zone} zone be:{data[zone][dis]["district"]}''')
    time.sleep(2)
    print(f'''fetching the headquarter of {data[zone][dis]["district"]} district....\n''')
    time.sleep(3)
    print(f'''The headdquarter of {data[zone][dis]["district"]} is {data[zone][dis]["headquarter"]}\n''')
print("The above information are  from the internet:")