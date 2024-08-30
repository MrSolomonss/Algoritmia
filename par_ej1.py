#1. Escriba un algoritmo que lea un número entero y determine si es par o impar. Si es par,
#que escriba todos los pares de manera descendiente desde sí mismo y hasta el cero. Si
#es impar, que escriba todos los impares de manera descendiente desde si sí mismo
#hasta el uno. Utilice la instrucción LEER NUMERO al inicio del programa para cargar un
#número en la variable NUMERO.


def determinar_paridad(numero):
    if numero % 2 == 0:
        print(f"{numero} es par. Pares descendientes hasta 0:")
        for i in range(numero, -1, -2):
            print(i)
    else:
        print(f"{numero} es impar. Impares descendientes hasta 1:")
        for i in range(numero, 0, -2):
            print(i)



numero = int(input("LEER NUMERO: "))
determinar_paridad(numero)
