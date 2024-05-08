"""Escribir una función que , dado un número de DNI, retorne True si el número es válido
y False si no lo es.

Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
Permita que el usuario ingrese distintos DNI por teclado hasta ingresar el número (-1)
que actuaría de corte."""

def es_dni_valido(dni):
    # Un DNI válido debe tener entre 7 y 8 dígitos
    return 1000000 <= dni <= 99999999

dni = int(input("Ingrese un número de DNI (ingrese -1 para terminar): "))
while dni != -1:
    if es_dni_valido(dni):
        print(f"El número de DNI {dni} es válido.")
    else:
        print(f"El número de DNI {dni} no es válido.")
    dni = int(input("Ingrese otro número de DNI (ingrese -1 para terminar): "))
