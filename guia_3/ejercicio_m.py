""" Ejercicio 13: 
Un  supermercado  descuenta  un  15%  al  total  de  la  compra  por  compras  superiores  a  10 
artículos  o  cuyo  total  sea  superior  a  $20000,  realice  un  programa  en  python  que  solicite 
los  precios  de  los  productos  hasta  que  el  usuario  ingrese  un  0,  y  determine  si  se  hace 
efectivo el descuento. """

descuento = 15
precio = 1
contador = 0
suma = 0

while precio > 0:
    precio = int(input("\nIngrese el valor del producto que va a llevar:$ "))
    contador += 1
    suma += precio
    

if suma > 20000 or contador > 10:
    print("\nEl descuento se ha realizado a su compra"
          " su precio final es de:$", suma * descuento // 100,"\n")
else:
    print("\nEl descuento no se ha realizado a su compra"
          " su precio final es de:$", suma,"\n")