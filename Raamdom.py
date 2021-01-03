import random     # random is module to choose randomly.
import keyword

print("The all keyword of python : \n")
print(keyword.kwlist,'\n')
Str = "Hi my name is Sayantan Das."      # indexing start form 0
print(Str)              # it will print the statement
print("Hi" in Str)       # it will verify that 'Hi' is the the string or not
print(Str[15])          # [] or [:] use as slicing oparator
        # print(Str[5:16])
print(Str * 3)
print(Str + "I study Engineering")
print('Random letter choose : \a', random.choice(Str))
print('Lenght of string : ',len(Str),':', Str.lower().strip('.').title())
print('Split the string to convert in List :',Str.split(' '))
print('Find the charecter and return the string: ',Str.find('Sayantan',0,len(Str)))
                                            #find('item',begin index,end index)
print('Checking the condition :',Str.isnumeric(),Str.istitle(),Str.islower(),Str.isdigit())
