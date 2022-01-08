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




    # print(data["bheri"][dis]["headquarter"])
# # print(data["janakpur"][0])
#     # print(district)
# #     time.sleep(1)
# # print(district)
# print(type(district))




# dis=input("Enter the district to know its headquater\n")




print("SAVING THE DISTRICT IN THE RESPECTIVE ZONE")
janakpur_district=data[dis]
print(janakpur_district)

with open("janakpur_zone_with_district.json",mode="w") as f:
    json.dump(janakpur_district,f,indent=2)

with open("janakpur_zone_with_district.json",mode="r") as f:
    new_data=json.load(f)
print(new_data)
print(type(new_data))

new1_data=json.dumps(new_data,indent=2)
print(new1_data)
with open("janakpur_zone_with_district.json",mode="w") as f:
    json.dump("janakpur_district",f,indent=2)

# with open("janakpur_zone_with_district.json",mode="r") as f:
#     data=json.load(f)
# print(data)