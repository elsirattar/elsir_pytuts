#Decorator in python

def test_decorator(func):
    print('before function')
    func()
    print('after function')

## decorator run automatically without call it
@test_decorator
def greeting():
    print('hello after before , before after')
'''
Result :
================
before function
hello after before , before after
after function
=================
'''

def deco(func):
    def inner_func():
        print('from inner function')
        func()
        print('after fire func')
    return inner_func

@deco
def fire_func():
    print('from fire func')
    
    #function will not fire automatically in this case 
# must call the function to execute it

fire_func()
'''
Results:
====================
from inner function
from fire func
after fire func

=============
'''

def num_divide(func):
    """
    - take two parameters from users
    - divide param1 by param2
    - check it if param is 0 ==> return message the can not divide by zero
    - if any or all parameters not integers ==> return message {param} is not integer
    """
    def check_int(x):
        if isinstance(x , int):
            if x == 0:
                print('can not divide by Zero')
                return False
            return True
        print('{} is not a number'.format(x))
        return False
    
    def mainly(num1, num2):
        if not check_int(num1) or not check_int(num2):
            return  
        return func(num1,num2)
    return mainly

        

@num_divide
def dvide_it(num1 , num2):
    print(num1 / num2)

dvide_it(12, 2) #6
dvide_it(0,2) # can not divide by Zero
dvide_it(2,0) # can not divide by Zero
dvide_it('Elsir',3) # Elsir is not a number
