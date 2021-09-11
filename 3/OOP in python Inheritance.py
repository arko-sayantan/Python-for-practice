# Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another


class Animal(): # perent class
    
    def __init__(self):
        print('Animal created !!')

    def eat(self):
        print('I eat grass.')

# Ani = Animal()
# Ani.eat()
    
class Dog(Animal): # this our child class and 
                    # we want the charectarestic of perent class
                    # Also see in child class.
    def __init__(self):
        Animal.__init__(self) # we inherited the Animal class in Dog class
        print('Dog created!!')
        
    # overwritting a method 
    def eat(self):
        print('Dog love bones !!')
    
    def bark(self): #new Method for Dog class.
        print('Woof !!')

dg = Dog()
dg.eat()
dg.bark()

