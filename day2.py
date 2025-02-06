#List
a = [10,20,30,-50,'HELLO']
# print(a,id(a))
# print(a[1])
# a[1]=40
# print(a[1])
# print(a,id(a))

# for element in a:
#     print(element)

# n = len(a)
# i = 0
# while i<n:
#     print(i, "=",a[i])
#     i+=1

#Deletion in list
# del a[1]
# print(a)
# del a
# print(a)

a = [10,20,-12,"HELLO"]
# print(a)
# a.append(100)
# print(a)

#append() adds one thing at a time, while extend() adds multiple things at once from an iterable.

# a.append([40,30,20])
# print("After Append List")
# print(a)
# a.extend([33,44,55])
# print("After Extend List")
# print(a)

# a=[]
# n = int(input("Enter Number Of Elements:"))
# for i in range(n):
#     a.append(int(input(f"Enter Element {i}:")))
# print(a)


# for elements in dir(list):
#     if '__' in elements:
#         pass
#     else:
#         print(elements)

#insert methods
# a = [10,20,30,10,90,'Hello']
# print('Before',a)
# a.insert(3,'Subs')
# print('After',a)

#pop method
# a.pop(3)
# print(a)
#only .pop() delete last element
# a.pop()
# print(a)

#remove method
# a.remove(10)
# print(a)
#it will remove first occurance of 10

# b = [9,5,4,3,8,5,7]
# b.remove(5)
# c = int(''.join(map(str, b)))
# print(c)
# b.remove(5)
# b.insert(1,'5')
# d = int(''.join(map(str, b)))
# print(d)
# if c > d:
#     print(c, "is greater number")
# else:
#     print(d, "is greater number")

list1 = ['8','6','3','4','5','6','6']
list2 = ['2','3','5','6','7','8','9']
print(list1)
print(list2)
a = list((map(int,list1)))
b = list((map(int,list2)))
print(a)
print(b)


