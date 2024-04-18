""" Dada como entrada la temperatura en Grados Centígrados (G),
obtenga la temperatura Fahrenheit equivalente utilizando la siguiente
fórmula: F = (9/5) * G +32. Mostrar el resultado por pantalla."""

# Solicita la temperatura en grados centígrados al usuario
grados_centigrados = float(input("Por favor, introduce la temperatura en grados centígrados: "))

# Calcula la temperatura en grados Fahrenheit
grados_fahrenheit = (9/5) * grados_centigrados + 32

# Muestra el resultado
print(f"La temperatura en grados Fahrenheit es: {grados_fahrenheit}")

