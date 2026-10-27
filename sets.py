#3.sets
# denoted by {}
#empty set -> {} , set()
#if values inside curly braces are seperated by colons then it is a dictionary and if values seperated by commas then it is a set
#sets do not allow duplicacy
#sets does not contain any indexing #unordered #subscriptable
#heterogeneous but they do not allow boolean data types
#mutable

# s={}
# print(type(s))#dictionary

# s=set()
# s={1,2,3,4,5}
# print(type(s))#set

# s={1,2,3,4,5,6,7,8}
# print(s)

# item assignment and item adding is different
#item assignment kisi index or key pe hoti h or item adding har data structure mai ho sakti hai

# s={'hello',1,3.14,True}
# print(s)

#METHODS IN SETS

#1. .add # add a new value in set # adds only a single value
#item adding
# s={1,2,3,4,5,6,7}
# s.add(100)
# print(s)

# .update([]) # for adding multiple values in set
# s={1,2,3,4,5,6,7}
# s.update([100,45,35])
# print(s)

#2. REMOVING AN ELEMENT FROM THE SET
#a. .remove(element)
# s={1,1,1,2,3,3}#saare duplicate values hata dega output me vo kitni bhi baar ho ek hi baar bachegi
# s.remove(1)
# print(s)

#b. .discard(element)
# s.discard(6)# agar value exist nahi karti to it will give you exact same set bina kisi error ke

#c. .clear() #empty set milega

#ADVANCED METHODS IN SETS
# 1. Union -> sre elements between given sets
# 2.INTERSECTION -> common elements between sets
# 3. DIFFERENCE -> s1.difference(s2) -> s1 me h par s2 me nahi
# 4. SYMMETRIC DIFFERENCE -> common elements ko chhod ke jo bach rhe vo laa do

# s1={1,2,3,4}
# s2={1,2,6,7}
# print(s1.union(s2))

# s1={1,2,3,4}
# s2={1,2,6,7}
# print(s1.intersection(s2))

# s1={1,2,3,4}
# s2={1,2,6,7}
# print(s1.difference(s2))#3,4
# print(s2.difference(s1))#6,7

# s1={1,2,3,4}
# s2={1,2,6,7}
# print(s1.symmetric_difference(s2))

#Q. by using for loop create a set which contain all values of l but no value should repeat
# l=[1,2,1,2,1,3,3,3,4,5,6,7]
# s=set()
# for i in l:
#     s.add(i)
# print(s)




