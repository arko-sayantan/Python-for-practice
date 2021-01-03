# 3 A Tuple is a another type of sequence data type that is similler to list.
# but the difference is b/w list and tuple is list can be change but tuple is not changable.
# You can say tuple is a read only lists .So in tuple we can not append item.
# [] or [:] us,e as slicing oparator and the '+' sign use for list concaatenation and '*' use for list repeatation

tup = (10,12,15,6,5,4987,44)
tup2 = (15,89,46)
# tup.append(12) you can not change the tuple 
print(tup[3:6])
print(tup)
print(tup + tup2) # But you can concatanate tuples
print(len(tup))
