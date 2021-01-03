
import math # math is a module
a = int(input("Enter the magnetic flux denity : "))
b = int(input("Enter the area : "))

c = float(input("angle between them : "))

e = math.cos(c)

d =float(a*b*e)
print("The value of flux is : ",d) 

