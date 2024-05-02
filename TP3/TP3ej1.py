#Ejercicio 1: Ingresar dos números a y b, y indicar si están ordenados en forma creciente.

#objetivo: determinar si dos numeros ingresador están ordenados de forma creciente

""" Algoritmo: solicitar al usuario que ingrese el numero a
    solicitar al usuario que ingrese el numero b
    mostrar en pantalla si están ordenados de forma decreciente o no"""

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
if a<b:
    print("Los numeros están ordenados de forma creciente")
else: 
    print("los numeros no están ordenados de forma creciente")
