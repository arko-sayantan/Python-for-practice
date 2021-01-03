# Set is a unorder data structure which element does not have particuler index number
# So in set we canton use slicing and indexing.

se = {1,2,4,5,9,5}
print('Poping element in set : ',se.pop(),':',se)
se2 = {450,456,89,45,65}
se3 = se.union(se2) # in union function we have to implement a veriable.
print('Union of set using union funtion :',se3)
se.update(se2) # in update function does not required any impletation.
print('Union of set using update funtion :',se)
se4 = {1,2,4,3}
se5 = se.intersection(se4)
print('The intersection of two set is : ',se5)
se7 = se.difference(se4)
print('The difference between two set is : ',se7)

# Adding element in set by user input.

a = int(input("How many element you want to add in set : "))
se6= set()  # Denote a empty set.
for i in range(a):
    k = input("Enter the element :")
    se6.add(k) # in set we use add to store a element inspite of append.

print('The element in set are :',se6)

# checking the element in set.

b = int(input('Enter the element you want to search :'))
print('Result :',b in se)

# .issubset ---> use for verifaying the set is subset of another
