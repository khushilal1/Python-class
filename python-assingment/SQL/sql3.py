import sqlite3

con=sqlite3.connect("students.db")
crs=con.cursor()

# command1='''CREATE TABLE student_detail(
# sid INTEGER,
# fname VARCHAR(10),
# lastname VARCHAR(10))'''
# crs.execute(command1)

# command2='''INSERT INTO student_details
# VALUES(7645,"MOHAN")'''
# crs.execute(command2)
# con.commit()

# putting more more perdom
pk=[1,2,3,4,5]
firstname=["ram","shyam","mohan","hari","gita"]

lastname=["yadv","mahato","kushwaha","rai","kurmi"]

for i in range(5):  
    command2=f'''INSERT INTO student_detail
    VALUES({pk[i]},"{firstname[i]}","{lastname[i]}")'''
    crs.execute(command2)
    con.commit()

    print("successsfully inserted")