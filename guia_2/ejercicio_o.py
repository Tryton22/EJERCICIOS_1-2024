""" Ejercicio 15: 
Hacer un algoritmo que tome el peso en kilos de una cantidad de ropa a lavar en una lavadora
y nos devuelva el nivel dependiendo del peso. Se sabe que con más de 30 kilos la lavadora no
funcionara, ya que es demasiado peso. Si la ropa pesa 22 ó más kilos, el nivel será de máximo;
si pesa 15 ó más, el nivel será de alto; si pesa 8 ó más será un nivel medio o de lo contrario el
nivel será mínimo (Note que cada caso es mutuamente exclusivo y que la cantidad de ropa a
lavar sólo puede dar como resultado un solo nivel de carga, además de que la definición es
imprecisa a propósito). """

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