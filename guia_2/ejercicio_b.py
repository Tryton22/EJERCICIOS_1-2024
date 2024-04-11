""" Ejercicio 2: Dado un numero de 5 digitos muestre cada digito por separado desde la unidad en adelante. """

numero = int(input("\nIngrese un número de 5 digitos: "))

d_1 = numero // 10000
d_2 = numero // 1000 % 10
d_3 = numero // 100 % 10
d_4 = numero // 10 % 10
d_5 = numero % 10

print("\nNúmero: ", numero," separado por digitos desde la unidad en adelante: ")
print(d_5,",",d_4,",",d_3,",",d_2,",",d_1,"\n")