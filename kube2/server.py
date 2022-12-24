from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello world from hostname: ' + socket.gethostname().encode())

SERVER_PORT = 8000
httpd = HTTPServer(('0.0.0.0', SERVER_PORT), SimpleRequestHandler)
print('Listen on prot %s ...' % SERVER_PORT)
httpd.serve_forever()