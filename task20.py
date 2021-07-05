#1Q

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",

)
mycursor = mydb.cursor()
print(mydb)
dose = mydb.cursor()
dbse.execute("CREATE DATABASE Employee_Management")
dbse = mtdb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
    print(entry)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="employee_management"
)
dbse = myydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)

dbse = mydb.cursor()
dbse.execute("SHOW COLUMNS FROM employee")
for value in dbse:
    print(value)

#2Q
mycursor = mydb.cursor()
mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select max(EMP_SALARY) from employee)")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor = mydb.cursor()
mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select min(EMP_SALARY) from employee)")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#3Q
mycursor = mydb.cursor()
mycursor.execute("SELECT COUNT(*) from employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#4Q
mycursor = mydb.cursor()
mycursor.execute("SELECT * from employee WHERE EMP_NAME LIKE('ANU%')")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)





