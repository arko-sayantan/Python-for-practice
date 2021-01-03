# list  ----> Lists is a order sequence of item.And it is mutable object.
# [] or [:] use as slicing oparator and the '+' sign use for list concaatenation and '*' use for list repeatation

lst_mkt = ['apple','meat','orange','milk','onion'] # the indexing is start form 0
print('The item in list are :\n',lst_mkt)
print('The item in list are : \n')
for x in range(len(lst_mkt)): 
    print (lst_mkt[x])   
print('\n')
lis = list()  #creat an open list. 
lst_mkt.remove('onion')
print(lis)
print(lst_mkt)