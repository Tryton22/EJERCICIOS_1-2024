""" Ejercicio 19:
Basado  en  el  ejercicio  anterior,  solicite  un  tercer  digito,  y  reemplace  el  numero  D  por  el 
nuevo número ingresado. 
Ejemplo de lo solicitado: 
N = 436534535 
D = 3 
R = 9 
Resultado = 496594595  
Se aplican las mismas restricciones acerca de uso de funciones de array o string."""

print("\nBasado en el ejercicio anterior solicite un tercer digitos y reemplace D por el numero ingresado.")
print("---------------------------------------------------------------------------------------------------\n")

numero = int(input("Ingrese un número entero: "))
D = int(input("Ingrese el dígito a reemplazar (D): "))
R = int(input("Ingrese el nuevo dígito (R): "))

resultado = 0
posicion = 0

while numero > 0:
    digito = numero % 10
    if digito == D:
        digito = R
    resultado += digito * (10 ** posicion)
    posicion += 1
    numero //= 10

print("\nResultado:", resultado,"\n")
