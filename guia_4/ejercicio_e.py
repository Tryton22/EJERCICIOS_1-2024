""" Ejercicio 5:
Definida la siguiente cadena dentro de una variable de programa:  "    ejemplo\nde\t mentira \n\t!!!"  muestre esta cadena por pantalla y luego 
nuevamente la misma cadena pero removiendo cualquier tipo de salto de línea 
"\n" tabulación o espacio por completo. Esto debe hacerlo de manera de que si se 
cambia la cadena definida originalmente, el resultado siga siendo válido para esa 
nueva cadena. """

print("\nDefinir una cadena definida dentro de una variable, imprimirla y luego imprimirla removiendo cualquier tabluacion existente.")
print("----------------------------------------------------------------------------------------------------------------------------------\n")

cadena_espacio ="    ejemplo\nde\t mentira \n\t!!!"
cadena_sin_espacio = cadena_espacio.split()

print("\nCadena original: \n")
print(cadena_espacio,"\n")

print("\nCadena modificada: \n")
print("".join(cadena_sin_espacio),"\n")