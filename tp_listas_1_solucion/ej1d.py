# Encuentre el elemento “root” de la lista y contar cuantos hay?

conexiones = ["127.0.0.1", "root", "123456", "nomina", "root"]

contador_root = 0
for i, elemento in enumerate(conexiones):
  if elemento == "root":
    contador_root += 1
    print(f"Índice: {i}, Elemento: 'root'")

print(f"Cantidad total de elementos 'root': {contador_root}")
