# We can use list as a Queue data structure (First In First Out). Its like a container which bottom side is open
# in List we use .append() for push the item in stack and .leftpop() for pop the item.
# But list is not efficient for this purpose. Python provide a module called collection in which a method
# called deque() is design to helps fast appends and pop form the both side

from collections import deque

queue = deque([10,20,60,45])

print(queue)

itm = int(input("How many item you want to store (Enter integer) : "))
for i in range(itm):
    itn = input('Enter item :')
    queue.append(itn) # Now .appen() push the item in stack.

print('\nThe Queue after appending : ',len(queue))

print('\nThe length of the Queue : ',queue)

itm2 = int(input("How many item you want to pop : "))
for i in range(itm2):
    queue.popleft()

print('\nThe queue after poping : ',queue)

