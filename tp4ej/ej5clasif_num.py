"""Escriba un programa que solicite al usuario un número entero y lo clasifique como positivo,
negativo o cero. Utiliza una función para realizar la clasificación del número, mostrar un
mensaje en el programa principal. Por ejemplo para el número 25 el mensaje sería:
“El número 25 es positivo”"""

def clasificar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

def mostrar_mensaje(n):
    clasificacion = clasificar_numero(n)
    print(f"El número {n} es {clasificacion}")

numero = int(input("Ingrese un número entero: "))
mostrar_mensaje(numero)
