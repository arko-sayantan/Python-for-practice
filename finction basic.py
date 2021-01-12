def name_of_function(name = 'world'): # world is default value
    # comment what function do.
    
    print('hello',name)
    
    return name # return allow to reuse veriable in any position of code which print is not do that

x = input('Enter the name : ')
y = name_of_function(x)
print(len(y))  # here we re use the variable which i assign in funtion.

def even_check_list(lis):
    # it return true if their in a only one even number.
    even_lis = [] # placeholder variable
    for num in lis:
        if num % 2 == 0:
            even_lis.append(num)
            
        else:
            pass
    return even_lis

zz = even_check_list([1,2,4,5,7])
print(f'\n{zz}')

work_hours = [('arko',1000),('soumili',400),('sayantan',100)]

def employee_check(work_hours):
    # Search which employee work more hr.
    hours_max = 0
    name = ''
    
    for i,hour in work_hours:
        if hour > hours_max:
            hours_max = hour
            name = i
    else:
        pass
    
    return (name,hours_max)

employee_check(work_hours)
