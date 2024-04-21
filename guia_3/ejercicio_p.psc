Proceso Ejercicio_16
	
	Escribir " "
	
	Escribir "Transformar un numero entero a numero binario."
	Escribir "------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese un numero entero positivo: " Sin Saltar
	Leer numero_entero
	
	Escribir " "
	
	Si numero_entero < 0 Entonces
		Escribir "Por favor, ingresa un numero entero positivo."
		Escribir " "
	SiNo
		Si numero_entero == 0 Entonces
			Escribir "El numero binario equivalente es: 0"
			Escribir " "
		SiNo
			binario <- 0
			lugar <- 0
			
			Mientras numero_entero > 0 Hacer
				rem <- numero_entero MOD 2
				Escribir rem
				binario <- binario + rem * (10 ^ lugar)
				lugar <- lugar + 1
				numero_entero <- trunc(numero_entero / 2)
			FinMientras 
			
			Escribir "El numero binario equivalente es: ", binario
			Escribir " "
		FinSi
	FinSi
FinProceso