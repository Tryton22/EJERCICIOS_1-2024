Proceso Ejercicio_10
	
	Escribir " "
	
	Definir d_1, d_2, d_3, d_4, d_5, d_6 Como Entero
	
	Escribir "Ingrese un numero de 6 digitos: "
	Leer digitos 
	
	Escribir " "
	
	Si (digitos > 99999 Y digitos < 1000000) O (digitos < -99999 Y digitos > -1000000) Entonces
		d_1 <- trunc(digitos / 100000)
		d_2 <- trunc(digitos / 10000) MOD 10
		d_3 <- trunc(digitos / 1000) MOD 10
		d_4 <- trunc(digitos / 100) MOD 10
		d_5 <- trunc(digitos / 10) MOD 10
		d_6 <- digitos % 10
		
		Escribir "El digito 1 es: ", d_1
		Escribir "El digito 2 es: ", d_2
		Escribir "El digito 3 es: ", d_3
		Escribir "El digito 4 es: ", d_4
		Escribir "El digito 5 es: ", d_5
		Escribir "El digito 6 es: ", d_6
		
		Escribir " "
		
		Si d_6 MOD 2 == 0 Entonces
			Escribir "El digito 6 del numero ingresado es par."
			Escribir " "
		SiNo
			Si d_6 == 3 O d_6 == 5 O d_6 == 7 Entonces
				Escribir "El digito 6 del numero ingresado es primo."
				Escribir " "
			SiNo
				Escribir "El digito 6 del numero ingresado es natural."
				Escribir " "
			FinSi
		FinSi
	SiNo
		Escribir "Ingrese un numero con 6 digitos, por favor."
		Escribir " "
	FinSi
	
FinProceso