# OOP :- OOP  stand for Object Oriented programming language. It s include object, class, constructor, inheritance etc. in programming language. OOP use in python to use OOP properties like:class, object etc. 

# Class :-
# # Class is a user defined data type/structure 
# Class contains data members and member functions
# Data members are variables that are part of the class, also called as attributes
# Member functions are functions that are part of the class, also called as methods
#  for Example:-
#  class class_name:
#       sttement  


# Object :- Object is an instance of class by which we can access the data members and member functions of the class. Withaut creating of object we are not using class.
# For Example:-
# object_name = class_name()

# Note :-

# A Single Class can have multiple objects/instances
# All the objects of a class share the same data members and member functions
# But the objects have different states i.e different values of data members
# self is a reference variable that refers to the current instance of the class
# class methods must have self as the first argument

# Class variable is also called Data Member and Attributes
# Function() is also called member function or methods
# Object  is also called instance
# instanciacing of class is called creating a class.
# method or function variable is called instance variable. 

"""
class syntax:
class ClassName:
    <statement-1> variables, function
    .
    .
    <statement-N>
object creation:
object_name = ClassName()
 
 using variable , function:
 object_name.class_variable_name/method
"""

class subject: #creating class
    a = 'nepali' # create attributes / class object 1
    b = 'english' # create attributes / class object 2
    c = 'math' # create attributes / class object 3
    def prnt(self):      # create method / function() 1   " def function_name(object)" self is also khown as object or instance
        print(self.c)  # calling attribute in function.  self.c means mark.a "it pass the output in object i.ee mark object"
    def eng(self):      # create method / function() 2
        print(self.b)   # calling attribute in function.
    def all(self):        # create method / function() 3
        print(self.a)     # calling attribute in function.

mark = subject() # creating object or intance
mark.prnt() # calling prnt() methods  in the class by using object.
mark.all() # calling all() methods in the class by using object.

# explanation of above code:- we are create one class i.e student. in the student class, we are create different attributes and method
# that method work to print the attribute in the class. after creating class we are call by using mark object or instance. after creating
# object, we are call the method by using object or instance. Self is use to indicate the object.

class cal: #create class cal
    a=4 #create attribute
    b=6
    def mul(self): #create method
        return self.a * self.b  # its retur the value of multiply in the calling object
   # you are notice this line of code
    def add(addition):
        return addition.a + addition.b # its retur the value of addition in the calling object

adde = cal() # creating intance 1
print(adde.add()) #printing return value of add() methods by using adde instance
multi = cal() # creating intance 2
print(multi.mul()) #printing return value of mul() methods by using multi instance

# in avobe code 1 class can be create that class calling of more object i.e multiple object share the methods or attribute of class.
