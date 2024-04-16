Proceso Ejercicio_9
	
	Escribir " "
	
	Definir num Como Entero
	
	Escribir "Ingrese un numero:"
	Leer num
	
	Escribir " "
	
	Escribir "El numero original es: ", num
	
	Escribir " "
	
	Si num MOD 2 == 0 Y num > 10 Entonces
		num <- num - 10
		Escribir "Se resta 10"
	FinSi
	
	Si num MOD 2 <> 0 Y num > 50 Entonces
		num <- num + 12
		Escribir "Se suma 12"
	FinSi
	
	Si num MOD 2 == 0 Y num < 50 Entonces
		num <- num + 20
		Escribir "Se suma 20"
	FinSi
	
	Si num MOD 2 <> 0 Entonces
		num <- num + 1
		Escribir "Se suma 1"
	FinSi
	
	Escribir " "
	
	Escribir "Al final de los cambios el numero ahora es: ", num
	
	Escribir " "
	
FinProceso