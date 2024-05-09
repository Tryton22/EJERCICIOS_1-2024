""" Ejercicio 4:
Modifique el programa anterior para que en el caso de que esté contenida, 
además, diga en qué índice se encuentra esta subcadena. Por ejemplo: “aloH” y 
"Hola Mundo” regresa "está contenida en el indice 0" sino, mostraría en pantalla 
"no está contenida " """

print("\nDadas 2 cadenas ingresadas, demuestre por pantalla que la primera al reves esta contenida en la segunda ")
print("E indique el indice en caso de estar contenida.")
print("-----------------------------------------------------------------------------------------------------------\n")

cadena_1 = input("Ingrese una cadena de caracteres: ")
cadena_2 = input("Ingrese otra cadena de caracteres: ")

indice = cadena_2.find(cadena_1[::-1])

if indice != -1:
    print("\nEsta contenida en el indice {} \n".format(indice))
else:
    print("\nNo esta contenida en ningun indice.\n")
