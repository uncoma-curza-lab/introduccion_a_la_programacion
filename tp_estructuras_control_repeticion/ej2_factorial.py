"""Dado un número N calcular su factorial. Utilizar ciclo definido,
estructura For y variable acumuladora del producto.
<u>Ejemplo:</u> 4! =4\*3\*2\*1 = 24"""

N = int(input("Ingresa el número que desees: "))  # Pide el número por pantalla
factorial = 1

for i in range(1, N + 1):
    factorial *= i

print(f"El factorial de {N} es: {factorial}")

