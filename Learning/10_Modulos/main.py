import Funciones_ejemplo #llamada a un modulo completo

from Funciones_ejemplo import resta   #importacion de una funcion en concreto esta no requiere mencionar el modulo en su invocacion en el code

print('Suma a travez de un modulo: ', Funciones_ejemplo.suma(4,4))

print('resta a travez de un modulo: ', resta(10,5))

#modulos utiles

#Modulo string

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#Módulo aleatorio
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive


