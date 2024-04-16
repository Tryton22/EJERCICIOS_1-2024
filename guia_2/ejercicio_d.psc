Proceso Ejercicio_4
	
	Escribir " "
	
	Definir digitos_5, d_1, d_2, d_3, d_4, d_5 Como Entero
	
	Escribir "Ingrese un numero de 5 digitos: "
	Leer digitos_5
	
	Escribir " "
	
	d_1 <- trunc(digitos_5 / 10000)
	d_2 <- trunc(digitos_5 / 1000) MOD 10
	d_3 <- trunc(digitos_5 / 100) MOD 10
	d_4 <- trunc(digitos_5 / 10) MOD 10
	d_5 <- digitos_5 MOD 10
	
	Escribir "El numero: ", digitos_5
	Escribir "El numero invertido: ", d_5, d_4, d_3, d_2, d_1
	Escribir " "
	
FinProceso