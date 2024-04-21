Proceso Ejercicio_20
	
	Escribir " "
	
	Escribir "Crear un contorno de rectangulo con numeros pares mayores a 4"
	Escribir "---------------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese el ancho del rectangulo (debe ser un numero par mayor a 4)"
	Leer ancho
	
	Escribir "Ingrese el alto del rectangulo (debe ser un numero par mayor a 4)"
	Leer alto
	
	Si ancho MOD 2 <> 0 O alto MOD 2 <> 0 O ancho <= 4 O alto <= 4 Entonces
		Escribir " "
		Escribir "Error: El ancho y el alto deben ser numeros pares mayores a 4"
		Escribir " "
	SiNo
		Escribir " "
		Escribir "El contorno resultante queda asi: "
		Escribir " "
		Para i <- 1 Hasta alto Con Paso 1 Hacer
			Para k <- 1 Hasta ancho Con Paso 1 Hacer
				Si i == 1 Entonces
					Escribir "*" Sin Saltar
				SiNo
					Si i == alto Entonces
						Escribir "*" Sin Saltar
					SiNo
						Si k == 1 Entonces
							Escribir "*" Sin Saltar
						SiNo
							Si k == ancho Entonces
								Escribir "*" Sin Saltar
							SiNo
								Escribir " " Sin Saltar
							FinSi
						FinSi
					FinSi
				FinSi
			FinPara
			Escribir " "
		Fin Para
	FinSi
FinProceso