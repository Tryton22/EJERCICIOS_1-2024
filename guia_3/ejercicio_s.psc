Proceso Ejercicio_19
	
	Escribir " "
	
	Escribir "Basado en el ejercicio anterior solicite un tercer digitos y reemplace D por el numero ingresado."
	Escribir "---------------------------------------------------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese un numero entero: " Sin Saltar
	Leer numero_entero
	Escribir "Ingrese el digito a reemplazar (D): " Sin Saltar
	Leer d
	Escribir "Ingrese el nuevo digito (R): " Sin Saltar
	Leer r
	
	Escribir " "
	
	resultado <- 0
	posicion <- 0
	
	Mientras numero_entero > 0 Hacer
		digito <- numero_entero MOD 10
		Si digito = d Entonces
			digito <- r
		FinSi
		resultado <- resultado + digito * (10 ^ posicion)
		posicion <- posicion + 1
		numero_entero <- trunc(numero_entero / 10)
	FinMientras
	
	Escribir "El resultado de los cambios fue: ", resultado
	Escribir " "
FinProceso