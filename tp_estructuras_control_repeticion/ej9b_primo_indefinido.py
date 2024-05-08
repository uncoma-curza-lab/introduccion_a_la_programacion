"""Desarrolle el punto a utilizando ciclo INDEFINIDO. Utilizando los procedimientos anteriores
ingrese distintos números enteros por teclado hasta ingresar el número (0) que actuaría de corte."""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

suma = 0
contador = 0
while True:
    num = int(input("Ingrese un número entero (0 para terminar): "))
    if num == 0:
        break
    suma += num
    contador += 1
    if es_primo(num):
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")
if contador > 0:
    print(f"El promedio de los números ingresados es {suma / contador}.")
