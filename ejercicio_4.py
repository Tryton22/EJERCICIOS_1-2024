#Ejercicio 4: Crear un programa que pidiendo el lado de un cuadrado muestre su perimetro y su area.

print("Ingrese cuanto mide el lado de su cuadrado: ")
lado_cuadrado = int(input())

print("")

perimetro_cuadrado = 4 * lado_cuadrado

print("El perimetro de su cuadrado de lado", lado_cuadrado,"es:", perimetro_cuadrado)

print("")

area_cuadrado = lado_cuadrado ** 2

print("El area de su cuadrado de lado", lado_cuadrado,"es:", area_cuadrado)
