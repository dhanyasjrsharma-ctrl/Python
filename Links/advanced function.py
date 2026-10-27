#SOME ADVANCED FUNCTIONS
""" *args -> accepts arguments in form of tuples and give also in tuples """
#            args bana dene se baar baar parameters nhi dene padte h 
#            kisi bhi cheez ke pehle * laga do vo arg ban jaega
# def add (*a):
#     print(a)
# add(10,20,30)
# priority in functions-> pehle positional parameters aaenge fir advanced functions


# sum --> :
# def add(*a):
#     sum = 0 
#     for i in a:
#         sum+=1
#         return sum
#     print(add(10,20,30))

""" **kwargs--> accepts and gives the data in the form of dictionary - k w args - key word args"""
# def info(**details):
#     print(details)
# info(name="chacha", age = 40, gender="M", address="bhopal",wife= "chachi")

# def info(**details):
#     for key, values in details.items():
#         print(key,values)
# info(name="chacha", age = 40, gender="M", address="bhopal",wife= "chachi")


"""lambda -> iss function ka use karke humara koi bhi code ek line me aa skata h""" 
# add = lambda a,b: a + b # jab tak a,b nhi denge tab tak aage ka code execute nhi hoga

# make a lambda function which accepts 2 variable a=2 and b=2 but output as a^b 2^2 = 4
# power = lambda a,b : a**b 
# print(power(2,2))




