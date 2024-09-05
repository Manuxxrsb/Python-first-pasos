#Declarar y llamar una función
""" 
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()

"""
#ejemplo de funciones sin paso de parametros
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()

#funcion con retorno
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name()) #mostramos lo que retorna la funcion

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

print(add_two_numbers())

#funcion con paso de parametros

def saludo (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(saludo('Manuel'))


def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
  
print('Full Name: ', generate_full_name('Manuel','Solis'))

#funcion que recibe un numero desconocido de valores

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total

print(sum_all_nums(2, 3, 5)) # 10