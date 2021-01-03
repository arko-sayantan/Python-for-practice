# Here we creat a empty list and insert item into it. Also we learn about the method.

itm = int(input("How many item you want to store : "))
lis = list()
for i in range(itm):
    itn = input('Enter item :')
    lis.append(itn)  # .append method add item n to the list
    # lis.sort(key=(None),reverse=False) --> Sort the list in assending order.
    
    
print('Here the item is : \n')
for k in range(len(lis)):
    print(lis[k])
print('\n')
lis2=lis.copy() # its copy the list 1 into list 2
lis.clear() # its clear the list.
print('The list after copy : ',lis2)
print('The list after clear :',lis)