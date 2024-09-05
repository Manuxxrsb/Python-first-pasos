#Creating a Class
"""
class ClassName:
  code goes here
"""

class Person:
  pass

print(Person)

#creamos el objeto
p = Person()
print(p)


#declaracion correcta de un objeto util
class Persona:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name = name

p = Persona('Asabeneh')
print(p.name)
print(p)

class Person:
      def __init__(self, firstname, lastname, age, country, city): #metodo constructor
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


#ejemplo completo

p = Person('Manuel', 'Solis', 23, 'Chileeeeeeeee', 'Santiago')
print(p.firstname) #forma de acceder a los atributos es similar a los struct
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)


#Métodos de objeto
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'   #f'code' Formatea el codigo a string sino retornaria la variable o lo que sea

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())

#Método para modificar los valores predeterminados de una clase
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill) #usamos el .append() normal para modificarlo

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

