"""Escriba una función que reciba la nota de un estudiante y devuelva la calificación en texto según la siguiente configuración:
Nota = 10 → Excelente
Nota: 8 o 9 → Sobresaliente
Nota = 7 → Aprobado
Nota: 4 o 5 o 6 → Regular
Nota_ 1 o 2 o 3 → Desaprobado
El programa principal debe mostrar un mensaje donde se indique el Nombre del alumno, Materia y Calificación. Por ejemplo:
“Alumno Jorge, su nota de Matemáticas es Sobresaliente”"""


def pasa_a_calificacion(nota):
    if nota == 10:
        return "Excelente"
    elif nota == 9 or nota == 8:
        return "Sobresaliente"
    elif nota == 7:
        return "Aprobado"
    elif nota == 6 or nota == 5 or nota == 4:
        return "Regular"
    else:
        return "Desaprobado"

def mostrar_calificacion(nombre, materia, nota):
    calif = pasa_a_calificacion(nota)
    print(f"Alumno {nombre}, su nota de {materia} es {calif}")

nombre = input("Ingrese el nombre del alumno: ")
materia = input("Ingrese la materia: ")
nota = int(input("Ingrese la nota: "))

mostrar_calificacion(nombre, materia, nota)
