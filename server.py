from os import curdir
from os.path import join as pjoin
import json

from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer

class StoreHandler(SimpleHTTPRequestHandler):
    lastUpdate = -1
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

            #print(json.loads(data.decode()))

            dataJson = json.loads(data.decode())
            #print('Server')
            #print(StoreHandler.lastUpdate)
            #print('Client')
            #print(dataJson['lastUpdate'])
            if (dataJson['lastUpdate'] < StoreHandler.lastUpdate):
                #print('failed!')
                response = bytes("CONFLICT", "utf-8") #create response

                self.send_response(409) #create header
                self.send_header("Content-Length", str(len(response)))
                self.end_headers()

                self.wfile.write(response) #send response
            else:
                #print('save!')
                StoreHandler.lastUpdate = dataJson['lastUpdate']
                with open(self.store_path, 'w') as fh:
                    fh.write(dataJson['text'])

                response = bytes("SAVED", "utf-8") #create response

                self.send_response(200) #create header
                self.send_header("Content-Length", str(len(response)))
                self.end_headers()

                self.wfile.write(response) #send response
               # self.send_response(200)


            #print(StoreHandler.lastUpdate)




server = HTTPServer(('', 9876), StoreHandler)
server.serve_forever()
