class Circle():
    
    # class object attribute
    pi = 3.14
    
    # user defined attribute 
    
    def __init__(self,radius = 1):
        
        self.radius = radius
    
    # method
    
    def circumference(self):
        cir = 2 * Circle.pi * self.radius # you can call pi using class because this is class object attribute 
        print(f'The circumference of circle having radius {self.radius} : {cir}')
    
    def area(self):
        are = self.pi * (self.radius ** 2)
        print(f'The area of circle having radius {self.radius} : {are}')
    
r = float(input('Enter the radius of the circle : '))

cir = Circle(r)

cir.circumference()
cir.area()
