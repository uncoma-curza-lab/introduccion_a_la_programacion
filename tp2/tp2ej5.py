"""Reciba como entrada el año de nacimiento de una persona y
calcule aproximadamente su edad, teniendo en cuenta solo su año
de nacimiento y el año actual"""

# Solicita el año de nacimiento y el año actual al usuario
anio_nacimiento = int(input("Por favor, introduce tu año de nacimiento: "))
anio_actual = int(input("Por favor, introduce el año actual: "))

# Calcula la edad y muestra el resultado
edad = anio_actual - anio_nacimiento
print(f"Tienes aproximadamente {edad} años.")

