#!C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

useremail = form.getvalue('useremail')
userpwd = form.getvalue('userpwd')

def checkUser():
    if useremail == "ram@gmail.com":
        return "Hello "+useremail
    else:
        return "User donot exist"


print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{}</h1>
</body>
</html>
""".format(checkUser()))