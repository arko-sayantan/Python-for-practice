# LEGB Rule:

# L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
# E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
# B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...


# x is local here:
#f = lambda x:x**2
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()

greet()