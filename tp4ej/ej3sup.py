"""       Escriba un programa que permita calcular la superficie de una forma simple (rectángulo, círculo, triángulo y rombo). El mismo debe contener un menú que pregunte que forma se va a elegir y luego pide la entrada correspondiente para cada fórmula. Por ejemplo:
1) Rectángulo
2) Círculo
3) Triángulo
4) Rombo
Si se ingresa 2, debería pedir el radio de un círculo y debería imprimir un mensaje: “La superficie de un círculo de radio 4 es 50,24”
Usted debe diseñar una función para resolver cada forma del menú."""

import math

def calcular_superficie_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    return largo * ancho

def calcular_superficie_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    return math.pi * (radio ** 2)

def calcular_superficie_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return (base * altura) / 2

def calcular_superficie_rombo():
    D = float(input("Ingrese la diagonal mayor del rombo: "))
    d = float(input("Ingrese la diagonal menor del rombo: "))
    return (D * d) / 2

def main():
    print("Seleccione la forma:")
    print("1) Rectángulo")
    print("2) Círculo")
    print("3) Triángulo")
    print("4) Rombo")
    
    opcion = int(input("Ingrese la opción: "))
    
    if opcion == 1:
        superficie = calcular_superficie_rectangulo()
        print(f"La superficie del rectángulo es {superficie}")
    elif opcion == 2:
        superficie = calcular_superficie_circulo()
        print(f"La superficie del círculo es {round(superficie, 2)}")
    elif opcion == 3:
        superficie = calcular_superficie_triangulo()
        print(f"La superficie del triángulo es {superficie}")
    elif opcion == 4:
        superficie = calcular_superficie_rombo()
        print(f"La superficie del rombo es {superficie}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
