"""Ejercicio 7:
Cree una función que al entregarle un número entero n, devuelva una matriz de 
dimensión nxn con números enteros ordenados. Pruebe su funcionamiento 
preguntando por teclado el parámetro a ingresar. Ej.- la salida de la función 
Gmatriz(4) sería: 
 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 
 
Con Gmatriz(3) sería: 
 
1 2 3  
4 5 6  
7 8 9  
    
Note que al ingresar 0 debería entregar un mensaje de error y si se ingresa 1 se 
generaría un arreglo que contenga un arreglo con un sólo elemento. """

def Gmatriz(n):
    if n == 0:
        print("Error, imposible crear una matriz con este número.")
    elif n == 1:
        matriz = [n]
        print(matriz)
        return matriz        
    else:
        matriz = [] 
        numero = 1

        for i in range(n):
            matriz.append([])
            for j in range(n):
                matriz[i].append(numero)
                numero += 1

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                print(matriz[i][j], end=" ")
            print("")
        
        return matriz

Gmatriz(1)
