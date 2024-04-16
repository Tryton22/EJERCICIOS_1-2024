Proceso Ejercicio_13
	
	Escribir " "
	
	Definir peso_ropa Como Entero
	
	Escribir "Ingrese los kilos de ropa que desea lavar:"
	
	Leer peso_ropa
	
	Escribir " "
	
	Si peso_ropa >= 30 Entonces
		Escribir "La lavadora tiene mucho peso, no funciona"
		Escribir " "
	SiNo
		Si peso_ropa >= 22 Entonces
			Escribir "Nivel de carga: Maximo"
			Escribir " "
		SiNo
			Si peso_ropa >= 15 Entonces
				Escribir "Nivel de carga: Alta"
				Escribir " "
			SiNo
				Si peso_ropa >= 8 Entonces
					Escribir "Nivel de carga: Medio"
					Escribir " "
				SiNo
					Si 0 < peso_ropa Y peso_ropa < 8 Entonces
						Escribir "Nivel de carga: Minimo"
						Escribir " "
					SiNo
						Escribir "Ingrese un numero mayor a 1, por favor"
						Escribir " "
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi

FinProceso