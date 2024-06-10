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
