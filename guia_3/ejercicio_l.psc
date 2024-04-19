Proceso Ejercicio_12
	
	Escribir " "
	
	Escribir "Calcular el factorial de un valor mayor a 5 y menor que 15."
	Escribir "--------------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingresar un numero mayor a 5 y menor que 15: "
	Leer numero_factorial
	
	Escribir " "
	
	factorial <- 1
	
	Si numero_factorial > 5 Y numero_factorial < 15 Entonces
		Para i <- 1 Hasta numero_factorial Con Paso 1 Hacer
			factorial <- factorial * i
		Fin Para
		
		Escribir "El factorial del numero ", numero_factorial," es: ", factorial
		Escribir " "
	SiNo
		Escribir "Siga la instrucciones, por favor."
		Escribir " "
	FinSi
	
	
	
FinProceso
