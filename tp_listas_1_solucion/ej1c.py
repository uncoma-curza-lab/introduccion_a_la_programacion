# cree otra lista con los elementos en orden inverso (desde el último al 1ero)

conexiones = ["127.0.0.1", "root", "123456", "nomina"]

# Obtener la longitud de la lista
longitud = len(conexiones)

# Recorrer la lista en orden inverso (detrás hacia adelante)
for i in range(longitud-1, -1, -1):
  elemento = conexiones[i]
  print(elemento)

"""conexiones_inversa = conexiones.copy()  # Crea una copia de la lista
conexiones_inversa.sort(reverse=True)  # Ordena la copia en orden descendente

# Imprimir la lista inversa
print(conexiones_inversa)
"""