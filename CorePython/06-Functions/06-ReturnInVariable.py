Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def show():
	return "Hello world"

>>> show()
'Hello world'
>>> a = show()
>>> a
'Hello world'
>>> def show():
	print("Hello world")

	
>>> show()
Hello world
>>> a = show()
Hello world
>>> a
>>> s = "Hello"
>>> s
'Hello'
>>> print(s)
Hello
>>> a
>>> type(a)
<class 'NoneType'>
>>> a = show
>>> type(a)
<class 'function'>
>>> a()
Hello world
>>> 
