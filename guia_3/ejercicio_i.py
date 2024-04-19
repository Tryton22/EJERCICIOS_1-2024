""" Ejercicio 9: 
Resuelva la multiplicación de 2 números positivos por medio de sumas, recuerde que 2x3 
podría ser expresado como 2+2+2 o 3+3. """

try:
    numero_1 = int(input("\nIngrese un numero para la multiplicación: "))
    numero_2 = int(input("Ingrese otro numero para la multiplicación: "))
except ValueError:
    print("\nIngrese un numero, por favor\n")
    exit()

suma = 0
suma_1 = 0

if numero_1 > 0 and numero_2 > 0:
    for i in range(1,numero_2+1):
        suma = suma + numero_1
    print("\nEl resultado sumando el primer numero es:", suma)

    for i in range(1,numero_1+1):
        suma_1 = suma_1 + numero_2
    print("El resultado sumando el segundo numero es:", suma_1,"\n")

    
else:
    print("\nIngrese solo numeros positivos, por favor\n")
    exit()
