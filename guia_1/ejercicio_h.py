#Ejercicio 8: Crear un programa que dada la ecuacion lineal y=ax+b pida a y b y luego calcule y para distintos valores de x

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