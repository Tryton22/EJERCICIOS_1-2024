""" Ejercicio 8:
Realizar la sumatoria de los números en un rango dado por el usuario. """

num_menor = int(input("\nIngrese el primer numero del rango: "))
num_mayor = int(input("Ingrese el segundo numero del rango: "))

suma = 0

if num_mayor > num_menor:
    for i in range(num_menor,num_mayor+1):
        suma = suma + i
else:
    print("\nIngrese primero el numero menor, por favor.\n")
    exit()

print("\nLa sumatoria del rango ingresado es", suma,"\n")