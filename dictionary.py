#DICTIONARY
# [] lists
# {} -> dictionary

# keys - value pairs
# keys=Index
# keys cannot be duplicate
#but values can be duplicate
#eg. {1:10,2:20,3:30}# : -> seperator of keys and values
# keys can be numbers or alphabets 
#heterogeneous
#mutable

# d={1:10,2:20,3:30}
# print(d[1])#10

# d={'a':10,'b':20,'c':30,'d':40}
# #print 40
# print(d['d'])
# #yaha per e print karaya to error aaega , but...
# d['e']=100#item assignment , e ko ek value assign kar di
# print(d)

# d={'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 100}
# d['e']=200
# print(d)


# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# info['age']=25 #item assignment
# print(info)

## Methods in dictionary ##

 #1. .values() -> sirf dictionary ki values
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# print(info.values())

# #2. .keys() -> sirf dictionary ki keys
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# print(info.keys())

# #3. .items() -> agar values or keys dono chahiye hai to
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# print(info.items())

#4. .pop() -> it accepts key and remove keys and values both 
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# info.pop('name')
# print(info)

#5. len -> tells length of the dictionary # jitni keys unti length
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# print(len(info))

#6. traversing - for writing all keys and values seperately (keys values) 
# info={'name':'rahul','age':21,'marks':50.25,'present':True}
# for i in info: #i -> keys
#     print(i,info[i]) #info[i] -> values

#you will only get values from the dictionary
# for i in info.values():
#     print(i)

#7. .update-({key:value}) can update multiple values as well
# d={1:100,2:200,3:900}
# d.update({2:500})
# print(d)

# #8. .clear() removes all the elements...single udhana hai to pop ....puri udhana hai to clear 
# d={1:100,2:200,3:900}
# d.clear()
# print(d)

# del d 
# isme permanentely remove ho jati hai dictionary ....mtlb kahi nhi store hoga pura gayab 
# it is a keyword not a function or a method 



# QUESTIONS:
# two lists are given,make 1 list keys and other values 
# if dono ke length same hai to hi ye loop valid hai 
# l=[1,2,3,4,5,6]
# l2=[10,20,30,40,50,60]
# d={}
# for i in range(len(l)):
#     d[l[i]]=l2[i]
# print(d)

# a list is given,make the indexes as keys and elements present on those indexes as values 
# l=[10,20,30,40]
# d={}
# for i in range (len(l)):
#     d[i]=l[i]
# print(d)

# # merge two dictionaries d1 ke piche add kardo d2 ko 
# d1={'a':10,"b":20}
# d2={"c":30,'d':40}
# d1.update(d2)
# print(d1)

# # not in is a membership operator 
# for i in d2:
# # yha pe d2 mai c aa rha hai 
#     if i not in d1:
#         d1[i]=d2[i]
# print(d1)

# # ye ek single line mai bhi ho sakta hai
# d1={'a':10,"b":20}
# d2={"c":30,'d':40}
# d1.update(d2)
# print(d1)

# # random list is given with multiple values,count karna hai konsi values kitni baar aa rhi hai in a dictionary 
# # frequency counter 
# l=[1,1,1,1,2,2,3,3,3,4,7,7,7,7,8,9,9,9]
# d={}
# for i in l:
#     if i not in d:
#         d[i]=1
# #1 (pehla wala),d mai nhi hai to vo d mai 1 add ho jayega 
# #abh 1 baar one to aa gya to abh d mai 1 to hai 
# #to if nhi chalega or else chalega jisme jo current value hai usme +1 ho jayega 
#     else:
#         d[i]=d[i]+1
# print(d)


