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

# list1 = ['8','6','3','4','5','6','6']
# list2 = ['2','3','5','6','7','8','9']
# print(list1)
# print(list2)
# a = list((map(int,list1)))
# b = list((map(int,list2)))
# print(a)
# print(b)

# a = [12,34,56,78,12,56,12]
# c = [12,34,56,78,12,56,12]
# a.reverse()
# print(a)

# a.index()
# print(a)

# b = a.count(12)
# print(b)

# a.sort()
# print(a)

# a.clear()
# print(a)
# n = c[:5]
# for i in n:
#     print(i)
# print(n)

# e = [12,34,56,78,12,56,12,[12,45,67,[10,80]]]
# c = e[-1][-1][-2]
# print(c)

#Concatination of list
# a = [12,23,45]
# b = [34,65,76]
# r = a+b
# c = a*3
# print(r)
# print(c)

#List Alliasing
# d = a
# print(a)
# print(d)
# a[1]=30
# print(a)
# print(d)

#only add element in b list which are unique/not repeated
# a = [5,4,3,5,3,9,8,7,6,7]
# b = []
# for element in a:
#     if a.count(element)>1:
#         pass
#     else:
#         b.append(element)
# print(b)

#Nested List modification
# a = [[10,20,21],[34,29,[56,87]]]
# print("List Before Modi:",a)
# a[0][0] = 70
# a[1][2][0] = 30
# print("List After Modi:",a)


#Q) print the name of the studnets which have second lowest marks
names_score = [['a',10],['b',20],['c',10],
               ['d',50],['e',40],['f',20]]
scores=[]
for students in names_score:
    scores.append(students[1])

# [10,20,10,50,40,20]
sorted_scores = sorted(set(scores))
# [10,20,40,50 ]
second_lowest = sorted_scores[1]
# [20]

names_second_lowest = []
for students in names_score:
    if students[1] == second_lowest:
        names_second_lowest.append(students[0])

print(sorted(names_second_lowest))

second_highest = sorted_scores[-2]

names_second_highest = []
for students in names_score:
    if students[1] == second_highest:
        names_second_highest.append(students[0])

print(sorted(names_second_highest))

