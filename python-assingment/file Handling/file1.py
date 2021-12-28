f=open("java.txt","r")
# f.write("I love java progarmming")
# f.writelines("\npython is my best language\nhello")
x=f.read()
y=f.readlines() #fives the size in the list form
print(x)
# print(y)

f=open("java.txt",mode="r")
data=f.readlines()
# print(data)
for i in data:
    print(i)


# Methods (tell and seek)
import time
f=open("file1.txt",mode="r")
for x in f:
    time.sleep(1)
    print(x)
    time.sleep(1)

# Check if File exist
import time
import os
f=open("file1.txt",mode="r")
for x in f:
    time.sleep(1)
    print(x)
    time.sleep(1)

if os.path.exists("file1.txt"):
    print("file1.txt")
    f=open("file1.txt",mode="r")
    x=f.read()
    print(x)
else:
    print("file does not exist")

import os
f=open("java.txt",mode="w")
x=f.write("i am python programmer")
print(x)
os.rmdir("delete1")
if os.path.exists("java.txt"):
    os.remove("java.txt")
    print("file delet")

else:
    print("file doesnot exist")