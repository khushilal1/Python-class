import sqlite3
from sqlite3.dbapi2 import connect
con=sqlite3.connect('database.db')
crs=con.cursor()

# command1='''CREATE TABLE student_detail(
# fname VARCHAR(10),
# lastname VARCHAR(10))'''

# crs.execute(command1)
# command2='''INSERT INTO student_detail
# VALUES("KHUSHILAL","MAHATO")'''
# crs.execute(command2)
# con.commit()

# command3='''INSERT INTO student_detail
# VALUES("sajis","yadav")'''
# crs.execute(command3)
# con.commit()

# command4='''SELECT * FROM student_detail'''
# ans=crs.execute(command4)
# for i in ans:
#     print(i)

# command5='''UPDATE student_detail
# SET lastname="yadav"'''
# crs.execute(command5)
# con.commit()


# command6='''UPDATE student_detail
# SET fname="yadav" WHERE fname="sajis"'''
# crs.execute(command6)
# con.commit()

#delteing the element of database table
# command7='''DELETE  FROM student_detail
# WHERE lastname="yadav"
# '''
# crs.execute(command7)
# con.commit()

command8='''DROP TABLE student_detail'''
crs.execute(command8)
con.commit()