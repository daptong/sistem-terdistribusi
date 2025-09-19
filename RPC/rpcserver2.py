from jsonrpc import JSONRPCResponseManager, dispatcher
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

@dispatcher.add_method
def convert(a):
    dictionary = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
      "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    res = ''.join(dictionary[i] for i in a.split())
    return res

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        response = JSONRPCResponseManager.handle(post_data, dispatcher)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.json.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=4000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'starting rpc server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
