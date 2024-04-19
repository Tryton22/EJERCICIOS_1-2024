Proceso Ejercicio_8
	
	Escribir " "
	
	Escribir "Realizar la sumatoria de numeros en un rango ingresado."
	Escribir "--------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese el numero incial del rango: "
	Leer numero_menor
	
	Escribir "Ingrese el numero final del rango: "
	Leer numero_mayor
	
	suma <- 0
	
	Escribir " "
	
	Si numero_mayor > numero_menor Entonces
		Para i <- numero_menor Hasta numero_mayor Con Paso 1 Hacer
			suma <- suma + i
			
		Fin Para
	SiNo
		Escribir "Ingrese el rango ingresando primero el menor, por favor."
		Escribir " "
	FinSi
	
	Escribir "La sumatoria del rango ingresado es: ", suma
	Escribir " "
	
FinProceso