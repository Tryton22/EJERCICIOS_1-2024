""" Ejercicio 15:
A  partir  de  un  ciclo  for,  donde  la  variable  i  debe  recorrer  un  rango  dado  por  el  usuario, 
cuyo requisito para el rango es haber una diferencia de mínimo 20 entre el inicio y el fin.  
Cada  número  debe  ser  multiplicado  por  la  siguiente  serie  de  números:  3,  4,  5,  6.  Se 
multiplica  en  el  orden  de  la  secuencia,  y  una  vez  que  se  acabe,  se  volverá  a  multiplicar 
desde el primer número otra vez (el 3).
Cada iteración, deberá mostrar la multiplicación de la siguiente manera (salida por 
pantalla): 
1 x 3 = 3 
2 x 4 = 8 
3 x 5 = 15 
4 x 6 = 24 
5 x 3 = 15 
6 x 4 = 24  """

print("\nSecuencia de multiplicación en un rango con una diferencia de 20\n")
print("------------------------------------------")

numero_inicial =int(input("\nIngrese un numero inicial para su rango: "))
numero_final= int(input("Ingrese un numero final para su rango: "))

diferencia = numero_final - numero_inicial

if diferencia >= 20:
    for i in range(numero_inicial, numero_final + 1):
        factor = (i - numero_inicial) % 4

        suma = 3 + factor
        resultado = i * suma

        print ("\n",i, "x", suma,"=", resultado)
else:
    print("\nSiga las instrucciones, por favor\n")