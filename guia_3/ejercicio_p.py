""" Ejercicio 16:
Analizar  y  construir  un  programa  que,  dado  un  numero  entero  positivo,  lo  transforme  a 
numero binario, no puede usar funciones del lenguaje ni usar tipo de dato string. """

print("\nTransformar un numero entero a numero binario.")
print("--------------------------------------------------\n")

numero_entero = int(input("Ingresa un número entero positivo: "))

if numero_entero < 0:
    print("\nPor favor, ingresa un número entero positivo.\n")
else:
    if numero_entero == 0:
        print("\nEl número binario equivalente es: 0\n")
    else:
        binario = 0
        lugar = 0
        while numero_entero > 0:
            rem = numero_entero % 2
            binario += rem * (10 ** lugar)
            lugar += 1
            numero_entero //= 2
        
        print("\nEl número binario equivalente es:", binario,"\n")
