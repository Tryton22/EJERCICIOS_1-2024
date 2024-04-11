""" Ejercicio 6: Desarrollar un programa que permita evaluar una expresión algebraica mediante numeros reales. """

print("\nExpresión a resolver: 6.57**(x/n)-3.987+8*(y-5)")

x = int(input("\nIngrese un valor para x: "))
y = int(input("Ingrese un valor para y: "))
n = int(input("Ingrese un valor para n: "))

if n > 0:
    ecuacion = 6.57 ** (x/n) - 3.987 + 8 * (y + 5)
    print("\nEl resultado de la ecuación es: {:.2f}".format(ecuacion),"\n")
else:
    print("\nIngrese un valor de n distinto de 0\n")
    exit()