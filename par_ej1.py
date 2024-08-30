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
