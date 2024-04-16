Proceso Ejercicio_15
	
	Escribir " "
	
	Escribir "Ingrese 3 valores para formar un triangulo: "
	Escribir "Recuerde:"
	Escribir "El lado mayor es menor a la suma de los otros lados."
	Escribir "---------------------------------------------------------"
	
	Escribir " "
	
	Definir lado_1, lado_2, lado_3 Como Entero
	
	Escribir "Ingrese un valor entero para el primer lado"
	Leer lado_1
	Escribir "Ingrese un valor entero para el segundo lado"
	Leer lado_2
	Escribir "Ingrese un valor entero para el tercer lado"
	Leer lado_3
	
	Escribir " "
	
	verifica_1 <- Falso
	verifica_2 <- Falso
	verifica_3 <- Falso
	
	Si lado_1 > lado_2 Y lado_1 > lado_3 Entonces
		suma_lados_1 <- lado_2 + lado_3
		verifica_1 <- lado_1 < suma_lados_1
	SiNo
		Si lado_2 > lado_1 Y lado_2 > lado_3 Entonces
		suma_lados_2 <- lado_1 + lado_3
		verifica_2 <- lado_2 < suma_lados_2
		SiNo  
			suma_lados_3 <- lado_1 + lado_2
			verifica_3 <- lado_3 < suma_lados_3
		FinSi		
	Fin Si
	
	Si verifica_1 == Verdadero Entonces
		Si lado_2 == lado_3 Entonces
			Escribir "El triangulo que se forma es isosceles"
			Escribir " "
		SiNo
			Escribir "El triangulo que se forma es escaleno"
			Escribir " "
		Fin Si
	SiNo
		Si verifica_2 == Verdadero Entonces
			Si lado_1 == lado_3 Entonces
				Escribir "El triangulo que se forma es isosceles"
				Escribir " "
			SiNo
				Escribir "El triangulo que se forma es escaleno"
				Escribir " "
			Fin Si
		SiNo
			Si verifica_3 == Verdadero Entonces
				Si lado_1 == lado_2 Y lado_2 == lado_3 Entonces
					Escribir "El triangulo que se forma es equilatero"
					Escribir " "
				SiNo
					Si lado_2 == lado_1 Entonces
						Escribir "El triangulo que se forma es isosceles"
					SiNo
						Escribir "El triangulo que se forma es escaleno"
					FinSi
				Fin Si
			SiNo
				Escribir " "
			Fin Si
		Fin Si
	Fin Si
	
FinProceso