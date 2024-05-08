Departamento de Ciencia y Tecnología

Universidad Nacional del Comahue

Centro Regional Zona Atlántica

Tecnicatura en Desarrollo Web

---

**Asignatura: INTRODUCCIÓN A LA PROGRAMACIÓN**

**TRABAJO PRÁCTICO: Estructuras Repetitivas: Fija (FOR) y Condicional (WHILE)**

**PRÁCTICA**

Para cada uno de los ejercicios identificar los siguientes ítems:

- Objetivo del problema

- Datos relevantes

- Programa Python

**Ejercicio 1**

a. Construya un programa que lea los 10 primeros números naturales y determinar su suma.

b. Modifique el programa anterior para que muestre el promedio de los pares y el promedio de los impares.

**Ejercicio 2**

Dado un número N calcular su factorial. Utilizar ciclo definido, estructura For y variable acumuladora del producto.

<u>Ejemplo:</u> 4! =4\*3\*2\*1 = 24

**Ejercicio 3**

Leer un número X y una secuencia de números. Mostrar cuál es el porcentaje de números leídos que fueron múltiplos de X. Utilizar ciclo iterativo.

<u>Ejemplo:</u> X= 8 y la secuencia 12, 23, 24, 56, 11, 16, la salida es: 50

**Ejercicio 4**

Escribir los números positivos MENORES a N, donde N es un número solicitado al usuario

**Ejercicio 5**

Ingresar dos números a y b. retornar la suma de los números impares naturales que hay entre ellos.

Este problema se resuelve con ¿ciclo definido o indefinido?

<u>Ejemplo:</u> a=4 y b= 12, el cálculo es 5+7+9+11 y la salida es: 32.

**Ejercicio 6**

Escriba un procedimiento/función CartelMayor que muestre por pantalla la frase “es un número mayor que cincuenta” y un procedimiento CartelMenor que muestre por pantalla la frase “ es un número menor que cincuenta”.

Utilizando los procedimientos anteriores ingrese distintos números enteros por teclado hasta ingresar el número (-1) que actuaría de corte. Luego muestre por pantalla los carteles adecuados.

Halle e imprima la suma de todos los números menores de cincuenta.

**Ejercicio 7**

Sin ejecutar el siguiente programa, determinar cuál es la salida en pantalla si se ingresan los valores x= 6, y=7. Practicar con traza.

```python
def coordenadaZ(x,y):
    x=x+10
    y=y+15
    return x+y

#principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
    z=coordenadaZ(x,y)
    x=x+1
    y=y+1
print(x," . ",y)
```

**Ejercicio 8**

Crear un programa que permita al usuario procesar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará), cortando el ingreso de datos cuando el usuario ingrese el monto 0.

Si ingresa un monto negativo, no se debe procesar y se debe pedir que proporcione un nuevo monto. Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superar el total del $1000, se debe aplicar un 10% de descuento.

**Ejercicio 9**

a. Desarrollar una función que indique si un determinado entero es un número primo. Desde el programa principal: ingrese 25 números enteros e imprima un mensaje indicando si es o no primo (llamando a la función) y el promedio de todos los números ingresados.

b. Desarrolle el punto a utilizando ciclo INDEFINIDO. Utilizando los procedimientos anteriores ingrese distintos números enteros por teclado hasta ingresar el número (0) que actuaría de corte.

**Ejercicio 10**

Escribir una función que , dado un número de DNI, retorne True si el número es válido y False si no lo es.

Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos. Permita que el usuario ingrese distintos DNI por teclado hasta ingresar el número (-1) que actuaría de corte.
