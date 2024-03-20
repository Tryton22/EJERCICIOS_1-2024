#Ejercicio 9: Crear un programa que haga lo del ejercicio 8 y ademas sume los valores de y, los muestre en pantalla y saque el promedio

print("")

print("Ecuacion lineal a resolver y=ax+b")

print("")

print("Ingrese un valor para a: ")
a = int(input())

print("")

print("Ingrese un valor para b: ")
b = int(input())

print("")

y_1 = a + b
y_2 = a * 2 + b
y_3 = a * 3 + b
y_4 = a * 4 + b

print("El valor de la ecuacion para x = 1 seria:", y_1)
print("El valor de la ecuacion para x = 2 seria:", y_2)
print("El valor de la ecuacion para x = 3 seria:", y_3)
print("El valor de la ecuacion para x = 4 seria:", y_4)

print("")

suma_total = y_1 + y_2 + y_3 + y_4
promedio_suma = suma_total / 4

print("El valor de la suma de los valores de y es:", suma_total)
print("El promedio de los valores de y es:", round(promedio_suma))