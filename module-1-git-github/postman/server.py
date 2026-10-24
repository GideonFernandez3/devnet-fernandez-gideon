from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/':


            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, From my server using Python!')

        elif self.path == '/users':

            users = ["Gideon" , "Fernandez"]
            self.send_response(200)
            self.send_headers("Content-Type", "application/json")
            self.end_headers()

            response = json.dumps(users).encode('utf-8')
            self.wfile.write(response)

        else: 

            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Sorry the page is not Found!")

server = HTTPServer(("127.0.0.1", 8000), MyServer) 
server.serve_forever()
