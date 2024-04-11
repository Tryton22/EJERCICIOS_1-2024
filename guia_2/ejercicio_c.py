""" Ejercicio 3: Dado un numero de 5 digitos muestre cada digito por separado. """

num = int(input("\nIngrese un numero con 5 digitos: "))

d_1 = num // 10000
d_2 = num // 1000 % 10
d_3 = num // 100 % 10
d_4 = num // 10 % 10
d_5 = num % 10

print(" \nNumero: ", num," separado por digitos:")
print(d_1,",",d_2,",",d_3,",",d_4,",",d_5,"\n")