""" Ejercicio 3: Los siguientes programas no contienen errores sintácticos y Python los ejecutaría. Escribe cuál 
sería la salida de cada uno de estos programas, explicando brevemente el motivo de tu respuesta. Si 
consideras que el programa no produciría ninguna salida, explica por qué. """

#PUNTO A
numero = input("Ingrese un número: ")
numero = int(numero)
if numero == 3:
 print("¡Acertaste!")
elif numero == 4 or numero == 2:
 print("¡Casi aciertas!")
else:
 print("Frío, frío")

""" RTA: la salida del programa dependerá del número que ingrese el usuario. 
Si ingresa 3, la salida será "¡Acertaste!". 
Si ingresa 4 o 2, la salida será "¡Casi aciertas!". 
Para cualquier otro número, la salida será "Frío, frío"."""

#PUNTO B

a = 20
if a > 15:
 print("Este es el primer saludo")
elif a < 30:
 print("Este es el segundo saludo")
elif a != 15:
 print("Este es el tercer saludo")
else:
 print("Este es el cuarto saludo")

#RTA: En pantalla sale el mensaje "este es el primer saludo" ya que la variable a tiene asignado el valor 20 y es > a 15
