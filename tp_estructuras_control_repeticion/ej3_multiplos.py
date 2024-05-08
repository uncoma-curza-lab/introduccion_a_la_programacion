"""Leer un número X y una secuencia de números. Mostrar cuál es el porcentaje
de números leídos que fueron múltiplos de X. Utilizar ciclo iterativo.

<u>Ejemplo:</u> X= 8 y la secuencia 12, 23, 24, 56, 11, 16, la salida es: 50"""

print("Ingrese el número X:")
X = int(input())

print("Ingrese una secuencia de números, termine con un número negativo:")

contador = 0
multiplos = 0
num = 0

while num >= 0:
    num = int(input())
    if num >= 0:
        contador += 1
        if num % X == 0:
            multiplos += 1

if contador > 0:
    porcentaje = (multiplos / contador) * 100
    print("El porcentaje de números que son múltiplos de", X, "es:", porcentaje)
else:
    print("No se ingresaron números válidos.")

