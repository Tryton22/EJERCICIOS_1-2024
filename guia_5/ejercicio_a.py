"""Ejercicio 1:
Hacer una función que reciba tres palabras y que imprima línea por línea las 
primeras, segundas, etc. letras de las palabras en orden. Por ejemplo, llamándola 
con "Hola", "como" y "estas", el resultado sería: 
    H c e 
    o o s 
    l m t 
    a o a 
        s    """

def Imprimir_linea(palabra1, palabra2, palabra3):
    largo_max = max(len(palabra1), len(palabra2), len(palabra3))
    
    for i in range(largo_max):
        letra = ""
        for palabra in (palabra1, palabra2, palabra3):
            if i < len(palabra):
                letra += palabra[i] + " "
            else:
                letra += "  "
        print(letra)

Imprimir_linea("Hola", "como", "estas")
