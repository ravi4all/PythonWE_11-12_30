import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                passwd='', db='users', autocommit=True)

cursor = connection.cursor()

query = 'INSERT INTO user VALUES("Ram", "ram@gmail.com","ramram","HCL","15000","IT")'

cursor.execute(query)
print("Data Inserted Successfully...")