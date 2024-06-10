import http.server
import socketserver
import os
PUERTO = 8000

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
            mensaje=[]
            for archivo in archivos:
                mensaje.append(f'<li><a href="{archivo}">{archivo}</a></li>')
            mensaje = '<ul>' + '\n'.join(mensaje) + '</ul>'
            self.wfile.write(bytes(mensaje, "utf8"))
        return
    
with socketserver.TCPServer(("", PUERTO), Handler) as httpd:
    print("sirviendo en el puerto", PUERTO)
    httpd.serve_forever()