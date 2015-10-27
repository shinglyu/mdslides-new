from os import curdir
from os.path import join as pjoin

from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer

class StoreHandler(SimpleHTTPRequestHandler):
    store_path = pjoin(curdir, 'slide.md')

    def do_GET(self):
        super(StoreHandler, self).do_GET();

#        if self.path == '/n':
#            with open(self.store_path) as fh:
#                self.send_response(200)
#                self.send_header('Content-type', 'text/json')
#                self.end_headers()
#                self.wfile.write(fh.read().encode())

    def do_POST(self):
        if self.path == '/save':
            length = self.headers['content-length']
            data = self.rfile.read(int(length))

            with open(self.store_path, 'w') as fh:
                fh.write(data.decode())

            self.send_response(200)


server = HTTPServer(('', 9876), StoreHandler)
server.serve_forever()
