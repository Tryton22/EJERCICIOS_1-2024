""" Ejercicio 9: Aplique las siguientes instrucciones a un numero ingresado en la
secuencia que se muestra: 
- Si es par mayor que 10 restar 10
- Si es impar mayor que 50 sumar 12
- Si es par <50 sumar 20
- Si es impar sumar 1                     """

num = int(input("\nIngrese un numero: "))
print("\nEl numero original es:", num,"\n")

if num % 2 == 0 and num > 10:
    num = num - 10
    print("Se resta 10.")
if num % 2 != 0 and num > 50:
    num = num + 12
    print("Se suma 12.")
if num % 2 == 0 and num < 50:
    num = num + 20
    print("Se suma 20.")
if num % 2 != 0 :
    num = num + 1
    print("Se suma 1.")

print("\nAl final el numero quedo en:", num,"\n")
