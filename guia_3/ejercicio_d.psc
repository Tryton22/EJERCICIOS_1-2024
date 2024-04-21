Proceso Ejercicio_4
	
	Escribir " "
	
	Escribir "Sumar todos los numero hasta que se ingrese un 0"
	Escribir "---------------------------------------------------"
	
	Escribir " "
	
	suma <- 0
	numero_suma <- 1
	
	Mientras numero_suma > 0 Hacer
		Escribir "Ingrese un numero: "
		Leer numero_suma
		Si numero_suma > 0 Entonces
			Escribir " "
			Escribir "Numero ", numero_suma," ingresado"
			Escribir " "
		FinSi
		suma <- suma + numero_suma
	Fin Mientras
	
	Escribir "La suma de los numeros ingresados es: ", suma
	Escribir " "
FinProceso