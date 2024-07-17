from http.server import BaseHTTPRequestHandler
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
import os
from io import open

class HttpGetHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="./htdocs/", **kwargs)
        
class HttpGetHandler1(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':                
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("./htdocs/index.html", "r") as f:
                extra = f.read()
                self.wfile.write(f.read().encode())
        elif self.path == '/read_file':
            extra = ""

            try:
                with open("./htdocs/index.html", "r") as f:
                    extra = f.read()
            except Exception as e:
                extra = str(e)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write('<html><head><meta charset="utf-8">'.encode())
            self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
            self.wfile.write('<body>{}</body></html>'.format(extra).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Page not found')



def run(server_class=HTTPServer, handler_class=HttpGetHandler1):
  server_address = ('', 8081)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

run()
