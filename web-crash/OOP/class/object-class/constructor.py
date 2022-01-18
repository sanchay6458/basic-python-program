#constructor :- Construcor is a special method that is called when an object is created.
# It is used to initialize the state of the object.

# Class variable is a variable that is shared by all the objects of a class.
# Class variable is accessible by all the objects of the class.
# Class variable is not a part of the object.
# Class variable is also known as static variable.

# Instance variables are variables whose value is assigned inside a constructor or method with self
# Instance variables are accessible by all the objects of the class.
# Instance variable is a part of the object.
# Instance variable is not shared by all the objects of the class

#__str__ is a special method that is called when an object is converted to a string.
# It is used to return a string representation of the object.

# syntax:-

# """class class_name:
#    def __init__(self, argument):
#        statement 
# obj = class_name()"""

# example:-
class boy: #create class
    a= 'sanchay' # create attribute
    def __init__(self, a): # Create constructor, object= self and argument = a
        self.a = 'sanchay' + a # object.instance varible = string + argument
good = boy('good') # creating object
print(good.a) #object.instance variable


class math:
    a = 5
    b = 6
    def mul(self):
        self.c = self.a * self.b
        return self.c 
    def __init__(self):
        self.add = self.a+self.b
    def __str__(self):
       return self.add
        

ad = math()
print(ad.add) 
print(ad.mul())

class Friend:
    def __init__(self):
        self.job = "biki"

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job

obj1 = Friend()
obj2 = Friend()
print(obj1.job) # calling by constructor
obj1.setJob("computer") # calling by method by passing argument
obj2.setJob("engineer") # calling by method by passing argument

print(obj2.job) # calling by method variable
print(obj1.job) # calling by method variable




