Proceso Ejercicio_10
	
	Escribir " "
	
	Escribir "Encontrar el MCD entre 48 y 60"
	Escribir "--------------------------------"
	
	Escribir " "
	
	menor <- 48
	mayor <- 60
	mcd <- 0
	
	Para i <- 1 Hasta menor Con Paso 1 Hacer
		Si menor MOD i == 0 Y mayor MOD i == 0 Entonces
			mcd <- i
		FinSi
	Fin Para
	
	Escribir "El MCD entre 48 y 60 es: ", mcd
	Escribir " "
FinProceso