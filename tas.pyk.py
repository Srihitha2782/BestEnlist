try:
    print(x)

except NameError :
    print("Name error")

# Calculator

a = int(input("Enter 1st Number "))
b = int(input("Enter 2nd Number "))

c = input("Enter operation ")

try:
    if(c=="+"):
        print(a+b)
    elif(c=="-"):
        print(a-b)
    elif(c=="*"):
        print(a*b)
    elif(c=="/"):
        print(a/b)

except:
    print("Wrong Number")
finally:
    print("Thank you for using calculator ")


## print one message if the try block raises a NameError and another for oth

try:
    print()
except NameError:
    print("Name error")
else:
    print("Other type of error")
print()
## When try-except scenarip is not required
print("try catch is needed only if excepted error is small and does not affect the program, in case of fatal errors try catch block is not recommended")
print()

# Try getting an input inside the try catch block

try:
    n = int(input("Enter a number"))
    print(n)
except:
    print("Sorry mam")


    print("Task completed")
