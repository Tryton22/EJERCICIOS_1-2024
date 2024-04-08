Proceso ejercicio_k
	
	x <- 1
	suma <- 0
	
	Escribir "Promedio de 5 numeros."
	
	Escribir ""

	Mientras x <= 5 Hacer
		Escribir "Numero ", x
		Leer n
		Escribir ""
		suma <- suma + n
		x <- x + 1
	Fin Mientras
	
	promedio <- suma/5
	
	Escribir ""
	
	Escribir "El promedio de los numeros ingresados es: ", promedio
	
	Escribir ""

FinProceso
