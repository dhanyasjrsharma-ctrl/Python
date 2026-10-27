"""operations with a file"""
#1. r -> read -> kisi bhi file ko sirf read kar skte h
#2. a -> append -> kisi bhi existing content ke last me new content add kar dega
#3. w -> write  -> 1.yadi file exist nahi karti h to file ko create kar dega or usme content daal dega 
#                  2.yadi file exist karti h or usme content bhi hi to old content new content se replace ho jaega
#4. x -> creates file only


"""read a file"""# koi mode nhi diya to default read mode 
# file = open("captain.py","r")
# print(file.read())
# file.close()

"""using 'w' mode"""
# file=open('spiderman.txt','w')# this file does not exist to ye  create kar dega
# file.write('this is a marvel file')
# file.close()

"""using 'a' mode"""
# file=open('spiderman.txt','a')
# file.write('this content is added at the last')
# file.close()

""" 'with' laga diya to file alag se close nahi karna padegi apne aap ho jaegi"""
# with open('spiderman.txt','r') as file:
#     print(file.read())


# with open('batman.txt','w') as file:
#     file.write('print this at last of the line')

"""import os"""#operating system
# we can remove any file using os
import os
os.remove('batman.txt')

