""" Ejercicio 12:
Elaborar un programa que permita ingresar la edad de una persona. Si la edad es menor o
igual a 15 mostrar "niñez", si es mayor que 15, pero menor o igual a 35, mostrar "juventud", si
la edad es mayor que 35 mostrar "adulto". """

edad = int(input("\nIngrese su edad en años: "))

if edad <= 15:
    print("\nNiñez\n")
elif 15 < edad <= 35:
    print("\nJuventud\n")
else:
    print("\nAdulto\n")