""" Ejercicio 12: 
Calcule  la  factorial  de  un  número  positivo mayor  a  5 y menor  a  15  ingresado  por teclado 
(asegúrese de que el usuario deba ingresar un valor válido). Un factorial es el producto de 
todos los números desde 1 hasta el número, por ejemplo: el factorial de 5 es: 5*4*3*2*1 = 
120. """

numero_fact = int(input("\nIngrese un numero mayor a 5 y menor a 15: "))

if 5 < numero_fact < 15:

    factorial = 1

    for i in range(1, numero_fact+1):
        factorial *= i
        
    print("\nEl factorial de", numero_fact,"es:", factorial,"\n")

else:
    
    print("\nSiga las instrucciones, por favor.\n")
    exit()