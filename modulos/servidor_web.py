import http.server
import socketserver

PUERTO=8000

class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hola mundo</h1>")

with socketserver.TCPServer(("", PUERTO), MiHandler) as httpd:
    print("Sirviendo en el puerto", PUERTO)
    httpd.serve_forever()