""""       Los programas que se indican a continuación, en Python, no funcionan, deberá determinar donde está el error y corregirlos. 
Programa numeros.py : el programa implementa la funcion mostrar(), que recibe como parámetros 2 números y muestra el número mayor
def mostrar(a,b):
	if(a>b):
		mayor=a
		menor=b 
	else:
		mayor=b
		menor=a
	mensaje= a," es mayor que ",b

a=input("Introduzca primer numero: ")
b=input("Introduzca segundo numero: ")

mostrar(a,b)
print mensaje

Programa par.py: el programa devuelve True o False para indicar si el número es Par o Impar
def par(num):
	if num % 2 = 0:
		True
	else:
		False
nro=int(input("Ingrese un numero: ")) 
if par(nro)== True:
	else:
	print("Impar")

Corrija los programas numeros.py y par.py. Luego crear un programa principal que permita ingresar dos números,
determine el número mayor y defina si el número mayor es par o impar"""

def mostrar(a,b):
    if(a>b):
        mayor=a
        menor=b 
    else:
        mayor=b
        menor=a
    mensaje= str(mayor) + " es mayor que " + str(menor)
    return mensaje, mayor

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

a=int(input("Introduzca primer numero: "))
b=int(input("Introduzca segundo numero: "))

mensaje, mayor = mostrar(a,b)
print(mensaje)

if par(mayor)== True:
    print("El número mayor es Par")
else:
    print("El número mayor es Impar")
