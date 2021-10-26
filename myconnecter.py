import mysql.connector
mydb =mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='12345678',
    port ='3306',
    database ='student_details'
)
mycursor =mydb.cursor()
mycursor.execute('select * from students')
students =mycursor.fetchall()
for students in students:
    print(students)
    print('id : ' + students[1])
    print('id : ' + students[2])
    print('Name : ' + students[3])
    print('Email id : ' + students[4])