Proceso Ejercicio_2
	
	Escribir " "
	
	Escribir "Ingresar un rango de numero para buscar impares."
	Escribir "--------------------------------------------------"
	
	Escribir " "
	
	Definir num_inicio, num_final Como Entero
	
	Escribir "Ingrese un numero inicial: "
	Leer num_inicio
	
	Escribir "Ingrese un numero final: "
	Leer num_final
	
	Escribir " "
	
	n <- 1
	
	Si num_final > num_inicio Entonces
		Para i <- num_inicio Hasta num_final Con Paso 1 Hacer
			Si i MOD 2 <> 0 	Entonces
				Escribir "Numero impar: ", n,": ", i
				Escribir " "
				n <- n + 1
			FinSi
		Fin Para
	SiNo
		Escribir "Ingrese los valores correctamente, por favor"
		Escribir " "
	FinSi
FinProceso