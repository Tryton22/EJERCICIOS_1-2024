""" Ejercicio 10: Leer un numero de 6 digitos. separar sus digitos e imprimirlos
por separado. Luego, evaluar si el ultimo digito es par, primo o natural. 
Indique en pantalla. """

digitos = int(input("\nIngrese un numero de 6 digitos: "))

if (digitos > 99999 and digitos < 1000000) or (digitos < -99999 and digitos > -1000000):
    d_1 = digitos // 100000
    d_2 = digitos // 10000 % 10
    d_3 = digitos // 1000 % 10
    d_4 = digitos // 100 % 10
    d_5 = digitos // 10 % 10
    d_6 = digitos % 10

    print("\nEl digito 1 es:", d_1)
    print("El digito 2 es:", d_2)
    print("El digito 3 es:", d_3)
    print("El digito 4 es:", d_4)
    print("El digito 5 es:", d_5)

    if d_6 % 2 == 0:
        print("El digito 6 es:", d_6,"y es par.\n")
    elif d_6 == 3 or d_6 == 5 or d_6 == 7:
        print("El digito 6 es:", d_6,"y es primo.\n")
    else:
        print("El digito 6 es:", d_6,"y es natural.\n")
else:
    print("Ingrese un numero de 6 digitos por favor.")
    exit()