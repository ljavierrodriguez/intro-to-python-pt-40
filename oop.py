# OOP (Object Oriented Programming) (Programacion Orientada a Objeto)
from modulos import saludo

class Persona:
    nombre = None
    apellido = None
    edad = None
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def comer(self):
        return "Comer"
    
    def caminar(self):
        return "Caminar"
    
    def correr(self):
        return "Correr"
    

p1 = Persona("John", "Doe", "Unknown")
p2 = Persona("Jane", "Doe", "Unknown")

p1.nombre = "Hugo"

print(p1.comer())
print(p2.caminar())

class Estudiante(Persona):
    grado = None
    facultad = None
    
    def __init__(self, nombre, apellido, edad, grado, facultad):
        super().__init__(nombre, apellido, edad)
        self.grado = grado
        self.facultad = facultad
        
    def comer(self):
        return "Comer de Estudiante"
    
    
est1 = Estudiante("Tommy", "Doe", "Unknown", "2do", "Computacion")
print(est1.comer())

print(saludo())