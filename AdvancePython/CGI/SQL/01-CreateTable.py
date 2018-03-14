import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                passwd='', db='users', autocommit=True)

cursor = connection.cursor()

query = 'CREATE TABLE user(Name varchar(100), Email varchar(100),' \
        'Password varchar(120), Company varchar(150),Salary int(255), Dept varchar(50))'

cursor.execute(query)
print("Table Created Successfully...")