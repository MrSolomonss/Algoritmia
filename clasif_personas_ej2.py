import random

'''
2. Escriba un algoritmo que visualice una clasificación de 50 personas según edad y sexo.
Deberá mostrar los siguientes resultados:
a. Cantidad de personas mayores de edad (18 años o más).
b. Cantidad de personas menores de edad.
c. Cantidad de personas masculinas mayores de edad.
d. Cantidad de personas femeninas menores de edad.
e. Porcentaje que representan las personas mayores de edad respecto al total de
personas.
f. Porcentaje que representan las mujeres respecto al total de personas.
Utilice la instrucción LEER PERSONAS al inicio del programa para cargar los datos de las
50 personas en un variable, PERSONAS, que actúa como un vector de 50 posiciones.
Cada elemento de PERSONAS es de un tipo estructurado que dispone dos campos:
SEXO y EDAD.
'''

# Función para generar una lista de personas con sexo y edad aleatorios
def leer_personas():
    personas = []
    for _ in range(50):
        sexo = random.choice(["M", "F"])  # Escoge aleatoriamente "M" o "F" para el sexo
        edad = random.randint(1, 100)     # Escoge una edad aleatoria entre 1 y 100
        personas.append({"SEXO": sexo, "EDAD": edad})  # Agrega la persona a la lista
    return personas

# Generamos la lista de personas al inicio del programa
PERSONAS = leer_personas()

# Inicializamos los contadores
mayores_edad = 0
menores_edad = 0
masculinos_mayores_edad = 0
femeninas_menores_edad = 0
total_mujeres = 0

# Recorremos la lista de personas
for persona in PERSONAS:
    edad = persona["EDAD"]
    sexo = persona["SEXO"]

    # Contamos cuántos son mayores o menores de edad
    if edad >= 18:
        mayores_edad += 1
        if sexo == "M":
            masculinos_mayores_edad += 1
    else:
        menores_edad += 1
        if sexo == "F":
            femeninas_menores_edad += 1

    # Contamos el total de mujeres
    if sexo == "F":
        total_mujeres += 1

# Calculamos los porcentajes
porcentaje_mayores = (mayores_edad / len(PERSONAS)) * 100
porcentaje_mujeres = (total_mujeres / len(PERSONAS)) * 100

# Mostramos los resultados
print("a. Cantidad de personas mayores de edad:", mayores_edad)
print("b. Cantidad de personas menores de edad:", menores_edad)
print("c. Cantidad de personas masculinas mayores de edad:", masculinos_mayores_edad)
print("d. Cantidad de personas femeninas menores de edad:", femeninas_menores_edad)
print("e. Porcentaje de personas mayores de edad:", porcentaje_mayores, "%")
print("f. Porcentaje de mujeres respecto al total de personas:", porcentaje_mujeres, "%")
