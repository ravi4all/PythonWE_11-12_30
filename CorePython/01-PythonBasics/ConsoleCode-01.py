Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 12
>>> a_b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a_b
NameError: name 'a_b' is not defined
>>> a+b
22
>>> a = "Hello world"
>>> type(a)
<class 'str'>
>>> a[0:5]
'Hello'
>>> a[:]
'Hello world'
>>> a[0:]
'Hello world'
>>> a[:-1]
'Hello worl'
>>> a[-1]
'd'
>>> a[::-1]
'dlrow olleH'
>>> len(a)
11
>>> a.replace("Hello", "Bye")
'Bye world'
>>> a
'Hello world'
>>> a[0] = "Hi"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[0] = "Hi"
TypeError: 'str' object does not support item assignment
>>> a
'Hello world'
>>> b = a
>>> b
'Hello world'
>>> a
'Hello world'
>>> b[0]
'H'
>>> id(a)
1565456773360
>>> id(b)
1565456773360
>>> print("Hello "World"")
SyntaxError: invalid syntax
>>> print('Hello "World"')
Hello "World"
>>> a
'Hello world'
>>> a.find('r')
8
>>> a.rfind('r')
8
>>> a.index('r')
8
>>> a = 'Hello world world world'
>>> a.find('r')
8
>>> a.rfind('r')
20
>>> a = 'Hello worrrld'
>>> a.find('r')
8
>>> a.find('r')
8
>>> a.rfind('r')
10
>>> a.index('r')
8
>>> a = 12345
>>> a = 'Hello worrrld'
>>> a.count('r')
3
>>> a.isidentifier()
False
>>> a.islower()
False
>>> a.isalnum()
False
>>> a = 10
>>> b = 12
>>> c = a+b
>>> x = str(c)
>>> a
10
>>> x
'22'
>>> x.isidentifier()
False
>>> '22'
'22'
>>> x
'22'
>>> x.isdigit()
True
>>> import keywords
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    import keywords
ModuleNotFoundError: No module named 'keywords'
>>> import keyword
>>> keyword.kwlist()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    keyword.kwlist()
TypeError: 'list' object is not callable
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
33
>>> 
