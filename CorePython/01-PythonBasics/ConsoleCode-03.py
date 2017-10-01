Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,"Hello","Bye","Python",22,11]
>>> a = b
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = b
NameError: name 'b' is not defined
>>> b = a
>>> b
[1, 'Hello', 'Bye', 'Python', 22, 11]
>>> a
[1, 'Hello', 'Bye', 'Python', 22, 11]
>>> id(a)
2384632359880
>>> id(b)
2384632359880
>>> a[0] = 10.5
>>> a
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> b
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> a
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> a[:]
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> a[1:5]
['Hello', 'Bye', 'Python', 22]
>>> a[0:]
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> a[:-1]
[10.5, 'Hello', 'Bye', 'Python', 22]
>>> a[-1]
11
>>> a[-2]
22
>>> a[::-1]
[11, 22, 'Python', 'Bye', 'Hello', 10.5]
>>> a[::2]
[10.5, 'Bye', 22]
>>> a
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> a
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> b = a[:]
>>> b
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> a
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> id(a)
2384632359880
>>> b(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b(a)
TypeError: 'list' object is not callable
>>> id(b)
2384632359496
>>> a[0] = 100
>>> a
[100, 'Hello', 'Bye', 'Python', 22, 11]
>>> b
[10.5, 'Hello', 'Bye', 'Python', 22, 11]
>>> a = [100, 'Hello', ['Bye', 'Python', 22], 11,33,44]
>>> a
[100, 'Hello', ['Bye', 'Python', 22], 11, 33, 44]
>>> a[2]
['Bye', 'Python', 22]
>>> a[2][0]
'Bye'
>>> b = a[:]
>>> b
[100, 'Hello', ['Bye', 'Python', 22], 11, 33, 44]
>>> a
[100, 'Hello', ['Bye', 'Python', 22], 11, 33, 44]
>>> id(a)
2384632529352
>>> id(b)
2384620740296
>>> a[2][0] = "Hi"
>>> a
[100, 'Hello', ['Hi', 'Python', 22], 11, 33, 44]
>>> b
[100, 'Hello', ['Hi', 'Python', 22], 11, 33, 44]
>>> a[0] = 99
>>> a
[99, 'Hello', ['Hi', 'Python', 22], 11, 33, 44]
>>> b
[100, 'Hello', ['Hi', 'Python', 22], 11, 33, 44]
>>> import deepcopy
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    import deepcopy
ModuleNotFoundError: No module named 'deepcopy'
>>> import copy
>>> b = copy.deepcopy(a)
>>> b
[99, 'Hello', ['Hi', 'Python', 22], 11, 33, 44]
>>> a
[99, 'Hello', ['Hi', 'Python', 22], 11, 33, 44]
>>> a[2][0] = "Bye"
>>> a
[99, 'Hello', ['Bye', 'Python', 22], 11, 33, 44]
>>> b
[99, 'Hello', ['Hi', 'Python', 22], 11, 33, 44]
>>> 
