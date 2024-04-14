""" Ejercicio 1:
Hallar todos los numeros pares entre 10 y 100 incluyendo
los extremos. """

n = 1

print("\nLos numeros pares entre 10 y 100 son: \n")

for x in range(10,101):
    if x % 2 == 0:
        print("Numero par", n,":", x,"\n")
        n += 1
