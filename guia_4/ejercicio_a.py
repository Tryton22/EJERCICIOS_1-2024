""" Ejercicio 1:
Dada una cadena ingresada por teclado, insertar la subcadena “super” en la 
posición 3 de la cadena original, moviendo todo el contenido precedente después 
de la inserción. Si la cadena es más corta, poner la subcadena al final de la cadena. 
Ej.- extremo -> extsuperremo, menguante -> mensuperguante, im ->imsuper """

print("\nDada una cadena, insertar 'super' en su posicion 3")
print("-------------------------------------------------------")

cadena =input("\nIntroduzca un palabra: ")

if len(cadena) >= 3:
    print("\nLa cadena original es: ", cadena)
    print("La cadena cambiada es: ", cadena[:3] + "super" + cadena[3:],"\n")
else:
    print("\nLa cadena original es: ", cadena)
    print("La cadena cambiada es: ", cadena + "super","\n")
