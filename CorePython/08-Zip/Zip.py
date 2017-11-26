Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = ['id', 'name', 'age', 'salary']
>>> b = [101,'Ram', 28, 15000]
>>> zip(a,b)
<zip object at 0x0000017084505748>
>>> list(zip(a,b))
[('id', 101), ('name', 'Ram'), ('age', 28), ('salary', 15000)]
>>> x = list(zip(a,b))
>>> for i in x:
	print(i)

	
('id', 101)
('name', 'Ram')
('age', 28)
('salary', 15000)
>>> 
