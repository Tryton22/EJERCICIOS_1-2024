#Ejercicio 8: Crear un programa que pida la base y altura de un triangulo para mostrar su area.

print("Ingrese la base de su triangulo rectangulo:")
base_triangulo = int(input())

print("")

print("Ingrese la altura de su triangulo rectangulo:")
altura_triangulo = int(input())

print("")

area_triangulo = (base_triangulo * altura_triangulo) / 2

print("El area de su triangulo rectangulo de base", base_triangulo,"y altura", altura_triangulo,
      "es de:", round(area_triangulo))