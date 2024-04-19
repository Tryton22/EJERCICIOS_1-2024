Proceso Ejercicio_13
	
	Escribir " "
	
	Escribir "Solicitar precios de productos hasta que se ingrese un 0 y determinar descuentos"
	Escribir "---------------------------------------------------------------------------------"
	
	Escribir " "
	
	descuento <- 15
	precio <- 1
	contador <- 0
	suma <- 0
	
	Mientras precio > 0 Hacer
		Escribir "Ingrese el valor del producto que va a llevar: "
		Leer precio
		Escribir " "
		contador <- contador + 1
		suma <- suma + precio
	Fin Mientras
	
	Si suma > 20000 O contador > 10 Entonces
		Escribir " "
		Escribir "El descuento ha sido realizado a su carrito de compra"
		Escribir "El precio final a pagar es de: $", trunc(suma * descuento / 100)
		Escribir " "
	SiNo
		Escribir " "
		Escribir "El descuento no ha sido realizado a su carrito de compra"
		Escribir "El precio final a pagar es de: $", suma
		Escribir " "
	Fin Si
	
FinProceso