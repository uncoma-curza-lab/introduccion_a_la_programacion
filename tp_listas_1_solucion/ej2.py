# a) Lista de nombres de usuarios (reemplácela con los nombres reales)
nombres_usuarios = ["usuario1", "usuario2", "usuario3", "usuario4"]

# Funciones para gestionar usuarios

def mostrar_usuarios(nombres_usuarios):
  """ b)Función para mostrar todos los nombres de usuarios."""
  for nombre in nombres_usuarios:
    print(nombre)

def crear_listas_auxiliares(nombres_usuarios):
  """ c) Función para crear listas auxiliares con diferentes ordenaciones."""
  nombres_usuarios_ordenados = sorted(nombres_usuarios)
  nombres_usuarios_invertidos = list(reversed(nombres_usuarios))
  dos_ultimos = nombres_usuarios[-2:]
  dos_primeros = nombres_usuarios[:2]
  return nombres_usuarios_ordenados, nombres_usuarios_invertidos, dos_ultimos, dos_primeros

def agregar_usuario(nombres_usuarios):
  """ d y e) Función para agregar un usuario a la lista."""
  nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ")
  nombres_usuarios.append(nuevo_usuario)
  print(f"Usuario agregado: {nuevo_usuario}")

def buscar_usuario(nombres_usuarios, usuario_buscado):
  """ f) Función para buscar un usuario en la lista."""
  if usuario_buscado in nombres_usuarios:
    print(f"El usuario '{usuario_buscado}' se encuentra en la lista.")
  else:
    print(f"El usuario '{usuario_buscado}' no se encuentra en la lista.")


""""def buscar_usuario(nombres_usuarios, usuario_buscado):
  # Función para buscar un usuario en la lista y mostrar el índice de aparición.
  indices_encontrados = []  # Lista para almacenar los índices de aparición
  encontrado = False

  for i, nombre in enumerate(nombres_usuarios):
    if nombre == usuario_buscado:
      indices_encontrados.append(i)
      encontrado = True

  if encontrado:
    print(f"El usuario '{usuario_buscado}' se encuentra en la lista en los siguientes índices:")
    for indice in indices_encontrados:
      print(f"- Índice: {indice}")
  else:
    print(f"El usuario '{usuario_buscado}' no se encuentra en la lista.")"""

# Menú principal

def menu_principal():
  """Función para mostrar el menú principal y gestionar las opciones."""
  while True:
    print("\nMenú de gestión de usuarios:")
    print("1. Mostrar usuarios")
    print("2. Crear listas auxiliares")
    print("3. Agregar usuario")
    print("4. Buscar usuario")
    print("5. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
      mostrar_usuarios(nombres_usuarios)
    elif opcion == "2":
      nombres_usuarios_ordenados, nombres_usuarios_invertidos, dos_ultimos, dos_primeros = crear_listas_auxiliares(nombres_usuarios)
      print(f"\nLista ordenada: {nombres_usuarios_ordenados}")
      print(f"Lista invertida: {nombres_usuarios_invertidos}")
      print(f"Dos últimos: {dos_ultimos}")
      print(f"Dos primeros: {dos_primeros}")
    elif opcion == "3":
      agregar_usuario(nombres_usuarios)
    elif opcion == "4":
      usuario_a_buscar = input("Ingrese el nombre de usuario a buscar: ")
      buscar_usuario(nombres_usuarios, usuario_a_buscar)
    elif opcion == "5":
      print("Saliendo del programa...")
      break
    else:
      print("Opción no válida. Intente nuevamente.")

# Ejecución del programa

menu_principal()  # Llamada a la función del menú principal

