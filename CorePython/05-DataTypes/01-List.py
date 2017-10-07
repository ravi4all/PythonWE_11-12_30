Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = []
>>> a.append('Hello')
>>> a
['Hello']
>>> a.append(12)
>>> a
['Hello', 12]
>>> a.append(12.6)
>>> a
['Hello', 12, 12.6]
>>> a.pop()
12.6
>>> a
['Hello', 12]
>>> a.insert(0,'Hi')
>>> a
['Hi', 'Hello', 12]
>>> a.insert(2,99')
	 
SyntaxError: EOL while scanning string literal
>>> a.insert(2,99)
>>> a
['Hi', 'Hello', 99, 12]
>>> a.append(1,2,3,4,5,6,7)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append(1,2,3,4,5,6,7)
TypeError: append() takes exactly one argument (7 given)
>>> for i in range(11):
	a.append(i)

	
>>> a
['Hi', 'Hello', 99, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a.pop()
10
>>> a.pop(5)
1
>>> a
['Hi', 'Hello', 99, 12, 0, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.remove(99)
>>> a
['Hi', 'Hello', 12, 0, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.index(12)
2
>>> a.clear()
>>> a
[]
>>> a = ['Hi','Hello',12,77,12.45,'Bye']
>>> 'Bye' in a
True
>>> 'Python' in a
False
>>> a.index('Python')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.index('Python')
ValueError: 'Python' is not in list
>>> a = [12,11,34,65,2,23,6,18,9]
>>> sorted(a)
[2, 6, 9, 11, 12, 18, 23, 34, 65]
>>> sorted(a, reversed = True)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sorted(a, reversed = True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> sorted(a, reverse = True)
[65, 34, 23, 18, 12, 11, 9, 6, 2]
>>> a.sort()
>>> a
[2, 6, 9, 11, 12, 18, 23, 34, 65]
>>> a.append([99,98,97,96])
>>> a
[2, 6, 9, 11, 12, 18, 23, 34, 65, [99, 98, 97, 96]]
>>> a[-1][0]
99
>>> a.pop()
[99, 98, 97, 96]
>>> a
[2, 6, 9, 11, 12, 18, 23, 34, 65]
>>> a.extend([99,98,97,96])
>>> a
[2, 6, 9, 11, 12, 18, 23, 34, 65, 99, 98, 97, 96]
>>> a.count(2)
1
>>> 
