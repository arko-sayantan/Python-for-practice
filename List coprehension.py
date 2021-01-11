# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:42:33 2021

@author: ASUS
"""

## Herewe discuss list comprehension.

mylist = [1,2,3,4,5,6,7,8]

mylis = [x**2 for x in mylist]  # The for-loop operation take place in oneline
                                # this is the advance of list comprehension 
                                # x**2 is the opretion which take place in the for loop
mylis2 = [x**2 for x in mylis if x%2 == 0] # It prints square of odd position of elements in list 
                                            # you can use if-else in list comprehension.
print(f'The square of the element in mylis: {mylis}')
print(f'The square of odd element in mylist :{mylis2}')

lis = [x*y for x in [2,4,6] for y in [1,10,100]]  # Example of nested loop.
print(lis)    

celsius = [10,20,40,30,40,50,99]
fahrenteit = [((9/5)*temp+32) for temp in celsius] # (9/5)*temp+32) --> main operation
print(f'Fahrenteit : {fahrenteit}')
