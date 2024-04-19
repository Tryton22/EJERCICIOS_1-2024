""" Ejercicio 11:
Solicite  al  usuario  ingresar  5  números  y  a  continuación  muestre  por  pantalla  el  número 
mayor y el número menor. """

cantidad = 5
mayor = 0
menor = 99999

while cantidad > 0:
    numero = int(input("\nNumero : "))
    cantidad -= 1
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
 
print("\nEl numero mas grande es:", mayor)
print("El numero mas pequeño es:", menor,"\n")