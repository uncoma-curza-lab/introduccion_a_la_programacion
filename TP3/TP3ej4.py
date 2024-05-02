"""Ejercicio 4: Una empresa lleva el control de la productividad de un mes dado de acuerdo a lo siguiente:
1 Enero, febrero y marzo tienen factor 15
2 Abril, mayo y junio factor 17
3 Julio y Agosto factor 19
4 Septiembre, Octubre y Noviembre y Diciembre factor 20
Elaborar un programa que calcule la productividad de un mes dado, conociendo que la productividad es igual 
al número de artículos producidos en el mes, multiplicado por el factor que le corresponde al mes 
proporcionado.
"""

#Objetivo: Elaborar un programa que calcule la productividad de un mes dado
#Datos: (resumiendo) factor por mes; la formula de productividad

mes = input("Ingrese el mes: " ).lower()
articulos = int(input("Ingrese el número de artículos producidos en el mes: "))

if mes == "enero" or mes == "febrero" or mes == "marzo":
    factor = 15
elif mes == "abril" or mes == "mayo" or mes == "junio":
    factor = 17
elif mes == "julio" or mes == "agosto":
    factor = 19
elif mes == "septiembre" or mes == "octubre" or mes == "noviembre" or mes == "diciembre":
    factor = 20
else:
    print("Mes inválido")


productividad = articulos * factor
print("La productividad del mes es: ", productividad)

"""Algoritmo: Solicitar al usuario que ingrese el mes
Solicitar al usuario que ingrese el número de artículos producidos en el mes.
Verificar el mes ingresado y asignar el factor 
Calcular la productividad multiplicando el número de artículos producidos por el factor del mes.
mostrar en pantalla la productividad del mes"""
