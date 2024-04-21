Proceso Ejercicio_18
	
	Escribir " "
	
	Escribir "Ingrese 1 numero entero (N) y 1 digito (D) y elimine de N todas las apariciones de D"	
	Escribir "---------------------------------------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese un numero entero de mas de 4 digitos: " Sin Saltar
	Leer N
	
	Escribir "Ingrese el digito que desea eliminar: " Sin Saltar
	Leer D
	
	Escribir " "
	
	Si N < 10000 Entonces
		Escribir " "
		Escribir "Error: N debe tener mas de 4 digitos."
		Escribir " "
	SiNo
		Si D < 0 O D > 9 Entonces
			Escribir " "
			Escribir "Error: D debe ser un solo digito."
			Escribir " "
		SiNo
			resultado <- 0
			posicion <- 0
			
			Mientras N > 0 Hacer
				digito <- N MOD 10
				Si digito <> D Entonces
					resultado <- resultado + digito * (10 ^ posicion)
					posicion <- posicion + 1
				FinSi
				N <- trunc(N / 10) 
			FinMientras
			
			Si resultado == 0 Entonces
				Escribir " "
				Escribir "El resultado es: 0"
				Escribir " "
			SiNo
				Escribir " "
				Escribir "El resultado es: ", resultado
				Escribir " "
			FinSi
		FinSi
	FinSi
FinProceso