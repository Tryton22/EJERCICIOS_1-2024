""" Ejercicio 6:
Dada una cadena con el formato "DD/MM/AAaa" (día, mes, año) mostrar la misma 
información en pantalla en lenguaje natural. Ejemplo: "19/09/1996" entregaría por 
pantalla "19 de septiembre de 1996". """

print("\nDada una cadena en formato (DD/MM/aaa) muestre la información en lenguaje natural.")
print("------------------------------------------------------------------\n")

meses = { 
    "01" : "enero", "02" : "febrero", "03" : "marzo", "04" : "abril",
    "05" : "mayo", "06" : "junio", "07" : "julio", "08" : "agosto",
    "09" : "septiembre", "10" : "octubre", "11" : "noviembre", "12" : "diciembre"
}

fecha = input("Ingrese una fecha con el formato 'DD/MM/aaaa': ")

datos = fecha.split("/")

mes_natural = meses.get(datos[1],"")

fecha_natural = f"{datos[0]} de {mes_natural} de {datos[2]}"

print("\nCadena orginal:",fecha,"\n")
print("Cadena en lenguaje natural:",fecha_natural,"\n")