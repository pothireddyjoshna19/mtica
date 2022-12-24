Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello'"world"'python'
'helloworldpython'
a="hello
SyntaxError: unterminated string literal (detected at line 1)
a="hello","world",'python'
type(a)
<class 'tuple'>
a=2.3,23,'sunil reddy',5+6j,'s'
a
(2.3, 23, 'sunil reddy', (5+6j), 's')
type(a)
<class 'tuple'>
a=(25)
b=(9.8)
c=('hello world')
type(a)
<class 'int'>
a=(100,)
type(a)
<class 'tuple'>
type(c)
<class 'str'>
type(a)
<class 'tuple'>
lst2.append (25)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    lst2.append (25)
NameError: name 'lst2' is not defined
type(lst2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(lst2)
NameError: name 'lst2' is not defined
type(lst1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    type(lst1)
NameError: name 'lst1' is not defined
type(lst1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    type(lst1)
NameError: name 'lst1' is not defined
lst=(910,15,'hello')
lst
(910, 15, 'hello')
lst.append(199)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    lst.append(199)
AttributeError: 'tuple' object has no attribute 'append'
lst.append (199)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    lst.append (199)
AttributeError: 'tuple' object has no attribute 'append'
lst1=(10,56,'shell')
lst1
(10, 56, 'shell')
type(lst1)
<class 'tuple'>
lst2=(23,99)
lst2
(23, 99)
lst2.append (15)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    lst2.append (15)
AttributeError: 'tuple' object has no attribute 'append'
lst1=[10,25,'sunil reddy']
lst1
[10, 25, 'sunil reddy']
lst1.append (35)
lst1
[10, 25, 'sunil reddy', 35]
