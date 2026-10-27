# """ CLASS IN OOPS """

# # when you run your code you always initialize your class
# class Factory: # use first letter capital whenever you are creating a class 
#     print("hello how are you")
# Factory () # this will not run your code inside class
# # classes are not like functions , call karo ya na karo class ko 
# # kitni bhi baar call karlo ek hi baar chalega

# class Animal :
#     # attributes -> a variable defined inside a class is attribute
#     name="long_neck" 
#     # method -> functions defined inside a class is a method
#     def speak():
#         print("hello i am a giraffe")

# print(Animal.name) # calling an attribute
# Animal.speak() # calling a method


# """ OBJECTS IN OOPS """

# class Animal:
#     name="bear"

#     def speaks():
#         print("bear is roaring")
# obj= Animal() # this is how you create an object
# obj2= Animal()
# # object has all powers in its class 
# print(obj.name)
# print(obj2.name)
# obj.speak() # here we will send one argument by default , error occured
# multiple objects can be created in the same class


""" CONSTRUCTORS""" # parameters ko access karne ke liye constructor banan
# constructor function
# whenever you'll call this function will run
# class Bag_factory:
#     def __init__(self): # self will capture the location of objects or your class itself # double under score before and after init ,
#         #__init__is important for constructor function
#         # init -> initialise
#         print(self)
#         print("how are you")

# obj=Bag_factory()
# Bag_factory()
# # input lena hai to constructor function ke andar 

# class Bag_factory:
#     def __init__(self,material,zips,pockets):
#         self.material=material
#         self.zips=zips
#         self.pockets=pockets
#     def showdetails(self):
#             print("your bag details are")
#             print("material is",self.material)
#             print("total zips are",self.zips)
#             print("total pockets are",self.pockets)

# campus=Bag_factory("leather",3,4)
# hrx=Bag_factory("parachute",2,4)

# campus.showdetails()# jo object showdetails ko call karega usi ki info upar self ko milegi
# hrx.showdetails()

# # TYPES OF ATTRIBUTES AND METHODS

# class Registration:
#      school_name="sheryians" #class attribute

#      def __init__(self,name,age,email,number):
#           self.name=name # object attribute/instance attribute
#           self.age=age
#           self.email=email
#           self.number=number

#     # object method/instance method -> object ki location accept karta h
#      def details(self):# self will take obj location
#         print("we will provide details")

#      @classmethod 
#      def register(cls):# cls will take class location
#           print("you have accessed the class location")

#      #static method
#      @staticmethod
#      def hello(): # don't capture any location 
#           print("no location is sent")




# class Registration:
#     total_students=0 # class attribute
     
#     def __init__(self,name,age,studentclass):
#         self.name=name # object attribute
#         self.age=age
#         self.studentclass=studentclass
#         self.registered=False
    
#         if self.age>20:
#              print(f"registration failed : {self.name}")
#         else:
#              self.registered=True
#              Registration.total_students += 1
#              print("registration successfull : {self.name}")

#     def show_details(self):
#         if self.registered:
#               print(f"total students : {Registration.total_students}")
#               print(f"your details are: /n")
#               print(f"name: {self.name}")
#               print(f"age : {self.age}")
#               print(f"class : {self.studentclass}")
#         else:
#               print("sorry no such student exist")

# student1=Registration("rohan",19,12)
# student2=Registration("vikas",15,10)
# student3=Registration("dhanya",22,12)

# student1.show_details()

# """ OOPS PILLARS """
# # INHERITANCE
# # POLYMORPHISM
# # ENCAPSULATION
# # ABSTRACTION

"""Inheritance"""
## single level inheritance ##
# multi level -> ek parent or number of child classes

# class Animal:
#      name="ape"

#      def speak(self):
#           print(f"{Animal.name} is speaking")

# class Human(Animal):
#      pass

# obj1 = Animal ()
# obj2 = Human()
# print(obj2.name)
# # an object of your child class can access all the attributes and methods of your parent class

# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#         def details(self): # details function of animal class is now overrided by human class details method
#             ## method overriding occurs in inheritance only
#             # dono hi parent and child class me same name ka function create karte h to child class parent class ko override kar leti h
#             super().details()
#             print(self.name)
#             print(self.age)

# class Human(Animal):
#     def __init__(self,name,age,mail,number):
#         super().__init__(name,age)# used when you still need some new inputs
#         # super ().__init___ki jagah direct self. bhi likh skte h
#         self.mail=mail
#         self.number=number
# # name or age parent class me initialise hoga or mail and number child class me 

# class Robot(Human):# multi level -> ek parent and multiple child classes
#     def __init__(self,name,age,mail,number,chs):
#         super().__init__(name,age,mail,number)
#         self.chs=chs


        
# obj=Human("Akarsh",25,"hello@123.com", 1234567890)
# # human class is using the constructor of animal class
# obj2=Animal("Dhanya",19)

# obj.details()
# obj2.details()

# # multiple inheritance -> one child class and multiple parent classes
# class Factory:
#     def __init__(self,material):
#         self.material=material

# class Factory2:
#     def __init__(self,material,zips,pockets):
#         self.zips=zips
#         self.pockets=pockets

# class BhopalFactory(Factory2,Factory):
#     def __init__(self,material,zips,pockets):
#         Factory.__init(material)
#         Factory2.__init__(zips.pockets) # yaha agar super(). karke call karte to pehli parent class ki details aati

""" ENCAPSULATION """ 
# access modifiers
# public attributes and methods
# protected
# private -> using double underscore before any attribute or method makes them private and no one can access them outside our class


# class Animal:
#     name="lion"
#     __code="138ihuhdd" 

#     def speak (self):
#         print(f"{Animal.name} roars")
#     @classmethod
#     def __imei(cls):
#         return cls.__code

# obj= Animal()
# print(obj.__imei())

""" POLYMORPHISM """


""" method overloading -> whenever you have two same name methods inside a single class and 
both have different functionalities then it is known as method overloading"""

class Animal:
    def hello (self):
        print("how are you")

    def hello(self):
        print("what about you")

"""method overriding -> when we have same name methods inside a parent class and a child class , 
 resulting your child class object cannot acess the method of parent class this is concept of method overriding"""

"""ABSTRACTION"""

# from abc import ABC , abstractmethod 
# class Rules(ABC):

#     @abstractmethod
#     def perimeter(self):
#         pass
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Rules):
#     def __init__(self,side):
#             self.side=side

#     def area(self):
#             print(f"area is {self.side * self.side}")
#     def perimeter(self):
#             print(f"perimeter is {self.side * 4}")  

# obj=Square(5)  


"""DUNDER METHODS"""
"""
sabhi dunder methods me double underscore lagta h 
inko . karke nhi lkhna padta ye khud se run ho jate h 
whenever we have to perform arithmetic operations 
"""
class Human :
    def ___init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return(f"hello you are {self.name} and your age is {self.age}")
    
    def __add__(self,other):
        return self.age + other.age
    
obj=Human("harsh",23)
obj2=Human("dhanya",19)
print(obj+obj2) # this will trigger __add__method
print(obj) # this will trigger the __str__ method