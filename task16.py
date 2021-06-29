## create a list lambda function that multiplies arugument x with argument x with argument y

r = lambda x, y : x * y
print(r(10, 6))

## write a python program to create Fibonacci series to n using Lambda

from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                 range(n-2), [0, 1])

print(fib(11))

## 3Q
nums = [2,3,6,5]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

##4Q
list1=[2,3,6,5,45,56,35,52,26,24]
print(list1)
list2=list(map(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))
list2=list(filter(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str, list2)))

##5Q

list1=[2,3,6,5,4,9,868,23,36,35,34,39,75,65]
print(list1)
list2=list(filter(lambda j:j%2==0,list1))
print("Result :")
print(len(list2))
