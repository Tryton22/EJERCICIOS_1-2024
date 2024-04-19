"""Ejercicio 2: 
Hallar  todos  los  números  impares  en  un  rango  dado  por  el  usuario,  
incluyendo  los  extremos. """

print("\nIngresar un rango de numeros para buscar numeros impares.")
print("--------------------------------------------------------------")

num_inicio = int(input("\nIngrese un numero de inicio: "))
num_final = int(input("Ingrese un numero de termino: "))

print("\nLos numeros impares de su rango son: ")

n = 1

if num_final > num_inicio:
    for x in range(num_inicio,num_final+1):
        if x % 2 != 0:
            print("Numero impar", n,":", x,"\n")
            n += 1

else:
    print("Ingrese un valor inicial menor al final, por favor.")
    exit()