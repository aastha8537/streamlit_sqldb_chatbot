import sqlite3

connection = sqlite3.connect("student.db")
cursor=connection.cursor()
table_info='''
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
'''
cursor.execute(table_info)
cursor.execute('''Insert Into STUDENT values('Aastha','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Deepa','Data Science','B',90)''')
cursor.execute('''Insert Into STUDENT values('Harry','Data Science','C',90)''')

print("The inserted records are")
data=cursor.execute("select * from STUDENT")
for row in data:
    print(row)

connection.commit()
connection.close()