empty_list = list() #para crear una lista vacia
print(len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                      # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']       # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']              # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits) #Fruits: ['banana', 'orange', 'mango', 'lemon']
print('Number of fruits:', len(fruits))


# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # accedemos a la primera fruta por indice
print(first_fruit)      # banana
second_fruit = fruits[1]

# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# asignaciones
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # se asigna de la primera a la tercera fruta

fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits #ejemplo de comprobacion en la lista
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')   #agregamos una fruta con el comando append()

print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple'] <--

fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # inserta apple en la posicion elegida sin eliminar el objeto sino que lo mueve

print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')   #remueve banana y reasigna espacios no deja vacios entre parentecis se coloca la ocurrencia a eliminar
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()      #quita el elemento final como en una cola
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     #popea la fruta inicial pero no es muy comun su uso
print(fruits)       # ['orange', 'mango'] 

# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     #elimina igual que remove pero este elimina la posicion y no la frase o ocurrencia dentro de los parentesis este funciona con posiciones
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']

#del fruits
#print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     #dropea el arreglo completo
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()      #copia la lista completa
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']


# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))   #retorna el indice de la ocurrrencia en la lista

# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()  #invierte la lista
print("Reverso frutas: ",fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print("Reverso edades: ",ages) 

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort() #cambia las posiciones aleatoriamente 
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 