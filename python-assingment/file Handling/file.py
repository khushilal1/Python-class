# File Handling
# txt file
f=open("file.txt2",mode="w")
f.write("hell0 world i am engineering student")
f.close()
print(type(f))
print(f)



# txt mode
f= open("file.tx1",mode="w")
f.write("i am going to nepal")
f.close()
print("file create succesfully")


f=open("file.txt1",mode="r")
data=f.read()
print(data)
f.close()

# binary mode
f=open("file.txt1",mode="rb")
f.write("my name")
f.close()


# Opening a File
f=open("file.tx1",mode="r")
data=f.read(100) #reda function take the integer value hw chaacter u wanr t to read

f.close()
print(data)

# Text file mode and Binary File mode
# File object variables



from os import pardir


f=open("file.tx1",mode="r")
data=f.read(7) #reda function take the integer value hw chaacter u wanr t to read
print(data)

more_data=f.read(12)
print(more_data)

f.close()



#wirte content in pyhton]
with open("python.txt",mode="w") as f:
    f.write("i am python prpgrammer \n")
    f.write("i love python \n all the people want to be healthy")

    #using the append
with open("python.txt",mode="a") as f:
    f.write("\n i really like the python\n i am feeeling very happy today")

with open("python.txt",mode="r") as f:
    data=f.read()
    print(data)

# writelines and readlines to write number of lines of code

d= open("python.txt",mode="r")
line1=d.readlines()  #gives the result in the form of list
# lines=d.read()
# print(lines)
print(line1)
d.close()






#writelines

d= open("java.txt",mode="w")
d.writelines("the world are going toward this langauage\nwe are happy to learn java\nits amazing langauage")  #gives the result in the form of list
# lines=d.read()
# print(lines)
d.close()

# Check File exists or not
import os
r=os.path.isfile("file.tx1")
x=os.path.isfile("java.txt")

print(r)
print(x)


if os.path.isfile("java.tx"):
    f=open("java.txt","r")

else:
    print("file not found")






# Writing data to a file
# write()
f=open("java.txt","w")
f.write("mohan")
f.write("yadav")
f.close()