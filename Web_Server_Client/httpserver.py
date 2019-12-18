#!/usr/bin/env python

from http.server import SimpleHTTPRequestHandler , HTTPServer
import os

#Create custom HTTPRequestHandler class
class HTTPRequestHandler(SimpleHTTPRequestHandler):
    #handle GET command
    def do_GET(self):
        rootdir = 'C:/Users/atakb/Desktop/Network Programming/Web_Server_Client/' #file location
        try:
            if self.path.endswith('.html'):
                f = open(rootdir + self.path) #open requested file

                #send code 200 response
                self.send_response(200)

                #send header first
                self.send_header('Content-type','text-html')
                self.end_headers()

                #send file content to client
                self.wfile.write(f.read().encode("utf-8"))
                f.close()
                return
            
        except IOError:
            self.send_error(404, 'file not found')
    
def run():
    print('http server is starting...')

    #ip and port of servr
    #by default http server port is 80
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()
