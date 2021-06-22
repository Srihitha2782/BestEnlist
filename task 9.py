Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1
>>> list_1 = [1,2,3,4,5]
>>> l = []
>>> n = len(list_1)
>>> for i in list_1:
	l.append(i+2)
	print(l)

	
[3]
[3, 4]
[3, 4, 5]
[3, 4, 5, 6]
[3, 4, 5, 6, 7]
>>> # 2
>>> n = int(input('Enter number:'))
Enter number:5
>>> for i in range(n):
	print(''.join(map(str,range(n-i,0,-1))))

	
54321
4321
321
21
1
>>> # 3
>>> nterms = int(input("How many terms? "))
How many terms? 7
>>> n1, n2 = 0,1
>>> count = 0
>>> if nterms <= 0:
	print("Please enter a positive interger")
	elif nterms == 1:
		
SyntaxError: invalid syntax
>>> elif nterms == 1:
	
SyntaxError: invalid syntax
>>> # 3
>>> def fib(n):
	a = 0
	b = 1
	if n == 1:
	    print(a)
	else:
	    print(a)
	    print(b)
	    for i in range(2,n):
		c = a + b
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> n = int(5)
>>> a = 0
>>> b = 1
>>> c = 0
>>> sum = 0
>>> count = 1
>>> print("fibonacci series:",end = "")
fibonacci series:
>>> while(count<= n):
	print(sum,end ="")
	count+= 1
	a = b
	b = sum
	sum = a+b
	print("\n")

	
0

1

1

2

3

>>> 
>>> # 4
>>> num = int(input("Enter a number: "))
Enter a number: 663
>>> sum = 0
>>> temp = num
>>> while temp > 0:
	digit = temp % 10
	sum += digit ** 3
	temp //= 10

	
>>> if num == sum:
	print(num,"is an Armstrong number")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> else:
	
SyntaxError: invalid syntax
>>>  else:
	 
SyntaxError: unexpected indent
>>> else
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> if num == sum:
	print(num,"is an Armstrong number")
	else:
		
SyntaxError: invalid syntax
>>> if num == sum:
	print(num,"is an Armstrong number")
else:
	print(num,"is not an Armstrong number")

	
663 is not an Armstrong number
>>> 
>>> 
>>> num = int(input("Enter a number: "))
Enter a number: 407
>>> 
>>> sum = 0
>>> temp = num
>>> while temp > 0:
	digit = temp % 10
	sum += digit ** 3
	temp //= 10

	
>>> if num == sum:
	print(num,"is an Armstrong number")
else:
	
SyntaxError: multiple statements found while compiling a single statement
>>> sum = 0
>>> temp = num
>>> while temp> 0:
	digit = temp % 10
	sum += digit ** 3
	temp //= 10

	
>>> if num == sum:
	print(num,"is an Armstrong number")
else:
	print(num,"is not an Armstrong number")

	
407 is an Armstrong number
>>> # 5
>>> n_156 = int(9)
>>> mul_21 = 0
>>> print("multiplication table of:9",)
multiplication table of:9
>>> for p in range(1,10+1):
	mul_21 = n_156,"x",p,"=",mul_21)
	
SyntaxError: unmatched ')'
>>> for p in range(1,10+1):
	mul_21 = n_156*p
	print(n_156,"x",p,"=",mul_21)

	
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
>>> #6
>>> 
>>> num = float(input("Enter a number: "))
Enter a number: 6
>>> if num > 0:
	print("Positive number")
	elif num == 0:
		
SyntaxError: invalid syntax
>>> elif num == 0:
	
SyntaxError: invalid syntax
>>> if num > 0:
	print("Positive number")
elif num == 0:
	print("Zero")
else:
	print("Negative number")

	
Positive number
>>> num = float(input("Enter a number: "))
Enter a number: 0
>>> if num > 0:
	print("Positive number")
elif num == 0
SyntaxError: invalid syntax
>>> if num > 0:
	print("Positive number")
	elif num == 0
	
SyntaxError: invalid syntax
>>> if num > 0:
	print("Positive number")
elif num == 0:
	print("Zero")
else:
	print("Negative number")

	
Zero
>>> # 7
>>> def find(ins_12345):
	year = int(ins_12345/365)
	week = int((ins_12345%365)/day_check)
	days = int((ins_12345%365)%day_check)
	print(year,":years,",week,":weeks,",days,":days")

	
>>> ins_12345 = int(402)
>>> day_check = 7
>>> find(ins_12345)
1 :years, 5 :weeks, 2 :days
>>> # 8
>>> import math
>>> def trigo(n,m):
	if n=='sin':
	    return math.sin(m)
	elif n=='cos':
	    reurn math.cos(m)
	    
SyntaxError: invalid syntax
>>> def trigo(n,m)
SyntaxError: invalid syntax
>>> def trigo(n,m):
	if n=='sin':
	    return math.sin(m)
	elif n=='cos':
	      return math.cos(m)
	elif n=='cosin':
	      return math.cosine(m)
	elif n=='tan':
	      return math.tan(m)
	elif n=='sec':
	      return math.sec(m)
	elif n=='cosec':
	      return math.cosec(m)

	
>>> 
>>> In [39]:
	
SyntaxError: invalid syntax
>>> In [29]:
	
SyntaxError: invalid syntax
>>> In[29]:
	
SyntaxError: invalid syntax
>>> print(math.cos(m))
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    print(math.cos(m))
NameError: name 'm' is not defined
>>> import math
>>> a_b = math.pi/6
>>> print("the value of cosine of pi/6 is:",end="")
the value of cosine of pi/6 is:
>>> print(math.cos(a_b))
0.8660254037844387
>>> #9
>>> print('calculator')
calculator
>>> print('1.add')
1.add
>>> print('2.subtraction')
2.subtraction
>>> print('3.multiplication')
3.multiplication
>>> print('4.divide')
4.divide
>>> ch = int(input("enter choice(1-4):"))
enter choice(1-4):5
>>> if ch ==1:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a+b
	print("sum=",c)

	
>>> #9
>>> if ch ==2:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a-b
	print("sum=",c)

	
>>> if ch ==3:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a*b
	print("sum=",c)

	
>>> if ch ==2:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a-b
	print("difference=",c)

	
>>> if ch ==3:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a*b
	print("product=",c)

	
>>> if ch ==4:
	a = int(input("enter a:"))
	b = int(input("enter b:"))
	c = a/b
	print("quotient=",c)

	
>>> 
>>> 
>>> print('1.add')
1.add
>>> 
>>> print("Task 9 completed")
Task 9 completed
>>> 