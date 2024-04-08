# Ejercicio 2: Crea un programa que solicite un numero decimal y evalue un polimonio en especifico.

print("Ingrese un numero decimal: ")
num_d = float(input())

print("")

x = num_d

polinomio = (3 * x ** 4) - (10 * x ** 3) + 21

print("El polimonio a evaluar es 3x⁴-10x³+21 y su resultado es:", round(polinomio))