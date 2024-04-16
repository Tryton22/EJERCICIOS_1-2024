Proceso Ejercicio_3
	
	Escribir " "
	
	Definir numero_digit, d_1, d_2, d_3, d_4, d_5 Como Entero
	
	Escribir "Ingrese un numero con 5 digitos: "
	Leer numero_digit
	
	Escribir " "
	
	d_1 <- trunc(numero_digit / 10000)
	d_2 <- trunc(numero_digit / 1000) MOD 10
	d_3 <- trunc(numero_digit / 100) MOD 10
	d_4 <- trunc(numero_digit / 10) MOD 10
	d_5 <- numero_digit MOD 10
	
	Escribir "El numero ingresado es: ", numero_digit
	Escribir "El numero separado por digitos es: ", d_1,",",d_2,",",d_3,",",d_4,",",d_5
	Escribir " "
	
FinProceso