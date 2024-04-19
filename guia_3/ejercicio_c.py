""" Ejercicio 3:
Determinar si un número mayor a 20 ingresado por el usuario es primo o no. 
Un número  primo solo es divisible por 1 y por sí mismo. """

print("\nEvaluar si un numero mayor a 20 es primo.")
print("-----------------------------------------------")

try: 
    num_mayor = int(input("\nIngrese un numero mayor a 20: "))
except ValueError:
    print("\nIngrese numeros, por favor.\n")
    exit()

primo = 0

if num_mayor > 20:
    for i in range(2, num_mayor):
        if num_mayor % i == 0:
            primo += 1
    primo += 1

    if primo > 1:
        print("\nEl numero ingresado:", num_mayor,"no es primo.\n")
    else:
        print("\nEl numero ingresado:", num_mayor,"es primo.\n")  
else: 
    print("\nIngrese un numero mayor a 20, por favor.\n")
    exit()