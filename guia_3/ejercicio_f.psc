Proceso Ejercicio_6 
	
	Escribir " "
	
	Escribir "Los numeros primos entre 10 y 100 son: "
	Escribir "-------------------------------------------"
	
	Escribir " "
	
	primos <- 0
	divisores <- 0
	
	Para i <- 10 Hasta 100 Con Paso 1 Hacer
		Para j <- 2 Hasta i Con Paso 1 Hacer
			Si (i MOD j) == 0 Entonces
				divisores <- divisores +1
			FinSi
		FinPara
		Si divisores == 1 Entonces
			Escribir " "
			Escribir "El numero ", i," es primo"
			primos <- primos + 1
		FinSi
		divisores <- 0
	Fin Para
	
	Escribir " "
	Escribir "Entre 10 y 100 existen ", primos," numeros primos"
	Escribir " "
	
FinProceso