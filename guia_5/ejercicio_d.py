"""Ejercicio 4:
Función que calcule la distancia entre dos puntos (x1,y1) y (x2,y2). 
OBS: Revise el teorema de pitágoras. """
 
import math 

def Distancia_puntos(a,b,c,d):
    distancia = math.sqrt((b - a)**2 + (d - c)**2)
    return distancia

x_1 = int(input("\nIngrese la primera coordenada de x: "))
x_2 = int(input("Ingrese la segunda coordenada de x: "))
y_1 = int(input("Ingrese la primera coordenada de y: "))
y_2 = int(input("Ingrese la segunda coordenada de y: "))

distancia_final = Distancia_puntos(x_1,x_2,y_1,y_2)

print("\nLa distancia entre las coordenadas ingresadas es de:",round(distancia_final),"\n")