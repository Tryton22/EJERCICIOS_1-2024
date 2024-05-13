"""Ejercicio 2:
Hacer una función que reciba un string y que retorne el mismo string pero sin las 
vocales. Por ejemplo, para un input de "Yo no fuí", debería mostrar "Y n f".  """

def Sin_vocales(cadena):

    vocales = 'aeiou'
    no_vocales = ''

    for i in cadena:
        if i in vocales:
            no_vocales  = no_vocales
        else:
            no_vocales += i
    return no_vocales



cadena = "Yo no fui"
cadena_sin_vocales = Sin_vocales(cadena)

print("\nLa cadena original es:",cadena,"\n")
print("La cadena sin vocales es:",cadena_sin_vocales,"\n")