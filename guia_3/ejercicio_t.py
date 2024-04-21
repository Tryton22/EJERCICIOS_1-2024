""" Ejercicio 20:
Desarrolle  un  programa  que,  dada  una  altura  y  anchura  solicitados  por  teclado, dibuje  el 
contorno de un rectángulo de dichas medidas. Debe validar que los dos números 
solicitados sean pares mayores a 4, ejemplo:  
Ancho: 10 
Alto: 5 
 
********** 
*        * 
*        * 
*        * 
**********        """

print("\nCrear un contorno de rectangulo con numeros pares mayores a 4")
print("---------------------------------------------------------------\n")

ancho = int(input("Ingrese el ancho del rectángulo (debe ser un número par mayor a 4): "))
alto = int(input("Ingrese el alto del rectángulo (debe ser un número par mayor a 4): "))

if ancho % 2 != 0 or alto % 2 != 0 or ancho <= 4 or alto <= 4:
    print("\nError: El ancho y el alto deben ser números pares mayores a 4.\n")
else:
    print("\nEl contorno resultante queda así:\n")
    for i in range(alto):
        if i == 0 or i == alto - 1:
            print("*" * ancho)
        else:
            print("*" + " " * (ancho - 2) + "*")