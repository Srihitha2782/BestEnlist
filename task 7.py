
>>> # creating a function getting two integer inputs from user
>>> a = int(input("Enter an integer:"))
Enter an integer:5
>>> b = int(input("Enter an integer:"))
Enter an integer:9
>>> print
<built-in function print>
>>> print("sum of a and b:",a+b)
sum of a and b: 14
>>> print("difference of a and b:",a-b)
difference of a and b: -4
>>> print("multiplication of a and b:",a*b)
multiplication of a and b: 45
>>> print("division of a and b:",a/b)
division of a and b: 0.5555555555555556
>>> 
>>> # create a function covid()
>>> def covid(patientname,bodytemperature):
	if bodytemperature<str(0):
		default = str(98)
		print("patientname is",patientname,"bodytemperature is",default)
	else:
		print("patientname is",patientname,"bodytemperature is",bodytemperature)
		covid("srihitha","")
		covid("srihitha","99")

		
>>>
patientname is srihitha bodytemperature is 98

patientname is srihitha bodytemperature is 99

print ("Task 7 completed")

Task 7 completed
