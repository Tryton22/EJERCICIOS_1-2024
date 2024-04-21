""" Ejercicio 20:
Desarrolle  un  programa  que,  dada  una  altura  y  anchura  solicitados  por  teclado, dibuje  el 
contorno de un rectángulo de dichas medidas. Debe validar que los dos números 
solicitados sean pares mayores a 4, ejemplo:  
Ancho: 10 
Alto: 5 
 
********** 
*        * 
*        * 
*        * 
**********        """

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
