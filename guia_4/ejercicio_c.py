""" Ejercicio 3:
Dadas 2 cadenas ingresadas por teclado, muestra por pantalla si es que la primera cadena al revés está contenida como una subcadena en la segunda cadena. 
Por ejemplo: “aloH” y "Hola Mundo” regresa "está contenida" sino, mostraría en pantalla "no está contenida" """

print("\nDadas 2 cadenas ingresadas, demuestre por pantalla que la primera al reves esta contenida en la segunda.")
print("-----------------------------------------------------------------------------------------------------------\n")

cadena_1 = input("Ingrese una cadena de caracteres: ")
cadena_2 = input("Ingrese otra cadena de caracteres: ")

if cadena_1[::-1] in cadena_2:
    print("\nEstá contenida.\n")
else:
    print("\nNo está contenida.\n")