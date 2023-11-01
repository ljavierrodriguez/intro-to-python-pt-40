# Tipo de Datos y Variables
""" 
String
Int
Float
Boolean

None

Dict

Array:
    List
    Tuple
    Set

func

"""

nombre = ""
apellido = ''

direccion = f"""Lorem ipsum dolor sit amet consectetur adipisicing
 elit. Possimus minima fuga nam {nombre} inventore {apellido} dolor adipisci reiciendis
  praesentium dolorum obcaecati, veniam pariatur. Est, quisquam? 
  Libero autem animi temporibus porro enim quia!""" # str
  
edad = 40 # int
precio = 10.50 # float
grados = -10 # int
saldo = -1.5 # float

active = False
open = True

peso = None
users = None

persona = {
    "nombre": "",
    "apellido": ""
}

persona["nombre"] = "Jane"
persona["apellido"] = "Doe"

# List
nombres = ["Hugo", "Paco", "Luis"] # list
nombres[1] = "Donald"
nombres.append("Mickey")

# Tuple
status = ("active", "inactive", "suspended", "canceled", "approved", "banned")
status[3]

# Set
frutas = { "Pera", "Manzana", "Uva", "Banana"}


def nombre_funcion():
    pass

sumar = lambda a, b: a + b