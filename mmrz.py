Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> a=[1,2,3,"ali" , True, [1,2,3,4]]
>>> a[5][3]
4
>>> a[-1]
[1, 2, 3, 4]
>>> a[-6]
1
>>> a[-1][-4]
1
>>> a[-1][-1]
4
>>> a.append9
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.append9
AttributeError: 'list' object has no attribute 'append9'
>>> a.append(13)
>>> a
[1, 2, 3, 'ali', True, [1, 2, 3, 4], 13]
>>> a.append(3.5)
>>> a
[1, 2, 3, 'ali', True, [1, 2, 3, 4], 13, 3.5]
>>> a.append({"a":23})
>>> a
[1, 2, 3, 'ali', True, [1, 2, 3, 4], 13, 3.5, {'a': 23}]
>>> 
>>> 
>>> print("hello world")
hello world
>>> 