Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m=2
>>> n=[6,3,5,9]
>>> l=m*n
>>> print(l)
[6, 3, 5, 9, 6, 3, 5, 9]
>>> print("updated l list",l)
updated l list [6, 3, 5, 9, 6, 3, 5, 9]
>>> # add an item in list
>>> n.append(8)
>>> print(n)
[6, 3, 5, 9, 8]
>>> # remove an item in list
>>> n.remove(9)
>>> print(n)
[6, 3, 5, 8]
>>> # largest number
>>> p=max(n)
>>> print(n)
[6, 3, 5, 8]
>>> print(p)
8
>>> # smallest number
>>> q=min(n)
>>> print(q)
3
>>> # creating a tuple and reverse of the created tuple
>>> M=('a','b','hello','s','r')
>>> N=reversed(M)
>>> print(tuple(M))
('a', 'b', 'hello', 's', 'r')
>>> print(M)
('a', 'b', 'hello', 's', 'r')
>>> N=reversed(M)
>>> print(tuple(M))
('a', 'b', 'hello', 's', 'r')
>>> X=('a','d','g','hello')
>>> print(X)
('a', 'd', 'g', 'hello')
>>> Z=reversed(X)
>>> print(tuple(z))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(tuple(z))
NameError: name 'z' is not defined
>>> print(tuple(Z))
('hello', 'g', 'd', 'a')
>>> # tuple to list
>>> R=(56,36,'hsr',6)
>>> S=list(R)
>>> type(R)
<class 'tuple'>
>>> type(S)
<class 'list'>
>>> R=list(R)
>>> type(R)
<class 'list'>
>>> print(R)
[56, 36, 'hsr', 6]
>>> print (" Task 5 completed ")
 Task 5 completed 
>>> 