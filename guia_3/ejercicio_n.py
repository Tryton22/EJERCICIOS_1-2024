""" Ejercicio 14: 
Solicitar por teclado al usuario un número de 5 dígitos, y volver a solicitar cada vez que el 
usuario ingrese un número que no cumpla con el requisito, debe mostrar el siguiente aviso 
la primera  vez que  se  equivoque: “Debe  ingresar  un  numero  de 5  dígitos,  intente 
nuevamente”,    después  simplemente  debe  mostrar  el  siguiente  mensaje:  “Intente 
nuevamente”. (PROHIBIDO USAR LEN) """

print("\nSolicitar un numero de 5 digitos por teclado y verificar si tiene 5 digitos de verdad.")
print("------------------------------------------------------------------------------------------\n")
bandera = 0

while bandera < 2:
    numero_5 = int(input("Ingrese un numero de 5 digitos: "))
    if (numero_5 > 9999 and numero_5 < 100000) or (numero_5 < -9999 and numero_5 > -100000):
        print("\nEl numero ingresado si tiene los 5 digitos y el numero es:", numero_5,"\n")
        bandera = 2
    elif bandera == 0:
        print("\nDebe ingresar un numero de 5 digitos, intente nuevamente\n")
        bandera = 1
    else:
        print("\nIntente nuevamente\n")