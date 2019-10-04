from http.server import HTTPServer, BaseHTTPRequestHandler
from source.persistence.database import *
from source.format.format import *


def render_drinks(drinks_dict):
    drinks_html = ""
    for drink_name in drinks_dict.values():
        drinks_html += f'<li>{drink_name}</li>'
    return drinks_html

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Tell the client we're about to send HTML content in our HTTP payload
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        drinks_dict = create_dictionary("drink", "drink_id", "name")

        # Produce the HTML
        html_document = f"""
<!doctype html>
<html>
    <body>
        <p>Available drinks:</p>
        <ul>
            {render_drinks(drinks_dict)}
        </ul>
    </body>
</html>
"""
        # Render and send response
        self.wfile.write(html_document.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    print("Starting server")
    httpd.serve_forever()