#function ka naam=variable naam
# def greet(): #function defining
#     name = input("enter your name:- ")
#     print(f"hello {name} ")
# greet() #function call (function jitni baar call karenge utni baar print ho jaega)

# def greet(name):#parameters(function define karte time)
#     print(f"hello {name} ")
# greet("Dhanya") #arguments(function call karte time)

#Q. print greatest between two variables
# def greatest():
#  a=int(input("enter first no :-"))
#  b=int(input("enter second num:-"))
#  if a>b:
#     print("a is greater than b")
#  elif b>a:
#     print("b is greater than a")
#  else:
#     print("both are equal")
# greatest()

#Q. check num palindrome or not
# def palindrome():
#     name=input("enter your name :-")
#     reverse = name[::-1]
#     if name==reverse:
#         print(f"{name} is palindrome")
#     else:
#         print(f"{name} is not palindrome")
# palindrome()

#RETURN STATEMENT
# def add():
#     a=10
#     b=20
#     c=a+b
#     return c
# print(add())


# def greet():
#     return"hello"

# def add():
#     print(greet())
#     a=10
#     b=20
#     return(add())

#PARAMETERS AND ARGUMENTS
# def add(a,b): #functions define karte time parameters use karte h
#     print(a+b)
#     add(10,20)#function call karte time arguments use karte h 

# def add(a:int, b:int):
#     print(a+b)
# add(10,10)# string denge to bhi kuchh change nhi hoga

# def add(a,b=0):#default parameters #dono ko bhi default bana sakte h a and b
#     print(a+b)
# add(10)
# add(10,12)#default value kuchh bhi set kar sakte h 


#Q. accept a parameter named as "n" and print factorial of "n"using function

# def fact(n:int):
  
#   fact=1 #factorial ki value kabhi zero nhi rakhte kyoki usme zero ka multiply nhi hota h
#   for i in range(1,n+1):
#    fact*=i #shorthand operator
#   return fact
# print(fact(5))


#KEYWORD ARGUMENTS
# def info(name,gender,age,address):
#     print(name)
#     print(gender)
#     print(age)
#     print(address)

# info(gender='M',age='52',address='bhopal',name='mukesh')


#palindrome or not
# def palindrome(num):
#     copy=num
#     rev=num
#     while num>0:
#         last = num%10
#         rev = rev * 10 + last
#         num = num//10

#     if copy==rev:
#             print(f"{copy} is a palindrome number")
#     else :
#             print(f"{copy} is not palindrome number")
# palindrome(num=1221)

#RECURSION 
#FUNCTION CALL ITSELF
# 1. def display(num): #num=1s
#     if num>10:
#         return
#     print(num)
#     display(num+1)

# display(1)

# 1. def display(num):
#     if num<1:
#        return
#     print(num)
#     display(num-1)#function calling itself

# display(10)

#FACTORIAL USING RECURSION
# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num *factorial(num-1)
# print(factorial(5))

#FUNCTION BACKUP
# def add(a=5,b=8):#default parameters assign kar dete h to function call me sirf add() likh do 
#     print(a+b)
# add(5,9)#yaha wpas se values de di to inhi ko consider karega upar wale ko nhi 

# def info(name,age):
#     print(name , age)
# # info("rahul",25)
# info(age=18,name="rahul")

#RETURN KEYWORD
# def info(name,age):
#     return(name,age)
# x=info(name="rahul",age=18)
    
# print(x)

# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return(fact)
# print(fact(5))


