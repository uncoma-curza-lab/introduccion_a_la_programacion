"""Crear un programa que permita al usuario procesar los montos de las compras
de un cliente (se desconoce la cantidad de datos que cargará),
cortando el ingreso de datos cuando el usuario ingrese el monto 0.

Si ingresa un monto negativo, no se debe procesar y se debe pedir
que proporcione un nuevo monto. Al finalizar, informar el total a pagar
teniendo en cuenta que, si las ventas superar el total del $1000,
se debe aplicar un 10% de descuento."""

total = 0
monto = float(input("Ingrese el monto de la compra (0 para terminar): "))

while monto != 0:
    if monto < 0:
        print("El monto no puede ser negativo. Intente de nuevo.")
    else:
        total += monto

    monto = float(input("Ingrese el monto de la compra (0 para terminar): "))

if total > 1000:
    total *= 0.9  # Aplicar un descuento del 10%

print("El total a pagar es: $", total)
