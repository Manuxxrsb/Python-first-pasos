#Para crear un diccionario(Struct) utilizamos llaves, {} o la función incorporada dict() .

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 
       'key2':'value2', 
       'key3':'value3', 
       'key4':'value4'
       }

#diccionario con varios tipos de datos
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

#longitud de un diccionario
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

#Acceder a los elementos del diccionario
dct = {'key1':'Que pasa',
       'key2':'value2', 
       'key3':'value3', 
       'key4':'value4'
       }

print(dct['key1']) # value1
print(dct['key4']) # value4


"""""
Acceder a un elemento por nombre de clave genera un error si la clave no existe. 
Para evitar este error, primero debemos verificar si existe una clave o podemos usar el método get . 
El método get devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.
"""
print(person.get('first_name')) # Asabeneh Retorna la cadena que buscamos dentro del diccionario sino retorna 'None'  que es un valor de diccionario
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None


#Cómo agregar elementos a un diccionario

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor' #ingreso una key nueva con su valor
person['skills'].append('HTML') #agrego un valor a la key ya existente
print(person)

#Modificar elementos en un diccionario
person['first_name'] = 'Manuel'
person['age'] = 24

#Cómo eliminar pares de clave y valor de un diccionario

#pop(key) : elimina el elemento con el nombre de clave especificado:
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item

#popitem() : elimina el último elemento
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item

#del : elimina un elemento con el nombre de clave especificado
del dct['key2'] # removes key2 item

#Eliminar un diccionario
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

#Copiar un diccionario
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

#Obtener claves de diccionario en forma de lista
# metodo Key() 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

#Obtener valores del diccionario como una lista
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

