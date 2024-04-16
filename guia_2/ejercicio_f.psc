Proceso Ejercicio_6
	
	Escribir " "
	
	Escribir "Expresion a resolver: 6.57 ^ (x/n) - 3.987 + 8 * (y - 5)"
	
	Escribir " "
	
	Definir x, b, n Como Entero
	
	Escribir "Ingrese un valor para x:"
	Leer x
	
	Escribir "Ingrese un valor para y:"
	Leer b
	
	Escribir "Ingrese un valor para n:"
	Leer n
	
	Si n > 0 Entonces
		ecuacion <- 6.57 ^ (x/n) - 3.987 + 8 * (b - 5)
		Escribir "El resultado de la ecuacion con los numeros ingresados es: ", redon(ecuacion)
		Escribir " "
	SiNo
		Escribir "Ingrese un valor de n mayor a 0, por favor"
		Escribir " "
	FinSi
	
FinProceso