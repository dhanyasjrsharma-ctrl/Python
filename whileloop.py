#While loop tab tak chalegi jab tak condition true hai:::
#QUESTION 1
# i=0
# while i < 11:
#     if i == 5:
#         break 
#     print(i)
#     i += 1

#QUESTION 2
# num= int(input("enter a number: "))
# i=0
# sum=0
# while  num > 0:
#     last = num %  10
#     print(last)
#     sum = sum + last
#     num = num // 10
# print(f"The sum of the number is: {sum}")

#QUESTION 3
# num= int(input("enter a number: "))
# num2=num
# pal=0
# while  num > 0:
#     last = num %  10
#     pal = pal *10 + last
#     num = num // 10
# if pal == num2:
#         print("Palindrome")
# else:    
#         print("Not Palindrome")

#QUESTION 4
# num= int(input("enter a number: "))
# num2=num
# power = len(str(num))
# arms=0
# while  num > 0:
#     last = num %  10
#     arms = arms + last ** power
#     num = num // 10
     
# if arms == num2:
#         print("Armstrong")
# else:    
#         print("Not armstrong")

#QUESTION 5
# num= int(input("enter a number: "))
# sum = 0
# for i  in range(1,num):  
#     if num % i == 0:
#         sum += i
# if sum == num:
#     print(f"{num} is perfect number")
# else:
#     print(f"{num} is not perfect number")

#QUESTION 6
# rows = 5
# for i in range(1, rows + 1):
#     print("*" * i)

#Q 1.num is armstrong or not # same as question 4

# num = int(input("enter your num"))
# copy=num
# power=len(str(num))#3
# sum=0
# while num>0:
#     last = num%10
#     sum=sum+last**power
#     num=num//10
# if copy == sum:
#     print(f"{copy} is an armstrong number")
# else:
#     print(f"{copy} is not an armstrong")


# seperate teh digits of num 256
# a= int(input("enter your number"))
# while a>0:
#     print (a%10)
#     a = a//10

# # and if we have to reverse the number and then seperate the digits
# a= int(input("enter your number"))
# while a > 0:
#     rev = 0
#     rev = rev * 10 + a//10 
#     a= a//10
#     print (rev)

# # check a num palindrome or not
# a = int(input("enter a number"))
# copy = a
# rev = 0
# while a > 0 :
    
#     rev = rev * 10 + a % 10
#     a = a//10

# if copy == rev:
#     print ("palindrome")
# else :
#     print("not palindrome")

# random numbr guessing game using while loop
# import random 
# num = random.randint(1,10)
# tries = 0
# while True:
    
#     guess = int(input("guess your number between 1 to 10 :"))

#     if num == guess:
#         tries += 1
#         print(f"you are right and you guessed the number in {tries} tries")
#         break
#     elif num > guess:
#         print("guess a little higher")
#     elif num < guess :
#         print("guess a little lower")
    

# n = int(input("Enter n: "))

# i = 1
# smallest = int(input("enter a refrence no. num:- "))

# while i <= n:
#     num = int(input("Enter number: "))

#     if num < smallest:
#         smallest = num

#     i += 1

# print("Smallest =", smallest)

n = int(input("Enter n: "))

i = 0

while i < n:
    num = int(input("Enter number: "))

    if i == 0:
        smallest = num
    elif num < smallest:
        smallest = num

    i += 1

print("Smallest =", smallest)