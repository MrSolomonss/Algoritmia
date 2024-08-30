'''
3. Desarrolle un algoritmo para el cálculo del salario de un trabajador. El importe
liquidado (sueldo) depende de una tarifa o precio por hora establecida y de un
condicionante sobre las horas trabajadas: si la cantidad de horas trabajadas es mayor a
40 horas, la tarifa se incrementa en un 50% para las horas extras. Calcular el sueldo
recibido por el trabajador en base las horas trabajadas y la tarifa. Utilice las
instrucciones LEER HORASTRABAJADAS y LEER TARIFA al inicio del programa para
cargar los valores en las variables HORASTRABAJADAS y TARIFA.
'''

# Función para leer las horas trabajadas
def leer_horas_trabajadas():
    horas_trabajadas = float(input("Ingresa las horas trabajadas: "))  # Pedir al usuario las horas trabajadas
    return horas_trabajadas

# Función para leer la tarifa por hora
def leer_tarifa():
    tarifa = float(input("Ingresa la tarifa por hora: "))  # Pedir al usuario la tarifa por hora
    return tarifa

# Pedimos las horas trabajadas y la tarifa al inicio del programa
HORASTRABAJADAS = leer_horas_trabajadas()
TARIFA = leer_tarifa()

# Inicializamos el salario en 0
salario = 0.0

# Calculamos el salario según las horas trabajadas
if HORASTRABAJADAS <= 40:
    salario = HORASTRABAJADAS * TARIFA  # Si trabajó 40 horas o menos, se multiplica por la tarifa
else:
    horas_extra = HORASTRABAJADAS - 40  # Calculamos cuántas horas fueron extras
    salario_normal = 40 * TARIFA  # Salario por las primeras 40 horas
    salario_extra = horas_extra * TARIFA * 1.5  # Salario para las horas extras (1.5 veces la tarifa)
    salario = salario_normal + salario_extra  # Sumamos el salario normal y el extra

# Mostramos el salario total
print("El salario total es:", salario)
