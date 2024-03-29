#Ejercicio 1: Crear un programaque solicita la distancia en kilometros y el tiempo que le toma recorrer esa distancia para calcular su velocidad media.

print("Ingrese la distancia recorrida por el bus (KM): ")
d = int(input())

print("")


print("Ingrese el tiempo que tardo en recorrerla (HR): ")
t = int(input())

print("")

velocidad = d / t

print("La velocidad media del bus en recorrer", d,"km en", t,"h es de:", round(velocidad),"km/h")