# Dictionary --> It is a unorder collection of key-value pairs.It is known as "associative array".

Stu = {'Name' : 'jhon','Roll' : 15,'Dept' : 'ECE'}
print('The elements in dictionary :',Stu)
print('The values entered in the dictionary :',Stu.values()) # its print the values under the perticular key
print('The key in the dictionary :',Stu.keys())  # Its print the name of the key.
print(Stu['Name'])  # Call value by key`.
# We cannot call a key by values .so this statement is invalid print(Stu[15])
Stu['Sec'] ='A'
print('The value after add another key :',Stu)
Stu2 = {'year' : '2nd'}
Stu2 = Stu.copy()
print('The Copied Dictionary is :',Stu2) # if we copy a dictionary then the previous value of dictionary is remove.
# for i in range(len(Stu)):
#     print[Stu]          -->  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 

# EX -->
i = input('Enter the age: ')
j = input('Enter the Name: ')
Stu3 = {'Age' : i,'Name' : j }
Stu3.setdefault('phone',9073330433) # if the key no present in dic then it will set the default value
print('the dict is :',Stu3)

# We only assign one value for a perticular key.
