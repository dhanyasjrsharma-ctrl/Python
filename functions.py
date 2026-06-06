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





