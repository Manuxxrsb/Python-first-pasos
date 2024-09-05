#ciclo while

count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
print('\n')

#Break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break #termina el ciclo
    
# continue
print('\n')
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue #no termina el ciclo sino que se salta esa iteracion sin seguir ejecutando el codigo restante
    print(count)
    count = count + 1
    
#ciclo for
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
    

#For loop with string
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i]) #Imprimimos todas las letras 1 por 1
    
#la funcion Range

"""
La función range() se utiliza para crear una lista de números. 
El rango (inicio, fin, paso) acepta tres parámetros: inicio, fin e incremento. 
De manera predeterminada, comienza desde 0 y el incremento es 1. La secuencia de rango necesita al menos 1 argumento (fin). 
"""

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indica el inicio y el final, el paso a paso por default es 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2)) #aqui queda de dos en dos
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}