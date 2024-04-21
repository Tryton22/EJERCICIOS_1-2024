Proceso Ejercicio_3
	
	Escribir " "
	
	Escribir "Evaluar si un numero mayor a 20 es primo."
	Escribir "-------------------------------------------"
	
	Escribir " "
	
	Definir num_mayor, primo Como Entero
	
	Escribir "Ingrese un numero mayor a 20: "
	Leer num_mayor
	
	primo <- 0
	
	Si num_mayor > 20 Entonces
		Para i <- 2 Hasta num_mayor Con Paso 1 Hacer
			Si num_mayor MOD i == 0 Entonces
				primo <- primo + 1
			FinSi
		Fin Para
		
		Escribir primo
		
		Si primo == 1 Entonces
			Escribir "El numero ingresado: ", num_mayor," es primo."
			Escribir " "
		SiNo
			Escribir "El numero ingresado: ", num_mayor," no es primo."
			Escribir " "
		FinSi
	SiNo
		Escribir "Siga las instrucciones, por favor."
		Escribir " "
		
	FinSi
FinProceso