""" Genere una lista con los N nombres usuarios habilitados para ingresar al sistema SIU,
se los debe ingresar por teclado. Además se pide, armar otra lista llamada “ccaract” con
la longitud de caracteres de cada nombre de usuario. Se desea saber en promedio cuál es
la longitud de caracteres de los nombres de los usuarios"""

# Solicitamos al usuario que ingrese la cantidad de usuarios
N = int(input("Ingrese la cantidad de usuarios: "))

# Creamos una lista vacía para almacenar los nombres de los usuarios
usuarios = []

# Solicitamos al usuario que ingrese los nombres de los usuarios
for i in range(N):
    nombre = input("Ingrese el nombre del usuario " + str(i + 1) + ": ")
    usuarios.append(nombre)

# Creamos una lista con la longitud de caracteres de cada nombre de usuario
ccaract = [len(nombre) for nombre in usuarios]

# Calculamos el promedio de la longitud de los nombres de los usuarios
promedio = sum(ccaract) / N

# Imprimimos las listas y el promedio
print("Usuarios: ", usuarios)
print("Longitud de caracteres: ", ccaract)
print("Promedio de longitud de caracteres: ", promedio)
