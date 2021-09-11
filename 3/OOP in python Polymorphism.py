# Polymorphism is the ability of an object to take on many forms.
# Polymorphism refers to the way in which different object classes can share the same method name.

class Dog():
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + ' Says woof !!'
    
class Cat():
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + ' Says meow !!'
    
# here dog and cat both share a same method name speak

# So by Polymorphism we can use same method of different class in a program

bolt = Dog('Bolt') # Creat a object
nikky = Cat('nikky')

def sound(pet): # call method of different class by using a outside funtion 
    print(pet.speak()) # here pet is a local variable

sound(bolt)
sound(nikky)
print('-----------------------------')
#called method by using for loop 

for pet in [bolt,nikky]:
    print(type(pet))
    print(pet.speak()) # here pet is a global veriable 
    



