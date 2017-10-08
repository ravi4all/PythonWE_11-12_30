Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = True
>>> type(a)
<class 'bool'>
>>> a = 0
>>> bool(a)
False
>>> a = 1
>>> bool(a)
True
>>> def show():
	return

>>> show()
>>> print(show())
None
>>> def show():
	return "Hello world"

>>> show()
'Hello world'
>>> def add(a,b):
	return a + b

>>> add(2,1)
3
>>> def temp_conv(c):
	f = 9/5 * c + 32
	return f

>>> temp_conv(33.33)
91.994
>>> c = [32.11, 34.23, 38.11,36.45,29.12]
>>> for i in range(len(c)):
	print(temp_conv(i))

	
32.0
33.8
35.6
37.4
39.2
>>> temp_conv(32.11)
89.798
>>> for i in c:
	print(temp_conv(i))

	
89.798
93.614
100.598
97.61000000000001
84.416
>>> fah = []
>>> for i in c:
	f = temp_conv(i)
	fah.append(f)

	
>>> f
84.416
>>> fah
[89.798, 93.614, 100.598, 97.61000000000001, 84.416]
>>> 
