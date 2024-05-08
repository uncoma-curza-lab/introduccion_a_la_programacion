"""Desarrollar una función que indique si un determinado entero es un número primo.
Desde el programa principal: ingrese 25 números enteros e imprima un mensaje indicando
si es o no primo (llamando a la función) y el promedio de todos los números ingresados."""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

suma = 0
for i in range(25):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
    if es_primo(numero):
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")

promedio = suma / 25
print("El promedio de todos los números ingresados es", promedio)
