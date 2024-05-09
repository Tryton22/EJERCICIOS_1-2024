""" Ejercicio 2:
Dada una cadena ingresada por teclado regresa como resultado las veces en que 
una letra minúscula sigue a una mayúscula en esa cadena. Por ejemplo: “HoLa mUnDo” regresa: 4 """

print("\nDada una cadena, regresar las veces que una minuscula sigue de una mayuscula.")
print("----------------------------------------------------------------------------------\n")

cadena = input("Ingrese una cadena alternando entre mayusculas y minusculas: ")

cuenta = 0

for i in range(len(cadena) - 1):
    if cadena[i].isupper() and cadena[i + 1].islower():
        cuenta += 1

print("\nLa cadena es: ", cadena)
print("Y el resultado es: ", cuenta,"\n")