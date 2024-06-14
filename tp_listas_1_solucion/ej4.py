# Arme una lista con el factorial de un número N, ingresado por teclado. Ejemplo: 4! = 4x3x2x1.

# Solicitamos al usuario que ingrese un número
N = int(input("Ingrese un número: "))

# Inicializamos la variable factorial en 1
factorial = 1

# Creamos una lista vacía para almacenar los números del factorial
lista_factorial = []

# Usamos un bucle for para multiplicar sucesivamente los números
for i in range(1, N + 1):
    factorial *= i
    lista_factorial.append(factorial)

# Imprimimos la lista con los factoriales
print(lista_factorial)
