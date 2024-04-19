""" Ejercicio 4:
Sumar todos los números que introduzca el usuario hasta que ingrese un 0. """

suma = 0
num_suma = 1

while num_suma > 0:
    num_suma = int(input("\nIngrese un numero: "))
    if num_suma > 0:
        print("\nNumero", num_suma,"ingresado.\n")
    else:
        break
    suma = suma + num_suma

print("\nLa suma de los numeros ingresados es:", suma,"\n")