#1Q
def listofTuples(11, 12):
    return list(map(lambda x, y:(x,y), 11, 12))
list1 = [1,2,3]
list2 = ['a', 'b', 'c']
print(listofTuples(list1, list2))

def merge(list1, list2):
    merged_list = list(zip(list1, list2))
    return merged_list
list1 = [1,2,3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))

#2Q
list1 = [1,2,3,4,5,6,7,8]
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
result =tuple(zip(list1,list2))
print(result)
#3Q
list1=[23,45,26,35,35,55,44]
list2=sorted(list1)
print(list2)

#4Q
def filtereven(nums):
    if nums%2 !=0:
        return True
    else:
        return False
numbers =[23,11,25,53,44,56,35,56,48,38,68]
result=filter(filtereven,numbers)
for i in result:
    print(i)
    
