import os

archivos = os.listdir('.')
for archivo in archivos:
    print(archivo)

# Oneliner --> [print(archivo) for archivo in os.listdir('.')]
