Proceso Ejercicio_11
	
	Escribir " "
	
	Escribir "Solicitar 5 numeros y mostar el numero mayor y menor."
	Escribir "-------------------------------------------------------"
	
	Escribir " "
	
	cantidad <- 5
	n <- 1
	mayor <- 0
	menor <- 99999999
	
	Mientras cantidad > 0 Hacer
		Escribir "El numero ingresado ", n," es:"
		Leer numero_1
		Escribir " "
		n <- n + 1
		cantidad <- cantidad - 1
		Si numero_1 > mayor Entonces
			mayor <- numero_1
		FinSi
		Si numero_1 < menor Entonces
			menor <- numero_1
		FinSi
	Fin Mientras
	
	Escribir "El numero mas grande de los ingresados es: ", mayor
	Escribir "El numero mas peque�o de los ingresados es ", menor
	Escribir " "
FinProceso