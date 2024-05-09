""" Ejercicio 7:
Tomando en cuenta el mismo tipo de entrada anterior, cree un programa en 
donde se muestre una cadena que contenga la fecha en formato norteamericano, 
es decir "MM-DD-aa" donde "aa" son los últimos 2 dígitos del año (recuerde que 
este resultado debe quedar guardado en una variable string). Ejemplo: 
"12/10/2013" entregaría por pantalla "10-12-13". """

print("\nDado el ejercicio anterior crear una cadena con formato de fecha norteamericana (MM-DD-aa)")
print("----------------------------------------------------------------------------------------------\n")

fecha = input("Ingrese una fecha con el formato 'DD/MM/aaaa': ")

datos = fecha.split("/")

anio_americano = datos[2][2:]

fecha_nueva = datos[1], datos[0], anio_americano

print("\nLa fecha original es:", fecha,"\n")

print("La fecha en formato americano es:",end=" ")

print("-".join(fecha_nueva),"\n")