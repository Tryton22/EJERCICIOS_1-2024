""" Ejercicio 8:
Al ingresar una cadena de caracteres por teclado, entregar por pantalla una cadena que contenga cada palabra por separado de 
la cadena original escrita al revés, con la primera letra de cada palabra en mayúscula. 
Por ejemplo: “hola mundo” regresa: “Aloh Odnum” """

print("\nIngresar una cadena de caracteres y devolver cada palabra escrita al reves con la primer letra en mayuscula.")
print("---------------------------------------------------------------------------------------------------------------\n")

cadena = input("Ingrese una cadena de caracteres: ")

cadena_separado = cadena.split()

print("\nLa cadena despues de los cambios que en:",end=" ")

for i in cadena_separado:
        print(i[::-1].capitalize(),end=" ")

print("\n")