
# Single line comment
letter = 'P'                # A string puede ser una letra o una frase
print(letter)               # P
print(len(letter))          # 1 , se pueden contar las letras tambien
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)


# otra forma de definir un string multilineal
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)


# String Concatenation
first_name = 'Manuel'
last_name = 'Solis'
space = ' ' #reconoce los espacios
full_name = first_name  +  space + last_name
print(full_name) 

# Checking length of a string using len(variable) 
print(len(first_name))  # 8
print(len(last_name))   # 7


#### desempacar caracteres 
language = 'Python'
a,b,c,d,e,f = language # desempacando la secuencia de caracteres en cada variable con la declaracion de multivariables en una linea
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# acceso a caracteres especificos con el enfoque de lista
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# para empezar al revez usar numeros negativos 
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

#Descomposicion

language = 'Python'
first_three = language[0:3] # para asignar los valores 0,1,2     |ojo no se incluye el 3|
last_three = language[3:6]
print(last_three) # hon


# uso mas complejo de printear intermedios en un string
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# secuencias de escape
print('I hope every one enjoying the python challenge.\nDo you ?') # Salto de linea
print('Days\tTopics\tExercises') #tabs
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('In every programming language it starts with \"Hello, World!\"') ##permite escribir formato code pero no es muy util

## String metodos
# capitalize(): Convierte el primer caracter a Mayuscula

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): retorna el numero de ocurrencias en el string

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('th')) # 2`

# endswith(): confirma si un string termina con alguna sentencia

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# find(): retorna el indice de la primera ocurrencia

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

# index(): parecido al find pero sirve para subcadenas
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isalnum(): Comprueba el carácter alfanumérico

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Comprueba si todos los caracteres son alfabetos.

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Comprueba los caracteres decimales

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isdigit(): Comprueba los caracteres de los dígitos

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.digit())   # True

# isdecimal(): Comprueba los caracteres decimales.

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower(): Comprueba si todos las letras de una cadena están en minúsculas

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): comprueba si todos las letras son caracteres en mayúsculas

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Elimina los caracteres iniciales y finales.

challenge = ' thirty days of python '
print(challenge.strip('y')) # 5

# replace(): Reemplaza la subcadena dentro

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split():Divide la cadena desde la izquierda creando una lista

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title(): Devuelve una cadena de título en mayúsculas y minúsculas

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Comprueba si la cadena comienza con la cadena especificada
  
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False