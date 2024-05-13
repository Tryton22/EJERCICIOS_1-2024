"""Ejercicio 5:
Cree la función pares(a) que al entregarle un arreglo a como parámetro, retorne 
un arreglo que contenga sólo los números pares dentro del arreglo original. Pruebe 
su funcionamiento preguntando por teclado el parámetro a ingresar."""

def Pares(a):
    arreglo_pares = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            arreglo_pares.append(a[i])
    
    return arreglo_pares

arreglo_a = []
suma = 0

while suma <= 4:
    numero = int(input("\nIngrese un numero: "))
    arreglo_a.append(numero)
    suma += 1

print("\nEl nuevo arreglo solo con números pares es:",Pares(arreglo_a),"\n")