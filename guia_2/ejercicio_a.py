""" Ejercicio 1: Rotar circularmente las variables a, b, c y d de tipo int. """

a = 43
b = 12
c = 34
d = 70
aux_1 = 0
aux_2 = 0

aux_1 = a
a = d
d = aux_1

aux_2 = b
b = c
c = aux_2

print("\n",a, b, c, d,"\n")
