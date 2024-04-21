Proceso Ejercicio_9
	
	Escribir " "
	
	Escribir "Resolver multiplicaciones de 2 numeros positivos mediante sumas de factores."
	Escribir "-----------------------------------------------------------------------------"
	
	Escribir " "
	
	Escribir "Ingrese un factor positivo para la multiplicacion: "
	Leer numero_1
	
	Escribir "Ingrese otro factor positivo para la multiplicacion: "
	Leer numero_2
	
	Escribir " "
	
	suma <- 0
	suma_1 <- 0
	
	Si numero_1 > 0 Y numero_2 > 0 Entonces
		Para i <- 1 Hasta numero_2 Con Paso 1 Hacer
			suma <- suma + numero_1
		Fin Para
		Escribir "El resultado sumando el primer numero es: ", suma
		Escribir " "
		
		Para i <- 1 Hasta numero_1 Con Paso 1 Hacer
			suma_1 <- suma_1 + numero_2
		FinPara
		Escribir "El resultado sumando el segundo numero es: ", suma_1
		Escribir " "
	SiNo
		Escribir "Ingrese solo numeros positivos, por favor"
		Escribir " "
	FinSi
FinProceso