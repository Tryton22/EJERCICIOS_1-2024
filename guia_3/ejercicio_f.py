""" Ejercicio 6:
Obtener todos los números primos entre 10 y 100 incluyendo los extremos """

print("\nLos numeros primos entre 10 y 100 son: ")
print("-------------------------------------------\n")

primos = 0

for numero in range(10,101):
    for i in range(2, numero):
        if (numero % i) == 0:
            break
    else:
        print("El numero", numero,"es primo.\n")
        primos += 1

print("Existen", primos,"numeros primos entre 10 y 100\n")