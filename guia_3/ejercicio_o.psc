Proceso Ejercicio_15
	
	Escribir " "
	
	Escribir "Secuencia de multiplación en un rango con una diferencia de 20"
	Escribir "---------------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese un numero incial para su rango: "
	Leer numero_inicio
	
	Escribir "Ingrese un numero final para su rango: "
	Leer numero_final
	
	Escribir " "
	
	diferencia <- numero_final - numero_inicio
	
	Si diferencia >= 20 Entonces
		Para i <- numero_inicio Hasta numero_final Con Paso 1 Hacer
			factor <- (i - numero_inicio) MOD 4
			suma <- 3 + factor
			resultado <- i * suma
			
			Escribir i," x ", suma," = ", resultado
			Escribir " "
		Fin Para
	SiNo
		Escribir "Siga las instrucciones, por favor."
		Escribir " "
	FinSi
	
FinProceso