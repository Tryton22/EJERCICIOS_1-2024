"""Ejercicio 6:
Cree una función max(b) que, al entregarle un arreglo b de enteros, retorne el 
mayor valor entre los contenidos en b (retornaría un entero). Pruebe su 
funcionamiento preguntando por teclado el parámetro a ingresar."""

def Max(b):
    mayor = b[0]
    for i in b:
        if i > mayor:
            mayor = i
    
    return mayor

arreglo_b = []
suma = 0

while suma <= 4:
    numero = int(input("\nIngrese un numero para el arreglo: "))
    arreglo_b.append(numero)
    suma += 1

print("\nEl numero mayor del arreglo ingresado es: ", Max(arreglo_b),"\n")