import sqlite3 
con=sqlite3.connect("student_database.db")
crs=con.cursor()

value=[1,2,3]
firstname=["name1","name2","nam"]
lastname=["lname1","lname2","las"]
fullname=["fname","fname2","total"]

for i in range(3):
    command3=f'''INSERT INTO students_details VALUES({value[i]},"{firstname[i]}","{lastname[i]}","{fullname[i]}"); '''
    crs.execute(command3)
    con.commit()

print("succesful entry")
