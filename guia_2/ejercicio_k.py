""" Ejercicio 11: Usando Switch - Case crear un programa que al ingresar un numero del 1 al 4 haga:
1: Imprima el numero es un uno
2: Pedir un nuevo numero, sumar 10 e imprimirlo en pantalla.
3: Pedir un nuevo numero, restar 10 e indicar que el numero es negativo.
4: Generar un numero al azar y mostarlo.   
Cualquier otro numero: Muestre mensaje de equivacion en pantalla.    """

import random

def uno():
    print("El numero es un uno.\n")

def dos():
    num_nuevo = int(input("\nIngrese un numero nuevo: "))
    if num_nuevo > 0 and num_nuevo <= 9:
        num_nuevo = num_nuevo + 10
        print("El numero es:", num_nuevo,"\n")
    else:
        print("Ingrese un numero entre 1 y 9.\n")
        exit()

def tres():
    num_nuevo_1 = int(input("\nIngrese un numero nuevo: "))
    if num_nuevo_1 > 0 and num_nuevo_1 <= 9:
        num_nuevo_1 = num_nuevo_1 - 10
        print("El numero es:", num_nuevo_1,"y es negativo.\n")
    else:
        print("Ingrese un numero entre 1 y 9.\n")
        exit()

def cuatro():
    aleatorio = random.randint(1,9)
    print("\nEl numero elegido es:", aleatorio,"\n")

def otra_cosa():
    print("Ha ingresado un numero ilegal, ingrese uno entre 1 y 4.\n")
    exit()

opciones ={1: uno,
        2: dos,
        3: tres,
        4: cuatro
}

n = int(input("\nIngrese un numero entre 1 y 4: "))

try:
    opciones[n]()    
except KeyError:
    otra_cosa()