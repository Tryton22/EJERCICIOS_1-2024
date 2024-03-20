#Ejercicio 5: Crear un programa que pidiendo los lados de un rectangulo muestre su perimetro y su area.

print("Ingrese el lado de su rectangulo:")
lado_rectangulo = int(input())

print("")

print("Ingrese el ancho de su rectangulo:")
ancho_rectangulo = int(input())

print("")

perimetro_rectangulo = 2 * (lado_rectangulo + ancho_rectangulo)
print("El perimetro de su rectangulo de lado", lado_rectangulo,"y de ancho", ancho_rectangulo,
      "es de:", perimetro_rectangulo)


print("")

area_rectangulo = lado_rectangulo * ancho_rectangulo
print("El area de su rectangulo de lado", lado_rectangulo,"y de ancho", ancho_rectangulo, 
      "es de:", area_rectangulo)