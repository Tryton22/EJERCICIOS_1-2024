Proceso Ejercicio_17
	
	Escribir " "
	
	Escribir "Separar un numero entero en 2: numero de sus digitos mayores y iguales a 5 y numeros con los digitos restantes."
	Escribir "------------------------------------------------------------------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese un numero entero: " Sin Saltar
	Leer numero_entero
	
	Escribir " "
	
	Si numero_entero < 0 Entonces
		Escribir "Por favor, ingresa un numero entero positivo."
		Escribir " "
	SiNo
		numero_mayor_igual_5 <- 0
		numero_menor_5 <- 0
		divisor <- 1
		
		Mientras numero_entero > 0 Hacer
			digito <- numero_entero MOD 10
			Si digito >= 5 Entonces
				numero_mayor_igual_5 <- digito * divisor + numero_mayor_igual_5
				divisor <- divisor * 10
			SiNo
				numero_menor_5 <- digito * divisor + numero_menor_5
				divisor <- divisor * 10
			FinSi
			numero_entero <- trunc(numero_entero / 10)
		FinMientras
		
		Escribir "Numero formado por digitos mayores o iguales a 5: ", numero_mayor_igual_5
		Escribir "Numero formado por digitos menores a 5: ", numero_menor_5
		Escribir " "
	FinSi
FinProceso