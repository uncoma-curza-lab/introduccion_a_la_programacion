"""Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de
tuplas con la siguiente forma: (nombre, dni, destino)
Ejemplo:
[("Diego Martinez”, 19753951, "Bariloche”),
("Silvana Dietz”, 23956124, "El Bolson”),
("Sergio Gutierrez”, 21789142, "San Martin de los Andes”),
("Claudia Ortiz”, 18553951, "Bariloche”),
("Ana Rodriguez”, 17635874, "Villa Pehuenia”),]
Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que
pertenecen.
Ejemplo:
[("Bariloche, Rio Negro”),
(" El Bolson, Rio Negro”),
(" San Martin de los Andes, Neuquen”),
("Villa Pehuenia, Neuquen”)]
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
i.
 Agregar pasajeros a la lista de viajeros.
ii.
 Agregar ciudades a la lista de ciudades.
iii.
 Dado el DNI de un pasajero, ver a qué ciudad viaja
iv.
 Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad
v.
 Dado el DNI de un pasajero, ver a qué provincia viaja.
vi.
 Dado una provincia, mostrar cuántos pasajeros viajan a esa provincia
vii.
 Salir del programa"""

def pasajero_provincia():
    dni = int(input("Ingrese el DNI del pasajero: "))
    encontrado = False
    for pasajero in pasajeros:
        if pasajero[1] == dni:
            encontrado = True
            for ciudad in ciudades:
                if pasajero[2] == ciudad[0]:
                    print(f"El pasajero {pasajero[0]} viaja a la provincia de: {ciudad[1]}")
    if not encontrado:
        print("No encontré el pasajero")      

pasajeros = [("Diego Martinez", 19753951, "Bariloche"),
             ("Silvana Dietz", 23956124, "El Bolson"),
             ("Sergio Gutierrez", 21789142, "San Martin de los Andes"),
             ("Claudia Ortiz", 18553951, "Bariloche"),
             ("Ana Rodriguez", 17635874, "Villa Pehuenia")]

ciudades = [("Bariloche", "Rio Negro"),
            ("El Bolson", "Rio Negro"),
            ("San Martin de los Andes", "Neuquen"),
            ("Villa Pehuenia", "Neuquen")]

while True:
    print("0. Imprimir listas")
    print("1. Agregar pasajeros a la lista de viajeros")
    print("2. Agregar ciudades a la lista de ciudades")
    print("3. Dado el DNI de un pasajero, ver a qué ciudad viaja")
    print("4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad")
    print("5. Dado el DNI de un pasajero, ver a qué provincia viaja")
    print("6. Dado una provincia, mostrar cuántos pasajeros viajan a esa provincia")
    print("7. Salir del programa")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 0:
        print("Pasajeros: ", pasajeros)
        print("Ciudades: ", ciudades)
    elif opcion == 1:
        nombre = input("Ingrese el nombre del pasajero: ")
        dni = int(input("Ingrese el DNI del pasajero: "))
        destino = input("Ingrese el destino del pasajero: ")
        pasajeros.append((nombre, dni, destino))
    elif opcion == 2:
        ciudad = input("Ingrese el nombre de la ciudad: ")
        provincia = input("Ingrese la provincia de la ciudad: ")
        ciudades.append((ciudad, provincia))
    elif opcion == 3:
        dni = int(input("Ingrese el DNI del pasajero: "))
        for pasajero in pasajeros:
            if pasajero[1] == dni:
                print(f"El pasajero {pasajero[0]} viaja a {pasajero[2]}")
    elif opcion == 4:
        ciudad = input("Ingrese el nombre de la ciudad: ")
        cantidad = 0
        for pasajero in pasajeros:
            if pasajero[2] == ciudad:
                cantidad += 1
        print(f"La ciudad {ciudad} tiene {cantidad} pasajeros")
    elif opcion == 5:
        pasajero_provincia()
    elif opcion == 6:
        provincia = input("Ingrese el nombre de la provincia: ")
        #Dado una provincia, mostrar cuántos pasajeros viajan a esa provincia
        cantidad = 0
        for pasajero in pasajeros:
            for ciudad in ciudades:
                if pasajero[2] == ciudad[0]:
                    if ciudad[1] == provincia:
                        cantidad += 1
        print(f"La provincia {provincia} tiene {cantidad} pasajeros")
    elif opcion == 7:
        break
    else:
        print("Opción no válida")
