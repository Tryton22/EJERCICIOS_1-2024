""" Ejercicio 17: 
Analice y desarrolle un programa que permita separar un número entero en dos números 
enteros, uno de ellos conformado por aquellos dígitos mayores o iguales a 5, y el otro por 
los números restantes. """

print("\nSeparar un numero entero en 2: numero de sus digitos mayores y iguales a 5 y numeros con los digitos restantes.")
print("------------------------------------------------------------------------------------------------------------------\n")

numero_entero = int(input("Ingresa un número entero: "))

if numero_entero < 0:
    print("\nPor favor, ingresa un número entero positivo.\n")
else:
    numero_mayor_igual_5 = 0
    numero_menor_5 = 0

    divisor = 1
    while numero_entero > 0:
        digito = numero_entero % 10
        if digito >= 5:
            numero_mayor_igual_5 = digito * divisor + numero_mayor_igual_5
            divisor *= 10
        else:
            numero_menor_5 = digito * divisor + numero_menor_5
            divisor *= 10
        numero_entero //= 10

    print("\nNúmero formado por dígitos mayores o iguales a 5:", numero_mayor_igual_5)
    print("Número formado por dígitos menores a 5:", numero_menor_5,"\n")