Proceso Ejercicio_14
	
	Escribir " "
	
	Escribir "Solicitar un numero de 5 digitos por teclado y verificar si tiene 5 digitos de verdad."
	Escribir "-----------------------------------------------------------------------------------------"
	
	Escribir " "
	
	bandera <- 0
	
	Mientras bandera < 2 Hacer
		Escribir "Ingrese un numero de 5 digitos:"
		Leer numero_5
		
		Si (numero_5 > 9999 Y numero_5 < 100000) O (numero_5 < -9999 Y numero_5 > -100000) Entonces
			Escribir " "
			Escribir "El numero ingresado si tiene los 5 digitos y el numero es: ", numero_5
			Escribir " "
			bandera <- 2
		SiNo
			Si bandera == 0 Entonces
				Escribir " " 
				Escribir "Debe ingresar un numero de 5 digitos, intente nuevamente."
				Escribir " "
				bandera <- 1
			SiNo
				Escribir " "
				Escribir "Ingrese nuevamente"
				Escribir " "
			FinSi
		Fin Si
	Fin Mientras
FinProceso