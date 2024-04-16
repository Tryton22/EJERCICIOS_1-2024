Proceso Ejercicio_11
	Escribir " "
	
	Escribir "Usar Switch-Case para crear un programa." 
	
	Escribir " "
	
	Escribir "Ingrese un numero del 1 al 4: "
	
	Definir numero_opcion Como Entero
	
	Leer numero_opcion
	
	Escribir " "
	
	Segun numero_opcion Hacer
		1:
			Escribir "El numero es uno"
			Escribir " "
			
		2:
			Escribir "Ingrese un numero nuevo"
			Leer numero_nuevo
			Escribir " "
			Si numero_nuevo > 0 Y numero_nuevo <= 9 Entonces
				numero_nuevo <- numero_nuevo + 10
				Escribir "El numero es:"," ",numero_nuevo," "
				Escribir " "
			SiNo
				Escribir "Ingrese un numero entre 1 y 9"
				Escribir " "
			Fin Si
			
		3:
			Escribir "Ingrese un numero nuevo"
			Leer numero_nuevo
			Escribir " "
			Si numero_nuevo > 0 Y numero_nuevo <= 9 Entonces
				numero_nuevo <- numero_nuevo - 10
				Escribir "El numero es:"," ",numero_nuevo," ","y es negativo"
				Escribir " "
			SiNo
				Escribir "Ingrese un numero entre 1 y 9"
				Escribir " "
			Fin Si			
			
		4:
			nuevo <- AZAR(10)
			Escribir "El numero elegido es:"," ",nuevo
			Escribir " "
			
		De Otro Modo:
			Escribir "Ha ingresado un numero ilegal, ingrese uno entre 1 y 4"
			Escribir " "
	Fin Segun
	
FinProceso