""" Ejercicio 13: 
Hacer un algoritmo que tome el peso en kilos de una cantidad de ropa a lavar en una lavadora
y nos devuelva el nivel dependiendo del peso. Se sabe que con más de 30 kilos la lavadora no
funcionara, ya que es demasiado peso. Si la ropa pesa 22 ó más kilos, el nivel será de máximo;
si pesa 15 ó más, el nivel será de alto; si pesa 8 ó más será un nivel medio o de lo contrario el
nivel será mínimo (Note que cada caso es mutuamente exclusivo y que la cantidad de ropa a
lavar sólo puede dar como resultado un solo nivel de carga, además de que la definición es
imprecisa a propósito)."""

peso_ropa = int(input("\nIngrese los kilos de ropa que desea lavar: "))

try:
    if peso_ropa >= 30:
        print("\nLa lavadora tiene mucho peso, no funciona.\n")
    elif peso_ropa >= 22:
        print("\nNivel de carga: Máximo\n")
    elif peso_ropa >= 15:
        print("\nNivel de carga: Alto\n")
    elif peso_ropa >= 8:
        print("\nNivel de carga: Medio\n")
    elif 0 < peso_ropa < 8:
        print("\nNivel de carga: Mínimo.\n")
    else:
        print("\nIngrese un numero valido, por favor.\n")
except ValueError:
    print("\nIngrese un numero, por favor.\n")
    exit()