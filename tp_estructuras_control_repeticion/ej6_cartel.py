"""Escriba un procedimiento/función CartelMayor que muestre por pantalla la frase
“es un número mayor que cincuenta” y un procedimiento CartelMenor que muestre por pantalla la frase
“ es un número menor que cincuenta”.

Utilizando los procedimientos anteriores ingrese distintos números enteros por teclado
hasta ingresar el número (-1) que actuaría de corte. Luego muestre por pantalla los carteles adecuados.

Halle e imprima la suma de todos los números menores de cincuenta."""

def CartelMayor():
    print("es un número mayor que cincuenta")

def CartelMenor():
    print("es un número menor que cincuenta")

suma = 0
numero = int(input("Ingrese un número entero (-1 para terminar): "))

while numero != -1:
    if numero > 50:
        CartelMayor()
    else:
        CartelMenor()
        suma += numero
    numero = int(input("Ingrese un número entero (-1 para terminar): "))

print("La suma de todos los números menores de cincuenta es", suma)
