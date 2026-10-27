# 1. list
# "denoted by -> [] square brackets"
# l = [] empty list
# l = [10,20,30,40,50] #square bracket aa jaye or comma se values seperated ho to list
# print(l)
# print(type(l))

# l = [10,"name",'true',3.14]
# print(l)
# print(type(l))

#1.HEGTEROGENEOUIS DATA STRUCTURES - multiple types ke data ko store karwa skte h 
#2. duplicacy is allowed 
#3. list is ordered
#4. mutable- we can changewteh value in the list to assign any new value

# list = []empty list
# l = [10,20,30,40,50]
# l[3]=400 #item assignment
# print (l)
#l- 

#ITEM WISE LOOP
# l = [10,20,30,40,50]
# for i in l:
#     print(i)

#INDEX WISE LOOP
# l = [10,20,30,40,50]
# for i in range (len(l)): #i=0,1,2,3,4
#     print(i,l[i])
#     #i=index of a list
#     #l(i)=items at index

# l=[1,67,10,445,857,8,9]
# for i in l:
#     if i >15:
#         print(i)

#sum of all elements of the list
# l=[1,5,6,8,9]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

# l=[1,67,10,445,857,8,9]
# # for i in l:
# #     if i >15:
# #         print(i)
# for i in range(len(l)):
#     if l[i] >15:
#         print(i)


#slicing
#[start=0:stop-1:step=1](by default values)
# l=[10,20,30,40,50]
# print(l[1:4:1])

#methods in list
#1. .append() ->adds elements at the end of the list #can accept only one value at a time
# l = [10,20,30,40,50]
# l.append(100)
# print(l)

# #2. .extend()-> adds second list at the end of first list(can accept multiple values)
# l1=[10,20,30,40]
# l2=[50,60,70]
# l1.extend(l2)
# print(l1)

# #3. .insert(index,value)#jo index enter karenge vaha pe given value add ho jaegi or baki values shift ho jaengi
# l1.insert(1,100)
# print(l1)

# #4. .pop(index)#jo index enter karenge vo value list se hat jaegi
# l1=[10,20,30,40,50]
# l1.pop(1)
# print(l1)

# #5. .remove(element)
# l1=[1,5,5,2,3,4,5,6]
# l1.remove(5)#agar ek value multiple times h to first occurance remove hoga
# print(l1)

# #6. len()->list length batata h
# l1=[1,2,3,4,5,6,7,8]
# print(len(l1))

#QUESTIONS
#1. Accept list elements and reprint it
#part1 accept elements
# n=int(input("enter the size of the list:"))#5
# l=[]
# for i in range(n): #0,1,2,3,4
#     element=input("enter elements of your list")
#     l.append(element)
# print(l)


# n=int(input("enter the size of the list:"))#5
# l=[]
# for i in range(n): #0,1,2,3,4
#     element=input("enter element {i} for your list")
#     l.append(element)
# print(l)

#2. reverse a list without using slicingn=int(input("enter the size of the list:"))
# l=[10,20,30,40,50]
# reverse= []
# for i in range(len(l)-1,-1,-1):
#      print(l[i])
#      reverse.append(l[i])
# print(reverse)




#3. print positive and negative elements of a list
# l=[10,-9,20,30,-12,15]
# neg = []
# pos = []
# for i in l:
#     if i<0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print(neg)
# print(pos)


#BUBLE SORT :- ek baar me ek element ko pick karte h or use baki elements se compare karate h
# l=[1,5,3,7,4,10]#used to arrange in ascending and descending order
# for i in range(len(l)):
#     for j in range(i+1,(len(l))):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# l=[1,5,3,7,4,10]
# for i in range(len(l)):
#     for j in range(i+1,(len(l))):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)




# #4.print list in ascending and descending order # buble sort is used
# l = [10,60,5,46,68,23]
# for i in range(len(l)):
#     for j in range(i+1,(len(l))):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# l = [10,60,5,46,68,23]
# for i in range(len(l)):
#     for j in range(i+1,(len(l))):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

#5. largest element from the list
# l=[2,96,69,77,145,20]
# max=l[0]#pata nhi h ki max kitna h to maan liya ki list ka pehla element hi max hai,0 is the index of first element
# for i in l:
#     if i>max:
#         max=i
# print(max)
# #or
# l=[2,96,69,77,145,20]
# max = l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
#         index=i
# print(f"max element from the list is {max} and at index {index}")

#6. mean/average of list elements
# l=[1,5,6,8,9]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum/len(l))

#7. print largest and second largest element of the list
# l=[10,5,20,15]
# largest=l[0]#20
# s_largest=l[0]#15

# for i in l: #i->15
#     if i>largest:#15>20
#         s_largest=largest
#         largest=i

#     elif i>s_largest:
#         s_largest=i
# print(largest,s_largest)

#i = 0  1  2  3
# l=[10,5,20,15]
# largest=l[0]#20
# s_largest=l[0]#10

# index=0 #2
# sindex=0 #0
# for i in range (len(l)): #i->2
#     if l[i]>largest:#20>10
#         s_largest=largest
#         largest=l[i]

#         sindex=index
#         index=i

#     elif l[i]>s_largest:
#         s_largest=l[i]
#         sindex=i
# print(largest,s_largest)
# print(index,sindex)

#list is palindrome or not
#method - 1
# l=[1,2,2,1]
# rev_l=[]

# for i in range(len(l)-1,-1,-1):
#     rev_l.append(l[i])

# if l==rev_l:
#     print("list is palindrome")
# else:
#     print("not palindrome")

#method 2
# l=[1,2,2,1]
# for i in range(0,len(l)):
#     if l[i]==l[len(l)-1-i]:
#       print("palindrome")

# l=[1,2,2,1]
# for i in range(0,len(l)):
#     if l[i]!=l[len(l)-1-i]:
#      print("not palindrome")
#      break
# else:
#    print("list is palindrome")

#method 3 ## THIS IS WRONG
# l=[1,2,2,1]
# for i in range(0,len(l)):
#  for j in range(len(l)-1,0):
#      if l[i]==l[j]:#ye sirf last or first value ko check karega yadi [1,2,3,1] hua to bhi palindrome bata dega kyoki bich wali values check kiye bina hi if condition true ho jaegi
      
#       print("palindrome")
#      else:
#        print("not palindrome")



### ENUMERATE ### Index ke saath unki values bhi dega
# list -> [10,20,30,40,50],index -> 0,1,2,3,4
# L=[10,20,30,40,50]
# for index,value in enumerate(L):#do chize saath me ek variable me store nhi ho sakti to do variable banana padega ek me index aaega or ek me value , ye kaam enumerate karta h
#     print(index,value)

# for index,value in enumerate(L):#aar indexing 1 se start karani ho to inddex +1 print karado
#     print(index+1,value)

# l=[1,2,3,4,5]
# l2=[1,3,4,5,6]
# new = [] #common elements rakhne h
# for i in l:
#     for j in l2:
#         if i==j:
#             new.append(i)

# print(new)


# Q. you have a list [1,2,3,4,5] and you have to rotate the list by k elements where you have variable k=2
# l=[1,2,3,4,5]
# k = 2 
# for i in range(k):
#     last=l[-1]#storing last value of the list
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=last
# print (l)


#you have a list [1,1,1,2,2,3,3,4,4,5,5,6] , count its frequency
d={}