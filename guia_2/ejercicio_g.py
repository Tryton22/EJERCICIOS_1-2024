""" Ejercicio 7: Analizar y desarrollar un programa que reciba 3 numeros enteros 
diferentes e imprima la suma, el promedio, el producto, el pequeño y el grande. """

num_1 = int(input("\nIngrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

suma = num_1 + num_2 + num_3
print("\nLa suma de los numeros es: ", suma)

producto = num_1 * num_2 * num_3
print("\nEl producto de los numeros es: ", producto)

promedio = suma // 3
print("\nEl promedio de los numeros es: ", promedio)

if num_1 > num_2 and num_1 > num_3:
    print("\nEl numero mas grande es: ", num_1)
    if num_2 > num_3:
        print("El numero mas pequeño es: ", num_3,"\n")
    else:
        print("El numero mas pequeño es: ", num_2,"\n")
elif num_2 > num_1 and num_2 > num_3:
    print("\nEl numero mas grande es: ", num_2)
    if num_1 > num_3:
        print("El numero mas pequeño es: ", num_3,"\n")
    else:
        print("El numero mas pequeño es: ", num_1,"\n")
else:
    print("\nEl numero mas grande es: ", num_3)
    if num_1 > num_2:
        print("El numero mas pequeño es: ", num_2,"\n")
    else:
        print("El numero mas pequeño es: ", num_1,"\n")