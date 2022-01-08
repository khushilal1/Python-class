import sqlite3

con=sqlite3.connect("database.db")
crs=con.cursor()


# command1='''CREATE TABLE computer_details(
#     id INTEGER(10),
#     fname VARCHAR(10),
#     lastname VARCHAR(10)
#     )'''
# crs.execute(command1)

# commnad2=f'''INSERT INTO computer_details
# VALUES(
# 6545364,
# "khushilal",
# "mahato"
# )
# '''
# crs.execute(commnad2)
# con.commit()

# commnad3=f'''INSERT INTO computer_details
# VALUES(
# 654536,
# "khushi",
# "yadav"
# )
# '''
# crs.execute(commnad3)
# con.commit()
# commnad4='''UPDATE computer_details SET lastname="KUSHAWAA" WHERE fname="khushi"'''
# crs.execute(commnad4)
# con.commit()

# import time
# command5='''SELECT * FROM computer_details'''
# value=crs.execute(command5)

# for i in value:
#     print(i)
#     time.sleep(1)

# command1='''DELETE FROM computer_details WHERE fname="khushi"'''
# crs.execute(command1)
# con.commit()

# command2='''DROP TABLE computer_details'''
# crs.execute(command2)
# con.commit()
