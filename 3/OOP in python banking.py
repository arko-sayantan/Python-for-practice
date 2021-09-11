# bank Account 
from colorama import init
from colorama import Fore,Back
init()
class Account():
    
    def __init__(self,name,banc):
            
        self.name = name
        self.banc = banc
    
    def __str__(self):
        return f'Account owner:   {self.name}\nAccount balance: \u20B9{self.banc}'
    
    # methods
    
    def deposit(self,amt1):
        
        self.banc += amt1
        print('Deposit done.')
        print(f'Available balence: \u20B9{self.banc}')
        
    
    def withd(self,amt2):
        if self.banc >= amt2:
            self.banc -= amt2
            print(f'{amt2} amount withdrawn')
            print(f'Available balence: \u20B9{self.banc}')
        else:
            print('Funds unavailable')
            
print('------------- Welcome to banking system -------------')            
            
# object calling
owner = input('Enter Account holder name: ') 
amount = float(input('Enter the amount: '))
acc1 = Account(owner, amount)

#Option selection
print('Select your option!')
print('1.Want to diposit \n2.Want to withdrawn')

option = int(input('Enter your choice :'))

if option == 1:
    am = float(input(Back.YELLOW+Fore.WHITE+'Enter the amount you want to add : '))
    acc1.deposit(am)
elif option == 2:
    am = float(input(Back.GREEN+Fore.BLUE+'Enter the amount you want to withdrawn : '))
    acc1.withd(am)
else:
    print('Please! choose the right option')



# >> from colorama import init
# >>> init()
# >>> print(Fore.RED + "Some red text")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Fore' is not defined
# >>> from colorama import Fore
# >>> print(Fore.RED + "Some red text")
# Some red text
# >>> from colorama import Fore, Back, Style
# >>> print(Fore.RED + 'some red text')
# some red text
# >>> print(Back.GREEN + 'and with a green background')
# and with a green background
# >>> print(Style.DIM + 'and in dim text')
# and in dim text
# >>> print(Style.RESET_ALL)

# >>> print('back to normal now')
# back to normal now
# >>>
