

'''
s1="python"
s2="program"

c=(s1+s2)  #concatenating two string at one
print(c)
d=s1+" "+s2
print(d)
# print(s1 +" " +s2)  #concatente with the gappi ng between them

# using join() method
s1="python"
s2="program"
s3="*".join([s1,s2])  #join function is used to  concatenate two string
print(s3)  #(*)  helps to join two string by the before character


s1="python"
s2="program"
s5="@".join([s1,s2])  #join function is used to  concatenate two string with the undescore perator
print(s5)  #(*)  helps to join two string by the before character



s1="python"
s2="program"
s4="_".join([s1,s2])  #join function is used to  concatenate two string with the undescore perator
print(s4)  #(*)  helps to join two string by the before character
print(s1,s2)  #bt defatlt it oncatenate two string with a white space


# Iterating Through a string
main=""
s1="pythonprogarm"
for ele in s1:  #iterating using  for loop
    main=main+ele
    print(ele ,end="********")
print(main ,end="**")  #end use to print at the end 
  #using the range function
s2="pythondeveloper"
for ele in range(0,len(s2)):
    # print(s2)
    # print(s2[ele])
    print(f"{ele,s2[ele]}")

    # Using enumerate() function

s3="pythonhelper"
for i,v in enumerate(s3):
    print(i)
    print(v)




s3="pythoninstructor"
for a,b in enumerate(s3):
    print(a,b)
    # print(a)

s3="pythoninstructor"
    # Iterate characters in reverse order
for ele in (s3[::-1]):
    print(ele)

s1="pythonprogramming"
for ele in reversed(range(0,len(s1))):
    print(s1[ele])


# String Membership Test
a=[1,2,3,4,5]
print( 3 in a)
print( 6 in a)
print(6 not in a)





# Logical Operators on String
s1=""
print(s1)



str1 = ''
str2 = 'python'
# repr is used to print the string along with the quotes
# Returns str1

print((str1 and str2))      # # Returns str1
print((str1 or str2))# Returns str2

print(repr(str2 and str1))  #repr  function print wuth the used quotation
print(repr(str1 or str2))
# Returns str2
print(repr(str2 or str1))
str1 = 'for'
# Returns str2
print(repr(str1 and str2))
# Returns str1
print(repr(str2 and str1))
# Returns str1
print(repr(str1 or str2))
# Returns str2
print(repr(str2 or str1))
str1='mohan'
# Returns False
print(repr(not str1))
str1 = ''
# Returns True
print(repr(not str1))


line = "Python \nJavascript \nC++"
print(line.split())  #split function give the list
# print(line.split(' ', 1))


line = "Python Javascript C++"
s1="khushilal MAhato"  #splity function return the list
# a=print(s1.split())
a=s1.split()
print(type(a))
print(line.split())

'''
line = "Python Javascript C++"
print(line.split())

