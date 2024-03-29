# Ejercicio 11: Crear un programa de lea 5 números y entregue el promedio de estos.

x = 1
suma = 0

print("Promedio de 5 numeros.")
print("")

while x <= 5:
    print("Numero", x)
    n = int(input())
    suma = suma + n
    x = x + 1

promedio = suma/5

print("")

print("El promedio de los numeros ingresados es: ", promedio)
