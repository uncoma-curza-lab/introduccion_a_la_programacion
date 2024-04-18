"""Héctor trabaja en una empresa de informática.
En su computadora administra archivos de gran tamaño y,
por recomendación de su jefe, el archivo que trabajó en
el día debe ser copiado en una carpeta utilizando un
software de la empresa. Este software le muestra a Héctor
la cantidad de segundos que tardó en realizar la copia.
El problema es que Héctor necesita los “segundos” expresados
en “minutos:segundos” para elaborar un informe diario y
no sabe cómo hacerlo. Por ejemplo: Ayer uno de los archivos
tardó 513 segundos.
Antes de ayer otro archivo tardó 86 segundos.
Programe el algoritmo que solucione el problema de Héctor
cada vez que lo necesite."""

# Solicitar al usuario que ingrese la cantidad de segundos
segundos = int(input("Por favor, ingresa la cantidad de segundos: "))

# Calcular los minutos y los segundos restantes
minutos = segundos // 60
segundos_restantes = segundos % 60

# Imprimir el resultado en formato "minutos:segundos"
print(f"Los {segundos} segundos corresponden a {minutos} minutos y {segundos_restantes} segundos.")
