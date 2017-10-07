Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d = {'id':101,'name':'Ram'}
>>> d['id']
101
>>> d['age'] = 21
>>> d
{'id': 101, 'name': 'Ram', 'age': 21}
>>> d.values()
dict_values([101, 'Ram', 21])
>>> d.keys()
dict_keys(['id', 'name', 'age'])
>>> d.items()
dict_items([('id', 101), ('name', 'Ram'), ('age', 21)])
>>> for i in d:
	print(i)

	
id
name
age
>>> for i in d.items():
	print(i)

	
('id', 101)
('name', 'Ram')
('age', 21)
>>> d.get('id')
101
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d.pop('id')
101
>>> d
{'name': 'Ram', 'age': 21}
>>> 
