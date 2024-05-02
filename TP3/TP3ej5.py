"""Ejercicio 5: Escribe un programa que responda a un usuario que quiere comprar un helado, cuanto le costará
en función del topping que elija. El helado sin topping cuesta $ 120.; el topping de oreo cuesta $30.; el 
topping de KitKat cuesta $40; el topping de brownie cuesta $25.; el topping de M&M cuesta $35. En caso de 
elegir un topping que no está en la lista, el programa escribirá por pantalla «no tenemos este topping, lo 
sentimos. » y a continuación informar del precio del helado sin ningún topping. Finalmente, el programa 
escribe por pantalla el precio del helado con el topping seleccionado (o ninguno)."""

#Objetivo: Hacer un programa que muestre cuanto costará un helado de acuerdo al topping elegido
#DATOS: (resumiendo) valor del helado, valor del topping, mensaje en caso de no seleccionar un topping correccto

topping = input("Elija un topping para su helado (oreo, kitkat, brownie, m&m): ").lower()
precio_helado = 120

if topping == "oreo":
    precio_con_topping = precio_helado + 30
elif topping == "kitkat":
    precio_con_topping = precio_helado + 40
elif topping == "brownie":
    precio_con_topping = precio_helado + 25
elif topping == "m&m":
    precio_con_topping= precio_helado + 35
else:
   print("No tenemos ese Topping, lo sentimos")
    
print("El precio del helado con topping", topping, "es de:", precio_con_topping)

"""Algoritmo: Solicitar al usuario que elija un topping de los disponibles.
Definir el precio base del helado sin topping como $120.
Verificar el topping seleccionado utilizando condiciones if, elif y else y asignarle un el valor correspondiente a cada topping.
Sumar el valor del helado + el valor del topping
Mostrar en pantalla el precio del helado con el topping o si no tenemos ese topping """
