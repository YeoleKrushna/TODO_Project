print("Hello World")

p = "Hello"
print("e" not in p)

a = 2
b ='2'
print(a is b)

value = (1+1)*2**4//3+4-1
print(value)


b = 1000 
while b > 0:
    a = int(input(f"Enter the amount to withdraw (Available balance: {b}): "))
    if a <= b:
        b -= a 
        print(f"You've withdrawn {a}. Your remaining balance is {b}.")
    else:
        print("Insufficient balance. Try again.")
        break

i =1
while i<=3:
    print("Outer",i)
    i+=1
    j =1
    while j<=5:
        print("Inner",j)
        j+=1
print("he")

#range
c=range(5,0,-1)
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])



st="HEY"
y = len(st)
print(y)
ch = 0
while ch < y:
    print(ch, "=", st[ch])
    ch += 1

st = "GeekyShows"
for ch in st:
    print(ch)
else:
    print("Else exe")
print("Rest")

for i in range(3):
    print("Outr",i)
    for j in range(5):
        print("inner =",j)
print("Rest")

for i in range(10):
    if(i==5):
        continue
    print(i)
print("rest")



str = "Krushna"
a =len(str)
for i in range(a-1, -1, -1):
    print(str[i], end="")



str1 = "racecer"
b = len(str1)
a =""
for i in range(b-1,-1,-1):
   a += str1[i]

if str1 == a:
    print("It is palindrome")
else:
    print("Not palindrome")



s = " 7hello eve das cad qdwq-hey "
b = s.title()
c = s.upper()
e = s.islower()
f = s.isupper()
d = s.lower()
print(b,c,d,e,f,s.lstrip(),s.rstrip(),s.split("-"))

n = ("Hello", "," , "How", "Are" , "You", "?")
a = "".join(n)
print(n)
print(a)



#function for cheking Sub-string in String
def issubsequence(s,s1):
    i=0
    j=0
    while i <len(s1) and j <len(s):
        if s1[i]==s[j]:
            i+=1
        j+=1
    return i == len(s1)
s = "abcdefghijk"
s1 = "efg"
r = issubsequence(s,s1)
print(r)


text = "krushna"
if not text:
    print("Empty String")
else:
    for char in text.lower():
      if char in ("a","e","i","o","u"):
        print(f"{char } is vowel")
      elif not char.isalpha():
        print(f"{char} is not letter")
      else:
        print(f"{char} is a consonant ")




month = "Feb"
months = ("jan","march","may","july","Aug","oct","Dec")
monthss = ("april","june","sept","nov")
if month in months:
    print(f"{month} has 31 days")
elif month in monthss:
    print(f"{month} has 30 days")
else:
    print(f"{month} has 28 days"),




a=3
b=2
c=1

if a>b>c:
    print("Descending")
elif a<b<c:
    print("Ascending")
else:
    print("Not In Order")


#Finding Leap Year
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year %400 == 0:
                leap = True
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))
