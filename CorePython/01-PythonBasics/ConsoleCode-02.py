Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = "Hello"
>>> a = [1,2,3,4,5]
>>> type(a)
<class 'list'>
>>> a = [1,'Hello',10.5,True]
>>> type(a)
<class 'list'>
>>> isinstance(a, list)
True
>>> isinstance(b, str)
True
>>> tup = (1,'Hello',10.5,True)
>>> tup
(1, 'Hello', 10.5, True)
>>> a
[1, 'Hello', 10.5, True]
>>> a[0]
1
>>> tup[0]
1
>>> a[0] = "Bye"
>>> a
['Bye', 'Hello', 10.5, True]
>>> tup[0] = "Bye"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tup[0] = "Bye"
TypeError: 'tuple' object does not support item assignment
>>> dictionary = {"id":101,"name":"Ram"}
>>> dictionary[0]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dictionary[0]
KeyError: 0
>>> dictionary['id']
101
>>> type(dictionary)
<class 'dict'>
>>> s = {1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> type(s)
<class 'set'>
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> for i in s:
	print(s)

	
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
>>> s1 = {3,4,5,6,7}
>>> s.intersection(s1)
{3, 4, 5}
>>> import frozenset
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    import frozenset
ModuleNotFoundError: No module named 'frozenset'
>>> s2 = frozenset(33,45,67,88)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s2 = frozenset(33,45,67,88)
TypeError: frozenset expected at most 1 arguments, got 4
>>> s2 = frozenset(s1)
>>> s2
frozenset({3, 4, 5, 6, 7})
>>> s1
{3, 4, 5, 6, 7}
>>> s1.update(7,11)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s1.update(7,11)
TypeError: 'int' object is not iterable
>>> s1.update(7)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s1.update(7)
TypeError: 'int' object is not iterable
>>> s1
{3, 4, 5, 6, 7}
>>> type(s1)
<class 'set'>
>>> type(s2)
<class 'frozenset'>
>>> import statistics
>>> 
