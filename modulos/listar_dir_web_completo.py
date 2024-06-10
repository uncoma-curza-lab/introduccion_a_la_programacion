# Importamos las bibliotecas necesarias
import http.server
import socketserver
import os
import mimetypes

# Definimos el puerto en el que se ejecutará el servidor
PORT = 8000

# Definimos una clase Handler que hereda de http.server.SimpleHTTPRequestHandler
class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-type', '; charset=utf-8')
        super().end_headers()

    # Definimos el método do_GET que se ejecuta cuando el servidor recibe una solicitud GET
    def do_GET(self):
        # Traducimos la ruta de la solicitud a una ruta en el sistema de archivos
        path = self.translate_path(self.path)
        # Si la ruta corresponde a un archivo existente
        if os.path.isfile(path):
            # Llamamos al método do_GET de la clase padre (http.server.SimpleHTTPRequestHandler)
            super().do_GET()
        else:
            # Si la ruta no corresponde a un archivo existente, enviamos una respuesta HTTP 200
            self.send_response(200)
            # Añadimos un encabezado al HTTP response indicando que el contenido es HTML
            self.send_header('Content-type', 'text/html; charset=utf-8')
            # Terminamos los encabezados HTTP
            self.end_headers()
            # Obtenemos una lista de los archivos en el directorio actual
            archivos = os.listdir('.')
            mensaje = []
            # Para cada archivo en el directorio
            for archivo in archivos:
                # Obtenemos el tipo MIME del archivo
                mimetype = mimetypes.guess_type(archivo)[0]
                # Si el tipo MIME es uno de los siguientes, añadimos un enlace al archivo en el mensaje
                if mimetype in ['text/html', 'text/plain', 'text/x-python', 'text/markdown']:
                    mensaje.append(f'<li><a href="{archivo}">{archivo}</a></li>')
                else:
                    # Si el tipo MIME no es uno de los anteriores, simplemente añadimos el nombre del archivo al mensaje
                    mensaje.append(f'<li>{archivo}</li>')
            # Creamos una lista HTML con los elementos del mensaje
            mensaje = '<ul>' + '\n'.join(mensaje) + '</ul>'
            # Enviamos el mensaje como respuesta HTTP
            self.wfile.write(bytes(mensaje, "utf8"))

# Creamos un servidor TCP en el puerto especificado que utiliza la clase Handler para manejar las solicitudes
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # Imprimimos un mensaje indicando en qué puerto está sirviendo el servidor
    print("sirviendo en el puerto", PORT)
    # El servidor comienza a escuchar y responder a las solicitudes hasta que se interrumpe el programa
    httpd.serve_forever()
