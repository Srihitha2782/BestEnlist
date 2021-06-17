

## initializing the dictionaries
fruits = {"apple": 2, "orange" : 3, "tangerine" : 5}
dry_fruits = {"cashew": 3, "almond": 4, "pistachio": 6}
## updating the fruits dictionary
fruits.update(dry_fruits)
## printing the fruits dictionary
fruits.update(dry_fruits)
## printing the fruits dictionary
## it contains both the key: value pairs
print(fruits)

## python program to remove the key from the dictionary
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)

#python program to Map two lists into a Dictionary

keys = ['name', 'age', 'job']
values = ['John', '25', 'Developer']
myDict ={k: v for k, v in zip(keys, values)}
print("Dictionary Items : ", myDict)

# python program to find the length of set
set1 = set()
# Adding element and tuple to the set
set1.add(8)
set1.add(9)
set1.add((6,7))
print("The length of set is:", len(set1))

# python program to remove the intersection of a 2nd set from the 1st set

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("\nRemove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print("sn1: ",sn1)
print("sn2: ",sn2)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("\nRemove the intersection of a 2nd set from the 1st set using -= operator:")
sn1-=sn2
print("sn1: ",sn1)
print("sn2: ",sn2)

print("Task 6 completed")
