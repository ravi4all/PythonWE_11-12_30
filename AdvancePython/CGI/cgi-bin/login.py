#!C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

username = form.getvalue('username')
userpwd = form.getvalue('userpwd')

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Hello {}</h1>
</body>
</html>
""".format(username))