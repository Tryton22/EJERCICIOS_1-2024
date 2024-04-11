""" Ejercicio 15: 
Se trata de leer el valor de 3 longitudes y determinar si con ellas se forma geométricamente
un triangulo, determinando de que tipo: equilátero (si tiene tres lados iguales), isósceles (si
tiene dos lados iguales) o escaleno (si tiene tres lados desiguales). Considere que para formar
un triángulo se requiere que: "el lado mayor sea menor que la suma de los otros dos lados", lo
primero que se tiene que verificar e indicar en el programa. """

print("\nIngrese 3 valores para formar un triangulo.")
print('Recuerde: "el lado mayor es menor a la suma de los otros lados"')
print("------------------------------------------------------------------\n")

lado_1 = int(input("Ingrese un valor entero para el primer lado: "))
lado_2 = int(input("Ingrese un valor entero para el segundo lado: "))
lado_3 = int(input("Ingrese un valor entero para el tercer lado: "))

verifica_1 = False
verifica_2 = False
verifica_3 = False

if lado_1 > lado_2 and lado_1 > lado_3:
    suma_lados_1 = lado_2 + lado_3
    verifica_1 = lado_1 < suma_lados_1
elif lado_2 > lado_1 and lado_2 > lado_3:
    suma_lados_2 = lado_1 + lado_3
    verifica_2 = lado_2 < suma_lados_2
else:
    suma_lados_3 = lado_1 + lado_2
    verifica_3 = lado_3 < suma_lados_3

if verifica_1 == True:
    if lado_2 == lado_3:
        print("\nEl triangulo que se forma segun sus lados es isósceles.\n")
    else:
        print("\nEl triangulo que se forma segun sus lados es escaleno.\n")
elif verifica_2 == True:
    if lado_1 == lado_3:
        print("\nEl triangulo que se forma segun sus lados es isósceles.\n")
    else:
        print("\nEl triangulo que se forma segun sus lados es escaleno.\n")        
elif verifica_3 == True:
    if lado_2 == lado_1 == lado_3:
        print("\nEl triangulo que se forma segun sus lados es equilatero.\n")
    elif lado_2 == lado_1:
        print("\nEl triangulo que se forma segun sus lados es isósceles.\n")
    else:
        print("\nEl triangulo que se forma segun sus lados es escaleno.\n")
