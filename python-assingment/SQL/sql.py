# # # connecting of the database field
    
# sid INTEGER PRIMARY KEY,
# fname VARCHAR(20),
# lname VARCHAR(10),
# gender CHAR(1),
# dob DATE);"""

# crs.execute(commnad)

# print("Table cereated")


# sql_command1 = """INSERT INTO otudent_details VALUES (2301, "firstName1",\
# "Lastname1", "M", "1997-03-28");"""
# crs.execute(sql_command1)
# # # Inserting into Table


# import sqlite3
# con=sqlite3.connect("student_database.db")
# crs=con.cursor()

# command1='''CREATE TABLE students_details(studentid INTEGER,
# FirstName VARCHAR(10),
# lastname VARCHAR(10),
# fullname VARCHAR(20))'''
# crs.execute(command1)

# # for i in range(10):
# con.commit()
    
# command3='''INSERT INTO students_details
# VALUES(1,"manish",'KUSHWAHA','MANISH+KUSHWAHA')'''
# crs.execute(command3)
# con.commit()

#input from yje user
# command4='''INSERT INTO students_details
# VALUES(2,"MOHAN",'KUSHWAHA','MOHAN+KUSHWAHA')'''
# crs.execute(command4)
# con.commit()


# from os import name
# import sqlite3
# con=sqlite3.connect("student_database1.db")
# crs=con.cursor()

# # command1='''CREATE TABLE students_details1(
# # studentid INTEGER,
# # FirstName VARCHAR(10),
# # lastname VARCHAR(10),
# # fullname VARCHAR(20))'''
# # crs.execute(command1)


# #USIN FOR LOOP
# value=[1,2,3,4]
# firstname=["name1","name2","namw3"]
# lastname=["lname1","lname2","name"]


# for i in range(3):
#     command3=f'''INSERT INTO students_details1
#     VALUES({value[i]},"{firstname[i]}","{lastname[i]}","{firstname[i]} +{lastname[i]}") '''
#     crs.execute(command3)
#     con.commit()
#     print("succefully excuted")


import sqlite3 #importing module
import time
con=sqlite3.connect("detail_database.db") #connecting and creting dtatabase
list=[]
list1=[]
n=int(input("Enter the number that you want to save in database\n")) #taking the input from the user

for i in range(n):
    name=input("Eneter firstname\n")#taking the firs name of user
    list.insert(i,name)#inserting the taken namme of user in the list
    name1=input("lasttname\n") #taking the lastbnaneof user 
    list1.insert(i,name1)
print(list)#duaspalring the list of the first name
print(list1)#displayoig nthe last name of list
# #puttin into database
# command1='''CREATE TABLE  student_detail(
#     firstname VARCHAR(10),
#     lastname VARCHAR(10))'''
# crs=con.execute(command1)
print("please wait for a while")
time.sleep(3)
for e in range(n):
    command2=f'''INSERT INTO student_detail
    VALUES("{list[e]}","{list1[e]}")'''
    crs=con.execute(command2)
    con.commit()
print("successful entery")

#fetchin gdata from the database 
print("fetching the data from database")
crs.execute("SELECT * FROM student_detail") #selscting all the data frof database
time.sleep(3)
ans=crs.fetchall()
time.sleep(2)
for k in ans:
    print(k)
#