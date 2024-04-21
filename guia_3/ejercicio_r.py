""" Ejercicio 18:
Realice  un  programa  que  dado  dos  números  enteros  por  teclado  (D  y  N),  elimine  del 
número N todas las apariciones del digito D, debe validar que N sea un numero de más de 
4 dígitos y que D sea solo un digito, ambos enteros. Ejemplo de lo solicitado: 
N = 436534535 
D = 3 
Resultado = 465455  
No se pueden usar métodos de string (replace() o similares)  """

print("\nIngrese 1 numero entero (N) y 1 digito (D) y elimine de N todas las apariciones de D")
print("-------------------------------------------------------------------------------\n")

N = int(input("Ingrese un número entero de más de 4 dígitos (N): "))
D = int(input("Ingrese el dígito que desea eliminar (D): "))

if N < 10000:
    print("\nError: N debe tener más de 4 dígitos.\n")
elif D < 0 or D > 9:
    print("\nError: D debe ser un solo dígito.\n")
else:
    resultado = 0  
    posicion = 0   
    
    while N > 0:
        digito = N % 10
        if digito != D:
            resultado += digito * (10 ** posicion)
            posicion += 1
        N //= 10  
    
    if resultado == 0:
        print("\nResultado: 0\n")
    else:
        print("\nResultado:", resultado,"\n")