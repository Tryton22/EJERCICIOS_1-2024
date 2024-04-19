""" Ejercicio 5:
Sacar el promedio de todos los números que introduzca el usuario hasta que ingrese un 0. """

suma = 0
num_suma = 1
promedio = 0

while num_suma > 0:
    num_suma = int(input("\nIngrese un numero: "))
    if num_suma > 0:
        print("\nNumero", num_suma,"ingresado.\n")
        promedio += 1
    else:
        break
    suma = suma + num_suma

print("\nEl promedio de los numeros ingresados es:", suma // promedio)
