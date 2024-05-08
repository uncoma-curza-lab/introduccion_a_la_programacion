"""Ingresar dos números a y b. retornar la suma de los números impares naturales que hay entre ellos.

Este problema se resuelve con ¿ciclo definido o indefinido?

<u>Ejemplo:</u> a=4 y b= 12, el cálculo es 5+7+9+11 y la salida es: 32."""

def suma_impares(a, b):
    suma = 0
    for i in range(a + 1, b):
        if i % 2 != 0:
            suma += i
    return suma

print("Ingrese el número a:")
a = int(input())
print("Ingrese el número b:")
b = int(input())

print("La suma de los números impares entre", a, "y", b, "es:", suma_impares(a, b))
