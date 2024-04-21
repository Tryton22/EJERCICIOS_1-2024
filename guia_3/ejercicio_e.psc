Proceso Ejercicio_5
	
	Escribir " "
	
	Escribir "Promediar todos los numero hasta que se ingrese un 0"
	Escribir "---------------------------------------------------"
	
	Escribir " "
	
	suma <- 0
	numero_suma <- 1
	promedio <- 0
	
	Mientras numero_suma > 0 Hacer
		Escribir "Ingrese un numero: "
		Leer numero_suma
		Si numero_suma > 0 Entonces
			Escribir " "
			Escribir "Numero ", numero_suma," ingresado"
			Escribir " "
			promedio <- promedio + 1
		FinSi
		suma <- suma + numero_suma
	Fin Mientras
	
	Escribir " "
	Escribir "El promedio de los numeros ingresados es: ", trunc(suma / promedio)
	Escribir " "
FinProceso