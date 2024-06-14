"""a. Solicitar al usuario que ingrese números, los cuales se guardaran en una lista.
Finalizar al ingresar el número 0, el cual no debe guardarse.
b. Solicitar al usuario que ingrese un número y, si el numero ingresado está en la lista,
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
c. Imprimir la sumatoria de todos los números de la lista
d. Solicitar al usuario que ingrese otro número y crear una lista con los elementos de la
lista original que sean menores que el número ingresado. Imprimir esta nueva lista,
iterando por ella.
e. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una
compuesta por un número de la lista original y la cantidad de veces que aparece en
ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá
[(5,3),(16,1),(2,2),(57,1)]"""

# a. Solicitar al usuario que ingrese números, los cuales se guardaran en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
lista = []
while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    lista.append(num)
print(lista)

# b. Solicitar al usuario que ingrese un número y, si el numero ingresado está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
num = int(input("Ingrese un número a borrar de la lista: "))
if num not in lista:
    print("No se encuentra en la lista")
else:
    i = 0
    while i < len(lista):
        if lista[i] == num:
            lista.pop(i)
            continue
        i += 1
print(lista)

# c. Imprimir la sumatoria de todos los números de la lista
print("La suma de los números de la lista es: ", sum(lista))

# d. Solicitar al usuario que ingrese otro número y crear una lista con los elementos de la lista original que sean menores que el número ingresado. Imprimir esta nueva lista, iterando por ella.
num = int(input("Ingrese un número, voy a borrar todos los mayores o iguales a ese: "))
lista_menores = []
for num_lista in lista:
    if num_lista < num:
        lista_menores.append(num_lista)
print("La lista con números menores a: ", num, " es ", lista_menores)

# e. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá [(5,3),(16,1),(2,2),(57,1)]
lista_tuplas = []
unicos = set(lista)
print("Los números únicos de la lista son: ", unicos)
for num_lista in unicos:
    tupla = (num_lista, lista.count(num_lista))
    lista_tuplas.append(tupla) 
print("La lista con tuplas es: ", lista_tuplas)