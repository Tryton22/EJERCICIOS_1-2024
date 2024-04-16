Proceso Ejercicio_14
	
	Escribir " "
	
	Definir edad Como Entero
	Definir mes_compra Como Entero
	
	Escribir "Indique su edad:"
	Leer edad
	
	Escribir " "
	
	Escribir "Indique hace cuantos meses exactos hizo su ultima compra (aproxime):"
	Leer mes_compra
	
	Escribir " "
	
	Si edad > 18 Entonces
		valor_equipo <- 1000000
		Si mes_compra == 1 Entonces
			descuento <- 40
			Escribir "El descuento del equipo es del: ", descuento,"%"
			valor_descuento <- trunc(valor_equipo * descuento / 100)
			valor_final <- valor_equipo - valor_descuento
			Escribir "El valor a pagar seria de $ ", valor_final
			Escribir " "
		SiNo
			Si mes_compra == 2 Entonces
				descuento_1 <- 30
				Escribir "El descuento del equipo es del: ", descuento_1,"%"
				valor_descuento_1 <- trunc(valor_equipo * descuento_1 / 100)
				valor_final_1 <- valor_equipo - valor_descuento_1
				Escribir "El valor a pagar seria de $ ", valor_final_1
				Escribir " "
			SiNo
				Si mes_compra == 3 Entonces
					descuento_2 <- 15
					Escribir "El descuento del equipo es del: ", descuento_2,"%"
					valor_descuento_2 <- trunc(valor_equipo * descuento_2 / 100)
					valor_final_2 <- valor_equipo - valor_descuento_2
					Escribir "El valor a pagar seria de $ ", valor_final_2
					Escribir " "
				SiNo
					Escribir "Usted no aplica para ningun descuento."
					Escribir "El valor a pagar seria de $ ", valor_equipo
					Escribir " "
				FinSi
			FinSi
		FinSi
	SiNo
		Si edad == 18 Entonces
			valor_equipo_1 <- 900000
			Si mes_compra == 1 Entonces
				descuento_3 <- 60
				Escribir "El descuento del equipo es del: ", descuento_3,"%"
				valor_descuento_3 <- trunc(valor_equipo_1 * descuento_3 / 100)
				valor_final_3 <- valor_equipo_1 - valor_descuento_3
				Escribir "El valor a pagar seria de $ ", valor_final_3
				Escribir " "
			SiNo
				Si mes_compra == 2 Entonces
					descuento_4 <- 30
					Escribir "El descuento del equipo es del: ", descuento_4,"%"
					valor_descuento_4 <- trunc(valor_equipo_1 * descuento_4 / 100)
					valor_final_4 <- valor_equipo_1 - valor_descuento_4
					Escribir "El valor a pagar seria de $ ", valor_final_4
					Escribir " "
				SiNo
					Si mes_compra == 3 Entonces
						descuento_5 <- 20
						Escribir "El descuento del equipo es del: ", descuento_5,"%"
						valor_descuento_5 <- trunc(valor_equipo_1 * descuento_5 / 100)
						valor_final_5 <- valor_equipo_1 - valor_descuento_5
						Escribir "El valor a pagar seria de $ ", valor_final_5
						Escribir " "
					SiNo
						Escribir "Usted no aplica para ningun descuento."
						Escribir "El valor a pagar seria de $ ", valor_equipo_1
						Escribir " "
					FinSi
				FinSi
			FinSi
		FinSi
	Fin Si
	
	Si edad < 18 Entonces
		Escribir "No cumple con la edad necesaria para adquirir un descuento"
		Escribir " "
	FinSi	
	
FinProceso