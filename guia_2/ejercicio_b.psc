Proceso Ejercicio_2
	
	Escribir "Dado un numero de 5 digitos muestre el numero separado desde la unidad."
	
	Escribir "Ingrese un numero de 5 digitos: "
	
	Leer numero_5
	
	d_1 <- trunc(numero_5 / 10000)
	d_2 <- trunc(numero_5 / 1000) MOD 10
	d_3 <- trunc(numero_5 / 100) MOD 10
	d_4 <- trunc(numero_5 / 10) MOD 10
	d_5 <- numero_5 MOD 10
	
	Escribir "El numero", " ", numero_5 , " ","separado por digitos desde la unidad es: " 
	Escribir d_5,",",d_4,",",d_3,",",d_2,",",d_1

FinProceso