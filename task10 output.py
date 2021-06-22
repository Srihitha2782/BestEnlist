Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:/Users/Srihitha/Downloads/task10.py ================
>>> Srihitha = User('Srihitha', 19, 'Female')
>>> Srihitha.show_details()
Personal Details

Name  Srihitha
Age  19
Gender  Female
>>> 
================ RESTART: C:/Users/Srihitha/Downloads/task10.py ================
>>> Srihitha = Bank('Srihitha', 19, 'Female')
>>> Srihitha.name
'Srihitha'
>>> Srihitha.age
19
>>> Johan.gender
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Johan.gender
NameError: name 'Johan' is not defined
>>> Srihitha.gender
'Female'
>>> 
================ RESTART: C:/Users/Srihitha/Downloads/task10.py ================
>>> 
================ RESTART: C:/Users/Srihitha/Downloads/task10.py ================
>>> Srihitha = Bank('Srihitha', 19, 'Female')
>>> Srihitha.deposit(100)
Account balance has been updated :  100
>>> Srihitha.deposit(400)
Account balance has been updated :  500
>>> 
================ RESTART: C:/Users/Srihitha/Downloads/task10.py ================
>>> Srihitha = Bank('Srihitha', 19, 'Female')
>>> Srihitha.deposit(400)
Account balance has been updated : $ 400
>>> 
================ RESTART: C:/Users/Srihitha/Downloads/task10.py ================
>>> Srihitha = Bank('Srihitha' ,19, 'Female')
>>> Srihitha.deposit(100)
Account balance has been updated : $ 100
>>> Srihitha.withdraw(5)
Account balance has been updated : $ 5
>>> Srihitha.withdraw(300)
Insufficient Funds : Balance Available : $ 5
>>> Srihitha.withdraw(5)
Account balance has been updated : $ 5
>>> Srihitha.withdraw(5)
Account balance has been updated : $ 5
>>> 
================ RESTART: C:/Users/Srihitha/Downloads/task10.py ================
>>> Srihitha = Bank('Srihitha', 19, 'Female')
>>> Srihitha.withdraw(900)
Insufficient Funds : Balance Available : $ 0
>>> Srihitha.deposit(1000)
Account balance has been updated : $ 1000
>>> Srihitha.withdraw(900)
Account balance has been updated : $ 900
>>> Srihitha.show_details()
Personal Details

Name  Srihitha
Age  19
Gender  Female
>>> Srihitha.view_balance()
Personal Details

Name  Srihitha
Age  19
Gender  Female
Account balance has been updated : $ 900
>>> 
>>> Successfully retrived the price from flipkart
SyntaxError: invalid syntax
>>> Successfully retrived the price from Flipkart and Amazon
SyntaxError: invalid syntax
>>> price available at Flipkart is 56,999
SyntaxError: invalid syntax
>>> price available at Amazon is 62,555