# funciones
"""
def nombre_funcion():
    pass

sumar = lambda a, b: a + b

"""
# parametros posicionales
def sumar(a, b, c):
    return a + b

sumar(10, 10, 10)

# parametros con valor por defecto
def saludo(nombre = "John", apellido = "Doe"):
    return f"Hola, {nombre} {apellido}"

saludo() # Hola, John Doe
saludo("Jane") # Hola, Jane Doe
saludo("Luis", "Rodriguez") # Hola, Luis Rodriguez

# parametros keywords
def saludo(nombre = "John", apellido = "Doe"):
    return f"Hola, {nombre} {apellido}"

saludo(nombre="Luis", apellido="Rodriguez") # Hola, Luis Rodriguez
saludo(apellido="Navas")


# agrupacion de parametros
def sumatoria(*datos):
    resultado = sum(datos)
    return resultado

sumatoria(1, 2, 3, 4, 5, 6)

# agrupacion de parametros keywords
def informacion(**datos):
    return f"Hola, mi nombre es {datos['nombre']} y vivo en {datos['pais']}"

informacion(nombre="Luis Rodriguez", pais="Chile") # Hola, mi nombre es Luis Rodriguez y vivo en Chile
