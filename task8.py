Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
@@ -0,0 +1,153 @@
Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1 = {"cricket":"sachin","badminton":"sindhu","running":"usha"}
>>> dict2 = {"madugula":"halwa","anakapalli":"jaggery","ongole":"mirchi"}
>>> dict3 = {**dict1,**dict2)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> dict3 = {**dict1,**dict2}
>>> print(dict3)
{'cricket': 'sachin', 'badminton': 'sindhu', 'running': 'usha', 'madugula': 'halwa', 'anakapalli': 'jaggery', 'ongole': 'mirchi'}
>>> #sorting the value in the list and converting it to the set
>>> a = [58,66,665,3,78,2,1,]
>>> print(a)
[58, 66, 665, 3, 78, 2, 1]
>>> num.sort()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    num.sort()
NameError: name 'num' is not defined
>>> a.sort()
>>> print(a)
[1, 2, 3, 58, 66, 78, 665]
>>> a=set(a)
>>> print(a)
{1, 2, 3, 66, 78, 665, 58}
>>> print(type(a))
<class 'set'>
>>> #to list no.of.items in a dict key and sorting
>>> print(dict2)
{'madugula': 'halwa', 'anakapalli': 'jaggery', 'ongole': 'mirchi'}
>>> #without function
>>> print(dict2)
{'madugula': 'halwa', 'anakapalli': 'jaggery', 'ongole': 'mirchi'}
>>> len(dict2.keys())
3
>>> sorted(dict2)
['anakapalli', 'madugula', 'ongole']
>>> sorted(dict2.keys())
['anakapalli', 'madugula', 'ongole']
>>> #repeated item in the list
>>> a = 3,3,3,8,2,6,3,691,3
>>> count = a.count(3)
>>> print(count)
5
>>> #to get a string from the given string
>>> str1 = input("Enter the string:")
Enter the string:hellow world
>>> char = input("Enter the character:")
Enter the character:h
>>> X = list(str1)
>>> X[0] = char
>>> new_str = ''.join([str(item) for item in X])
>>> print(new_str)
hellow world
>>> #to get a string from the given string
>>> str = input("Enter the string:")
Enter the string:hey start
>>> str = str.title()
>>> print(str)
Hey Start
>>> #mean
>>> n_num = [1,2,3,4,5]
>>> n = len(n_num)
>>> get_sum = sum(n_num)
>>> mean = get_sum/n
>>> print("mean/average is :"+str(mean))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print("mean/average is :"+str(mean))
TypeError: 'str' object is not callable
>>> print("mean/average is:"+str(mean))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print("mean/average is:"+str(mean))
TypeError: 'str' object is not callable
>>> n_num = [1,2,3,4,5]
>>> n = len(n_num)
>>> get_sum = sum(n_num)
>>> mean = get_sum/n
>>> print("mean/average is:"+str(mean))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print("mean/average is:"+str(mean))
TypeError: 'str' object is not callable
>>> #mediann
>>> def my_median(sample):
	n = len(sample)
	index = n//2
	if n%2:
		return sorted(sample)[index]
	return sum(sorted(sample)[index-1:index+1])/2

>>> my_median([3,5,1,4,2])
3
>>> my_median([3,5,1,4,2,6])
3.5
>>> import statistics
>>> statistics.mode([4,1,2,2,3,5])
2
>>> #mean
>>> n_num = [1,2,3,4,5]
>>> n = len(n_num)
>>> get_sum = sum(n_num)
>>> mean = get_sum/n
>>> print("mean/average is:"+str(mean))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print("mean/average is:"+str(mean))
TypeError: 'str' object is not callable
>>> 
>>> 
>>> 
>>> string = "ghsakjfywkefksdgfkuwykkkkkkkdyvd"
>>> #swap cases of a string
>>> strind = "ghsakjfywkefksgdfkuxykkkkkkkdyvd"
>>> print(strind.swapcase())
GHSAKJFYWKEFKSGDFKUXYKKKKKKKDYVD
>>> strind = "striver"
>>> print(strind.swapcase())
STRIVER
>>>  #7
>>> x = int(input("Enter the number:"))
Enter the number:4
>>> a = 4
>>> b = 5
>>> c = 6
>>> sum = a+b+c
>>> if (sum%x)==0:
	print("The sum is divisible by num")
else:
	print("The sum is not divisible by num")


The sum is not divisible by num
>>> #10
>>> num1 = int(input("Enter the number:"))
Enter the number:4
>>> 
>>> 
>>> 
>>> 
>>> number = int(input("Enter the integer:",))
Enter the integer:4
>>> print("Equivalent binary number is:",bin(number))
Equivalent binary number is: 0b100
>>> print("Equivalent octa decimal number is:",oct(number))
Equivalent octa decimal number is: 0o4
>>> n = 344
>>> print(oct(n))
0o530
>>> n1 = 4
>>> print(oct(n1))
0o4
>>>  
