from http.server import BaseHTTPRequestHandler
from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer
import os
from io import open

class Router:
    pass

class HttpGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':                
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("./htdocs/index.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Page not found')



def run(server_class=HTTPServer, handler_class=HttpGetHandler):
  server_address = ('', 8081)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

run()
