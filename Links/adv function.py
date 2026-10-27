'''args-accepts arguments in form of tuple
necessary to put a * to make anything a arg
args bana do to baar baar parameters nhi dene padhte hai 
anything can be a arg '''


# def add(*chacha):
#     print(chacha)
# add(10,20,30)
# priority in function - pehle positional parameters aayenge phir adv functions aayenge 

# def add(*chacha):
#     sum=0
#     for i in chacha:
#         sum =sum +i 
#     return sum 
#     print(sum)
# print(add(10,20,30))

'''
kwargs -accepts arguments in dictionary and gives iin dictionary 
necessary to put ** to make anything a kwarg 
kwarg bana do to keywords nhi dene padhte baar baar '''

# def info (**details):
#     for key, value in details.items():
#         print(key,value)
        
# info (name="Chacha", age=45, address="Bhopal",gender="M",wife="chachi")

"""
lambda functions:lambda keyword likhna jaruri hai taki python ko pata lage ki function ek line mai hoga  
yha pe function ka naam pehle likho, parameters do, aapko jo karwana hai parameters se vo karwao 

"""
# add= lambda a,b:a+b
# print(add(10,20))

# Q. make a lambda function which accepts two variable a=2 and b=3 but give output as a^b 
# power= lambda a,b:a**b 
# print(power(2,3)) 



