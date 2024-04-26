"""Diseñar el algoritmo principal que invoque a los módulos anteriores las veces
que sea necesaria para imprimir una cancha de fútbol de acuerdo al siguiente formato:

+---------------+---------------+
|               |               |
|               |               |
+----+          |          +----+
|    |          /\         |    |
etc.
"""

def linea_superior():
    print('+---------------+---------------+')

def linea_vacia():
    print('|               |               |')

def linea_central():
    print('+----+          |          +----+')

def linea_area():
    print('|    |\\        / \\        /|    |')

def centro_cancha():
    print('|  · | )      ( · )      ( | ·  |')

def linea_superior_invertida():
    print('|    |/        \\ /        \\|    |')

def linea_central_invertida():
    print('+----+          |          +----+')

# Dibujar la cancha de fútbol
linea_superior()
linea_vacia()
linea_vacia()
linea_central()
linea_area()
centro_cancha()
linea_superior_invertida()
linea_central_invertida()
linea_vacia()
linea_vacia()
linea_superior()
