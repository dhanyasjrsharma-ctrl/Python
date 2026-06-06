
a=2
b=7
#arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#reltional operators
print(a==b) #false
print(a!=b)#true
print(a>b)#false
print(a>=b)#false
print(a<=b)#true

#assignment operators
num=20
num=num+10 #either this or below line are same 
num += 10 #same #if we write both then its two times same command
print("num:",num) 

#logical operators
a=50
b=30
print(not False)
print(not(a>b))

val1=True
val2=False
print("and operator:",val1 and val2)
print("or operator:", (a==b)or(a>b))

#TYPE CONVERSION
a=2
b=4.25
sum = a+b
print(sum)

m="2"
n=4.25
sum =a+b
print(sum) #not possible to add string and float

p=int("2")
q=4.25
print(type(a))
print(a+b)

int("5")
val=input("enter some value:")
print(type(val),val)