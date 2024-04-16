Proceso Ejercicio_12
	
	Escribir " "
	
	Escribir "Elaborar programa que pida la edad de una persona y diga si es ni�o, joven o adulto."
	
	Escribir "---------------------------------------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese su edad en a�os"
	
	Definir edad Como Entero
	
	Leer edad
	
	Escribir " "
	
	Si edad <= 15 Entonces
		Escribir "Ni�ez"
		Escribir " "
	SiNo
		Si 15 < edad Y edad <= 35 Entonces
			Escribir "Juventud"
			Escribir " "
		SiNo
			Escribir "Adulto"
			Escribir " "
		FinSi
	Fin Si
	
FinProceso