from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class HttpGetHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="./htdocs", **kwargs)

def run(server_class=HTTPServer, handler_class=HttpGetHandler):
  server_address = ('', 80)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

run()
