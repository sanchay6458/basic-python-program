# inheritance :- Adovped the all properties (like: data member and method) of pairent class to the chield class. we can say that
# pairent class share all properties chield class from pairent class.

# Pairent class = Base class or Super class
# Child class = Sub class or Sub clas

# exaple:-

class smart:  #pairent class create
    b='sanchay'
    c= 'smart'
    a= 3
    b=4
    def mul(self):
        return self.b
        e = 5
        return e
class good(smart):  #chield class create of mart class
    def add(self): # create method in chield class
        return self.a + self.b #use pairent class attribute

obj = good() #create object for chield class good
print(obj.add()) # calling the method in chield class


