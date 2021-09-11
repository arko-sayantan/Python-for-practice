class Book():
    
    def __init__(self,title,name,pages):
        self.title = title
        self.name = name
        self.pages = pages
    
    def __str__(self): # we change default string notation by this method
        return f"{self.title} is written by {self.name} which having {self.pages} pages."
    
    def __len__(self):
        return self.pages
        
b = Book('Python magic','Das',300)

print(b) #print alwayes return a sting 
        # and default represention of class in from of string
        # is something like that ' <__main__.Book object at 0x000001F85E6991F0> '
        # but we change this default string representation of class by using __str__ method

print(len(b))

# del b --> this is use for delete a veriable form computer memory

