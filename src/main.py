from http.server import BaseHTTPRequestHandler
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
import os

class HttpGetHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="./htdocs", **kwargs)
        
class HttpGetHandler1(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        paths = list()
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                paths.append(file_path)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>Был получен GET-запрос. {}</body></html>'.format('\n'.join(paths)).encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler1):
  server_address = ('', 8081)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

run()
