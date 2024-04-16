Proceso Ejercicio_8
	
	Escribir " "
	
	Definir numero_positivo Como Entero
	
	Escribir "Ingrese un numero positivo y entero:"
	Leer numero_positivo
	
	Escribir " "
	
	Si numero_positivo > 0 Entonces
		Si numero_positivo < 500 Entonces
			porcentaje_1 <- trunc(50 * numero_positivo / 100)
			valor_1 <- numero_positivo + porcentaje_1
			Escribir "El numero ", numero_positivo," queda en: ", valor_1
			Escribir " "
		SiNo
			Si numero_positivo >= 500 Y numero_positivo <= 1000 Entonces
				porcentaje_2 <- trunc(7 * numero_positivo / 100)
				valor_2 <- numero_positivo + porcentaje_2
				Escribir "El numero ", numero_positivo," queda en: ", valor_2
				Escribir " "
			SiNo
				Si numero_positivo > 1000 Y numero_positivo <= 5000 Entonces
					valor_3 <- trunc(numero_positivo / 2)
					Escribir "El numero ", numero_positivo," queda en: ", valor_3
					Escribir " "
				SiNo
					resta <- trunc(numero_positivo / 4)
					valor_4 <- numero_positivo - resta
					Escribir "El numero ", numero_positivo," queda en: ", valor_4
					Escribir " "
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir "Ingrese un numero mayor a 0, por favor"
		Escribir " "
	FinSi
	
FinProceso