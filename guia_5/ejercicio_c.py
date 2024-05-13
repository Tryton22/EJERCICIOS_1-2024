"""Ejercicio 3.
Calcule la siguiente expresión para un N (N>0) ingresado por el usuario por medio 
de una función.  
n=5→p→ 1/5+2/5+3/5+4/5+5/5 
n=4→p→ 1/4+2/4+3/4+4/4 """

def Funcion_dada(n):
    suma = 0
    if n > 0:
        for i in range(1,n+1):
            suma += i/n
    
        return suma
    else:
        return "Número inválido.\n"

print("\nCalcular la expresión (n -> 1/n + 2/n + ....n/n) con un n > 0 ingresado por el usuario.")
print("--------------------------------------------------------------------------------------------\n")

n = int(input("Ingrese un valor para n mayor a 0: "))

calculadora = Funcion_dada(n)

print("\nEl resultado de la expresión con un n igual a", n,"es:", calculadora,"\n")