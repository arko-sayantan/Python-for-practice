#class keyword use for user defined object 
# class is blueprint of the object 
# Dog is a attribute, atribute is a charectarestic of the object 

class Dog(): #creat a class ehich name is SampleWord
   
    #class object attribute --> Same for any instance of a class.
    
    species = 'Mammal'
    
    # user-define the attribute.
    
    def __init__(self,breed,name): # self use to connect method with the instance of the class(my_sample)
        
        # We take the parameter/argument
        # Assign it using self.attribute_name = argument
        self.breed = breed 
        self.name = name
    
    # methods -> function acting on the object that take the object itself into
    
    def bark(self,rep): # method define - It is a function inside the class
        
        for i in range(0,rep): # rep does not connect with a perticular instance of a class 
            print('Woof!!! My name is {}'.format(self.name)) # don't written .format(name) 
    
my_dog = Dog(breed='Huskie', name='REX') #instance of the class 
print(my_dog.breed,my_dog.name,my_dog.species)

my_dog.bark(4) # calling the method.

