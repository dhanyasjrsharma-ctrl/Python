# check whether all the list elements are making pairs or not(all the elements should make pairs )

nums = [3,2,3,2,2,2]
d = {} #{3:3,2:4}
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1

#Itni loop jisse i ke andar sirf values aaye

for i in d.values():
    if i % 2 !=0: #1 Pair -> 2 elements
        print('Not making pair.')
        break
        
else:
    print('Making Pair')

#break lgana padega kyoki agar by chance kisi element ka cout odd no. hai to break se aage badhega hi nhi 
#pehlle isme frequency count karenge or uske baad agr count even h means 2 se divide ho rha h to making a pair 
#else not making a pair
