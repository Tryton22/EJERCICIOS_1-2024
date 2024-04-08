#Ejercicio 6: Crear un programa que pida el radio de un circulo y muestre su perimetro y su area.

pi = 3.1416

print("Ingrese el radio de su circulo:")
radio_circulo = int(input())

print("")

perimetro_circulo = 2 * pi * radio_circulo
print("El perimetro de su circulo de radio", radio_circulo,"es de:", round(perimetro_circulo))

print("")

area_circulo = pi * radio_circulo ** 2
print("El area de su circulo de radio", radio_circulo,"es de:", round(area_circulo))