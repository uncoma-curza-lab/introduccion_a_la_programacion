# Demo de Módulos en Python

En Python, el proceso de incorporar código de una biblioteca se llama **importación**. Las bibliotecas en Python son conjuntos de módulos, que son archivos de Python que contienen definiciones y declaraciones, como funciones, clases y variables.

Ver el [Tutorial de Módulos](https://docs.python.org/es/3/tutorial/modules.html) oficial de Python.

Al importar un módulo, Python busca ese archivo o conjunto de archivos y hace disponibles todas las funciones y clases definidas en ellos para su uso en el programa actual. Esto se hace utilizando la palabra clave `import`.

Por ejemplo, un módulo llamado `math` que contiene una función llamada `sqrt` se importa y usa de la siguiente manera:

```python
import math
print(math.sqrt(16))  # Imprime: 4.0
```

## Biblioteca de Módulos Estándar

Python viene con una gran cantidad de módulos estándar, es decir, bibliotecas de módulos que están disponibles por defecto con la instalación de Python. Algunos de las más importantes son:

1. **math**: Proporciona funciones matemáticas como `sqrt`, `sin`, `cos`, `tan`, `log`, etc.
2. **os**: Proporciona funciones para interactuar con el sistema operativo, como cambiar el directorio de trabajo, listar los archivos en un directorio, etc.
3. **sys**: Proporciona acceso a algunas variables y funciones utilizadas o mantenidas por el intérprete de Python.
4. **datetime**: Proporciona clases para manipular fechas y horas.
5. **random**: Proporciona funciones para generar números aleatorios.

### Módulos estándar para desarrollo web

Python viene con una serie de módulos estándar que son útiles para el desarrollo web. Por ejemplo:

1. **http.server**: biblioteca simple para la creación de servidores web. Útil para servir archivos estáticos o para crear un servidor de prueba rápido.
2. **mimetypes**: para mapear nombres de archivo a tipos MIME y viceversa.
3. **urllib**: proporciona funciones para hacer solicitudes HTTP, trabajar con URLs y manejar cookies.
4. **html**: contiene funciones para trabajar con HTML.
5. **socketserver**: provee clases de base para manejar conexiones de red

De todas formas, la mayoría de las aplicaciones web en Python se construyen utilizando frameworks de terceros como **Django** o **Flask**, que proporcionan una estructura y funcionalidades adicionales. Estos frameworks no son parte de la biblioteca estándar de Python y deben instalarse por separado, generalmente usando el comando `pip`.

## Uso de módulos

a. Veamos el uso básico del módulo `os`:

```python
import os

archivos = os.listdir('.')
print(archivos)
```
Dará una salida del tipo:
```shell
['readme.md', 'archivo1.py', 'archivo2.py', 'virus.exe', 'listar_dir.py']
```

b. Si queremos listar en formato vertical:

```python
import os

archivos = os.listdir('.')
for archivo in archivos:
    print(archivo)
```

Dará como salida:

```shell
readme.md
archivo1.py
archivo2.py
virus.exe
listar_dir.py
listar_dir_vertical.py
```

c. ahora vamos a hacer un servidor web básico importando los módulos `http.server` y `socketserver`

```python
import http.server
import socketserver

PUERTO=8000

class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hola mundo") #cadena de bytes para sockets

with socketserver.TCPServer(("", PUERTO), MiHandler) as httpd:
    print("Sirviendo en el puerto", PUERTO)
    httpd.serve_forever()
```

Luego se debe ejecutar y acceder a http://localhost:8000

---

***Comentario 1**: `class` se usa para definir una clase, que es una plantilla para crear objetos. En este código, `MiHandler` es una clase que hereda de `http.server.SimpleHTTPRequestHandler`. La clase `MiHandler` tiene un método llamado `do_GET`, que se ejecuta cuando el servidor recibe una solicitud **GET**.*

---

***Comentario 2**: `with` se utiliza para envolver la ejecución de un bloque de código con métodos definidos por un administrador de contexto. Un administrador de contexto es un objeto que define los métodos `__enter__` y `__exit__` que se utilizan para configurar y deshacer configuraciones, respectivamente. En el código, `with socketserver.TCPServer(("", PUERTO), MiHandler) as httpd:` crea un servidor **TCP** que escucha en el `PUERTO` especificado y utiliza `MiHandler` para manejar las solicitudes. `httpd` es el objeto servidor que se crea y `httpd.serve_forever()` se llama dentro del bloque `with`, lo que significa que el servidor continuará escuchando y respondiendo a las solicitudes hasta que se interrumpa el programa.*

---

d. Vamos a listar el contenido del directorio de trabajo y enviarlo por la web

```python
import http.server
import socketserver
import os

PUERTO = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        archivos = os.listdir('.')
        mensaje = '<br>'.join(archivos)
        self.wfile.write(bytes(mensaje, "utf8"))
        return

with socketserver.TCPServer(("", PUERTO), Handler) as httpd:
    print("sirviendo en el puerto", PUERTO)
    httpd.serve_forever()
```

e. pero este es un listado muy simple, lo mejor sería poder ofrecer vínculos a los contenidos e incluirlos en una lista sin orden de html `<ul>`:

```python
import http.server
import socketserver
import os

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if os.path.isfile(path):
            super().do_GET()
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            archivos = os.listdir('.')
            mensaje = []
            for archivo in archivos:
                mensaje.append(f'<li><a href="{archivo}">{archivo}</a></li>')
            mensaje = '<ul>' + '\n'.join(mensaje) + '</ul>'
            self.wfile.write(bytes(mensaje, "utf8"))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("sirviendo en el puerto", PORT)
    httpd.serve_forever()
```

f. por último, filtremos los archivos que sean texto y se puedan mostrar en el navegador usando `mimetypes`:

```python
import http.server
import socketserver
import os
import mimetypes

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if os.path.isfile(path):
            super().do_GET()
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            archivos = os.listdir('.')
            mensaje = []
            for archivo in archivos:
                mimetype = mimetypes.guess_type(archivo)[0]
                if mimetype in ['text/html', 'text/plain', 'text/x-python', 'text/markdown']:
                    mensaje.append(f'<li><a href="{archivo}">{archivo}</a></li>')
                else:
                    mensaje.append(f'<li>{archivo}</li>')
            mensaje = '<ul>' + '\n'.join(mensaje) + '</ul>'
            self.wfile.write(bytes(mensaje, "utf8"))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("sirviendo en el puerto", PORT)
    httpd.serve_forever()
```

## Para más detalles:
- [Tutorial en castellano la página de Python](https://docs.python.org/es/3/tutorial/modules.html)
- [Tutorial en inglés en la página de w3Schools](https://www.w3schools.com/python/python_modules.asp)
