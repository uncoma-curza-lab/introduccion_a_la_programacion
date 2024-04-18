"""Dados dos números X e Y, diseñe un algoritmo que calcule qué porcentaje es X de Y.
Mostrar el resultado por pantalla.
Ejemplo 1: si X=10 e Y=100 entonces X es el 10% de Y.
Ejemplo 2: si X=120 e Y=100 entonces X es el 120% de Y.11)"""

# Solicita los números X e Y al usuario
X = float(input("Por favor, introduce el número X: "))
Y = float(input("Por favor, introduce el número Y: "))

# Calcula el porcentaje de X con respecto a Y
porcentaje = (X / Y) * 100

# Muestra el resultado
print(f"X es el {porcentaje}% de Y.")

