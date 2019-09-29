from source.persistence.database import *
#from encoder import *
from http.server import HTTPServer, BaseHTTPRequestHandler
#from person import *
import json

class PersonHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()


    def do_GET(self):
        self._set_headers()
        db = get_db_connection()
        people = get_data_from_dictionary("Person")
        jd = json.dumps(people)
        self.wfile.write(jd.encode('utf-8'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        print(data)
        add_person(data["first_name"], data["surname"], data["age"])
        self.send_response(201)
        self.end_headers()

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, PersonHandler)
    print("Starting server")
    httpd.serve_forever()
