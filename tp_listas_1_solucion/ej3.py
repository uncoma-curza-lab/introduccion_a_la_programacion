# a) Armar una lista con números enteros positivos entre 0 y 20
lista = list(range(21))
print("Lista de números enteros positivos entre 0 y 20:", lista)

# b) Armar una lista entre 0 y 20 con múltiplos de 2
multiplos_de_2 = list(range(0, 21, 2))
print("\nLista de múltiplos de 2 entre 0 y 20:", multiplos_de_2)

# c) Armar una lista entre 0 y 20 con múltiplos de 5 y además emitir un mensaje con la cantidad de números impares
multiplos_de_5 = list(range(0, 21, 5))
impares = [num for num in multiplos_de_5 if num % 2 != 0]
print("\nLista de múltiplos de 5 entre 0 y 20:", multiplos_de_5)
print("Cantidad de números impares: ", len(impares))

# d) Generar una lista con los N primeros términos de la sucesión de Fibonacci
def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print("\nLos primeros 6 términos de la sucesión de Fibonacci:", fibonacci(6))
