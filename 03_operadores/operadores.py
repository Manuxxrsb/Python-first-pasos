# operaciones aritmeticas en Python

# Enteros

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python da numeros float
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # significa 3 * 3

# float numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type


# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b #modulo
floor_division = a // b #division de float
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)



print(len('mango') == len('avocado'))  # igual igual
print(len('mango') != len('avocado'))  # distinto de
print(len('mango') < len('avocado'))   # menor que
print(len('python') > len('dragon'))   # mayor que

# Boolean comparaciones
print('True == True: ', True == True)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - porque los valores son los mismos
print('1 is not 2', 1 is not 2)           # True - porque 1 no es 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - porque encontro dentro de Asabeneh una A
print('B in Asabeneh', 'B' in 'Asabeneh') # False -Hay una b pero no es mayuscula
print('coding' in 'coding for all') # True - porque escontro la palabra coding en toda la frase
