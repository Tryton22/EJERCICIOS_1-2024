Proceso Ejercicio_5
	
	Escribir " "
	
	Definir num_verificado, d_1, d_2, d_3, d_4, d_5 Como Entero
	
	Escribir "Ingrese un numero de 5 digitos: "
	Leer num_verificado
	
	Escribir " "
	
	d_1 <- trunc(num_verificado / 10000)
	d_2 <- trunc(num_verificado / 1000) MOD 10
	d_3 <- trunc(num_verificado / 100) MOD 10
	d_4 <- trunc(num_verificado / 10) MOD 10
	d_5 <- num_verificado MOD 10
	
	
	Si (num_verificado > 9999 Y num_verificado < 100000) O (num_verificado < -9999 Y num_verificado > -100000) Entonces
		Escribir "El numero ingresado es: ", num_verificado
		Escribir "El numero invertido es: ", d_5,d_4,d_3,d_2,d_1
		Escribir " "
	SiNo
		Escribir "Ingrese un valor de 5 digitos, por favor."
		Escribir " "
	FinSi

FinProceso