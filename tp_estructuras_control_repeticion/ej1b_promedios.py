"""Modifique el programa anterior para que muestre el promedio de los pares y el promedio de los impares."""

suma_pares = 0
suma_impares = 0
cont_pares = 0
cont_impares = 0

for i in range(1, 11):
    if i % 2 == 0:
        suma_pares += i
        cont_pares += 1
    else:
        suma_impares += i
        cont_impares += 1

promedio_pares = suma_pares / cont_pares
promedio_impares = suma_impares / cont_impares

print("El promedio de los primeros 10 números pares es:", promedio_pares)
print("El promedio de los primeros 10 números impares es:", promedio_impares)
