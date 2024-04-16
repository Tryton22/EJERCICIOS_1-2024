Proceso Ejercicio_7
	
	Escribir " "
	
	Definir num_1, num_2, num_3 Como Entero
	
	Escribir "Ingrese 3 numeros enteros"
	Leer num_1
	Leer num_2
	Leer num_3
	
	Escribir " "
	
	suma <- num_1 + num_2 + num_3
	Escribir "La suma de los numeros ingresados es: ", suma
	
	Escribir " "
	
	producto <- num_1 * num_2 * num_3
	Escribir "El producto de los numeros ingresados es: ", producto
	
	Escribir " "
	
	promedio <- trunc(suma / 3)
	Escribir "El promedio de los numeros ingresados es: ", promedio
	
	Escribir " "
	
	Si num_1 > num_2 Y num_1 > num_3 Entonces
		Escribir "El numero mas grande de los ingresados es: ", num_1
		Si num_2 > num_3 Entonces
			Escribir "El numero mas pequeño de los ingresados es: ", num_3
			Escribir " "
		SiNo
			Escribir "El numero mas pequeño de los ingresados es: ", num_2
			Escribir " "
		FinSi
	SiNo
		Si num_2 > num_1 Y num_2 > num_3 Entonces
			Escribir "El numeros mas grande de los ingresados es: ", num_2
			Si num_1 > num_3 Entonces
				Escribir "El numero mas pequeño de los ingresados es: ", num_3
				Escribir " "
			SiNo
				Escribir "El numero mas pequeño de los ingresados es: ", num_1
				Escribir " "
			FinSi
		SiNo
			Escribir "El numero mas grande de los ingresados es: ", num_3
			Si num_1 > num_2 Entonces
				Escribir "El numero mas pequeño de los ingresados es: ", num_2
				Escribir " "
			SiNo
				Escribir "El numero mas pequeño de los ingresados es: ", num_1
				Escribir " "
			FinSi
		FinSi
	FinSi

FinProceso