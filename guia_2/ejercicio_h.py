""" Ejercicio 8: Dado un numero positivo evaluar: Si es menor a 500 sumar el 50%,
si es mayor o igual a 500 pero menor o igual a 1000 sumar el 7%, si es mayor a 
1000 y menor o igual a 5000 dividir por 2 y si es mayor a 5000 restar 1/4 del mismo. """

numero = int(input("\nIngrese un numero positivo: "))

if numero > 0:
    if numero < 500:
        porc_1 = 50 * numero // 100
        valor_1 = numero + porc_1 
        print("\nEl numero", numero,"despues de la evaluacion queda en:", valor_1,"\n")
    elif numero >= 500 and numero <= 1000:
        porc_2 = 7 * numero // 100
        valor_2 = numero + porc_2
        print("\nEl numero", numero,"despues de la evaluacion queda en:", valor_2,"\n")
    elif numero > 1000 and numero <= 5000:
        valor_3 = numero // 2
        print("\nEl numero", numero,"despues de la evaluacion queda en:", valor_3,"\n")
    else:
        resta = numero // 4
        valor_4 = numero - resta
        print("\nEl numero", numero,"despues de la evaluacion queda en:", valor_4,"\n")
else:
    print("\nIngrese un valor mayor a 0, por favor\n")
    exit()