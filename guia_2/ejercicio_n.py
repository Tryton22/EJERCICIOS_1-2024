""" Ejercicio 14:
Tecnofactory, una tienda de artículos de computación e insumos, ha decidido realizar una
venta especial para sus clientes. A cada cliente que entre a la tienda durante la semana, se le
realizarán descuento en base a 2 criterios para la compra de un computador Alienware:
Además de la edad de la persona, se tendrá en cuenta hace cuanto tiempo realizó su última
compra en la tienda. Para todas las personas mayores de 18 años el equipo tendrá un costo de
$1000000 pero para aquellos que hayan comprado hace 1 mes o menos, se les hará un
descuento del 40%; para los que hayan comprado hace 2 meses o menos, el descuento será
del 30%; para 3 meses o menos del 15%; y para los demás no habrá descuento. Para los
jóvenes con los 18 años la libreta tiene un costo de $900000 y, entre ellos, quienes hayan
comprado hace 1 mes o menos, tendrán un descuento del 60%; para 2 meses o menos,
descuento del 40%, para 3 meses o menos, un descuento del 20% y para los demás no habrá
descuento. Hacer un algoritmo que tome la edad y la cantidad de meses pasados desde la
última compra (entero sin decimales) de una persona y nos muestre descuento que le hacen y
su valor final a pagar. """

edad = int(input("\nIndique su edad: "))
mes_compra = int(input("Indique hace cuantos meses exactos hizo su ultima compra: "))

if edad > 18:
    valor_equipo = 1000000
    if mes_compra == 1:
        descuento = 40
        print("\nEl descuento al valor del equipo es del:",descuento,"%")
        valor_descuento = valor_equipo * descuento // 100
        valor_final = valor_equipo - valor_descuento
        print("El valor final a pagar seria de $",valor_final,"\n")
    elif mes_compra == 2:
        descuento_1 = 30
        print("\nEl descuento al valor del equipo es del:",descuento_1,"%")
        valor_descuento_1 = valor_equipo * descuento_1 // 100
        valor_final_1 = valor_equipo - valor_descuento_1
        print("El valor final a pagar seria de $",valor_final_1,"\n")
    elif mes_compra == 3:
        descuento_2 = 15
        print("\nEl descuento al valor del equipo es del:",descuento_2,"%")
        valor_descuento_2 = valor_equipo * descuento_2 // 100
        valor_final_2 = valor_equipo - valor_descuento_2
        print("El valor final a pagar seria de $",valor_final_2,"\n")
    else:
        print("\nEl valor del equipo no sufre ningun descuento.")
        print("El valor final a pagar seria de $",valor_equipo,"\n")

elif edad == 18:
    valor_equipo_1 = 900000
    if mes_compra == 1:
        descuento_3 = 60
        print("\nEl descuento al valor del equipo es del:",descuento_3,"%")
        valor_descuento_3 = valor_equipo_1 * descuento_3 // 100
        valor_final_3 = valor_equipo_1 - valor_descuento_3
        print("El valor final a pagar seria de $",valor_final_3,"\n")
    elif mes_compra == 2:
        descuento_4 = 40
        print("\nEl descuento al valor del equipo es del:",descuento_4,"%")
        valor_descuento_4 = valor_equipo_1 * descuento_4 // 100
        valor_final_4 = valor_equipo_1 - valor_descuento_4
        print("El valor final a pagar seria de $",valor_final_4,"\n")
    elif mes_compra == 3:
        descuento_5 = 20
        print("\nEl descuento al valor del equipo es del:",descuento_5,"%")
        valor_descuento_5 = valor_equipo_1 * descuento_5 // 100
        valor_final_5 = valor_equipo_1 - valor_descuento_5
        print("El valor final a pagar seria de $",valor_final_5,"\n")
    else:
        print("\nEl valor del equipo no sufre ningun descuento.")
        print("El valor final a pagar seria de $",valor_equipo_1,"\n")

else:
    print("\nNo cumple uno de los criterios para obtener su descuento.\n")
    exit()