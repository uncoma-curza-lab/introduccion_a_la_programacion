""" Ejercicio 2: Para acceder a una beca del comedor de la universidad, se debe tener un promedio de 
secundario mayor a 7 y menos de 25 años, o en su defecto vivir en una localidad que se encuentre a más de 
30 km de la ciudad de Viedma. Diseñe un algoritmo que permita leer los datos correspondientes de un alumno
e imprima un cartel indicando si puede acceder o no a la beca. """

#Datos: promedio >7 ; edad: <25 ; vivir >30km de VDM 
#Objetivo:  Diseñe un algoritmo que diga si un alumno accede o no a la beca

edad=int(input("Ingrese su edad: "))
promedio=int(input("Ingrese su promedio: "))
ciudad=str(input("¿Vive a más de 30km de Viedma? si/no "))
if (edad < 25 and promedio >= 7) or (ciudad == "si"): 
    print("Podés acceder a la beca del comedor de la universidad")
else:
     print("No podés acceder a la beca del comedor de la universidad")

""" Algoritmo: Solicitar al alumno que ingrese su edad.
Solicitar al alumno que ingrese su promedio de secundario.
Solicitar al alumno que indique si vive a más de 30 km de Viedma.
Verificar las condiciones para acceder a la beca:
Si la edad es menor que 25 y el promedio es mayor o igual a 7 o si vive a más de 30 km de Viedma, entonces el estudiante puede acceder a la beca.
Si se cumplen alguna de estas condiciones, imprimir un mensaje indicando que el estudiante puede acceder a la beca.
En caso contrario, imprimir un mensaje indicando que el estudiante no puede acceder a la beca. """
