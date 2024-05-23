'''Venta de Pasajes'''
'''Tenemos que armar un software para calcular el precio de un pasaje
dado la distancia, el precio por kilometro.
'''

def confPrecio(precioActual):
    print("El precio actual configurado es: $",precioActual)
    precioNuevo = int(input("Ingrese nuevo valor por kilometro: "))
    return precioNuevo

def imprimirDestinos(dest):
    indice=0
    for destino in dest:
        print(indice,"-",destino)
        indice = indice+1

def calcPrecio(dest,dist,precioActual):
    imprimirDestinos(dest)
    iDestino = int(input("Seleccione un Destino usando el indice: ")) 
    precioPasaje = dist[iDestino]*precioActual
    print("Un pasaje a",dest[iDestino],"cuesta $",precioPasaje)

def agregarDestino(dest,dist):
    nombreDestinoNuevo = input("Ingresar nombre nuevo Destino: ")
    distanciaDestinoNuevo = int(input("Ingresar Distancia a "+nombreDestinoNuevo+" :"))
    dest.append(nombreDestinoNuevo)
    dist.append(distanciaDestinoNuevo)
    return dest,dist

destinos = ["San Antonio","General Roca","Bariloche","Valcheta","Jacobacci"]
distancias =[175,600,800,250,500]
precio = 100

print("Bienvenidos a la calculadora de precios de pasajes")
print("Opciones:")
print("a - Mostrar Precio Actual Configurado")
print("b - Configurar precio por kilometro")
print("c - Calcular Precio a un Destino")
print("d - Agregar un Destino")
print("x - Salir")
while True:

    opcion = input("Ingrese la opcion deseada: ")

    if opcion == "a":
        print("El precio actual configurado es: $",precio)
    elif opcion == "b": 
        precio = confPrecio(precio)
    elif opcion == "c":
        calcPrecio(destinos,distancias,precio)
    elif opcion == "d":
        destinos, distancias = agregarDestino(destinos,distancias)
    elif opcion == "x":
        print("Muchas Gracias!!")
        break
    else:
        print("Opcion Incorrecta")



