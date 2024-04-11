""" Ejercicio 5: Al ejercicio anterior agregue que el programa verifique si efectivamente se ingresaron 5 digitos. """

numero = int(input("\nIngrese un numero de 5 digitos: "))

d_1 = numero // 10000
d_2 = numero // 1000 % 10
d_3 = numero // 100 % 10
d_4 = numero // 10 % 10
d_5 = numero % 10

if (numero > 9999 and numero < 100000) or (numero < -9999 and numero > -100000):
    print("\nEl numero", numero,"invertido es:", "%d%d%d%d%d" % (d_5,d_4,d_3,d_2,d_1),"\n")
else:
    print("Ingrese un valor de 5 digitos, por favor\n")
    exit()