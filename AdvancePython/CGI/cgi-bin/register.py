#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                passwd='', db='users', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

name = form.getvalue('username')
email = form.getvalue('useremail')
pwd = form.getvalue('userpwd')
company = form.getvalue('company')
salary = form.getvalue('salary')
dept = form.getvalue('dept')

query = 'INSERT INTO user VALUES(%s, %s, %s, %s, %s, %s)'

cursor.execute(query,(name,email,pwd,company,salary,dept))

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Registered Successfully</h1>
</body>
</html>
""")
