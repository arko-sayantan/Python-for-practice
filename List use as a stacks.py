# We can use list as a Stack data structure (Last In First Out). Its like a container which top side is open
# in List we use .append() for push the item in stack and .pop() for pop the item.
# Demo list use as a stack.

stack = [10,20,60,45]

itm = int(input("How many item you want to store (Enter integer) : "))
for i in range(itm):
    itn = input('Enter item :')
    stack.append(itn) # Now .appen() push the item in stack.

print('\nThe stack after appending : ',len(stack))

print('\nThe length of the stack : ',stack)

itm2 = int(input("How many item you want to pop : "))
for i in range(itm2):
    stack.popleft()

print('\nThe stack after poping : ',stack)