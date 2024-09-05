#condicional if

"""
if condition:
    print('this part of code runs for truthy conditions')
"""

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number


#else

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
    
#else if

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
    
