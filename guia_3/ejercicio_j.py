""" Ejercicio 10: 
Encuentre el MCD (máximo común divisor) de 48 y 60. """

x = 48
y = 60
mcd = 0

if x > y:
    menor = y
else:
    menor = x

for i in range(1, menor + 1):
    if x % i == 0 and y % i == 0:
        mcd = i
    
print(mcd)