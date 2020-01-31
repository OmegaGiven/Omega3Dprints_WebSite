from http.server import HTTPServer, BaseHTTPRequestHandler
from time import strftime

class CS2610Assn1(BaseHTTPRequestHandler):
    """
    Your task is to define this class such that it fulfills the assingment
    requirements.

    Refer to the official Python documentation for the `http.server` class for
    details on what can go in here.

    Replace this pass statement with your own code:
    """
    def serve_file(self, fileName):
        f = open(fileName, 'rb')
        data = f.read()
        f.close()
        self.wfile.write(b'HTTP/1.1 200 OK\n\n')
        self.wfile.write(b"Server:Omega3DPrints server\n")
        self.wfile.write(bytes(f"Date: {strftime('%c')}\n", 'utf-8'))
        self.wfile.write(bytes(f"Content-Length: {len(data)}\n", "utf-8"))
        self.wfile.write(bytes(f"Content-Type: text/plain\n", "utf-8"))
        self.wfile.write(b'\n')
        self.wfile.write(data)

    def redir301(self, location='/index.html'):
        self.wfile.write(b'HTTP/1.1 301 Moved Permanently\n')
        self.wfile.write(b'Server: Omega3DPrints\n')
        self.wfile.write(bytes(f"Date:{strftime('%c')}\n", 'utf-8'))
        self.wfile.write(bytes(f'Location: {location}\n', 'utf-8'))
        self.wfile.write(b'\n')

    def do_GET(self):
        print(f"[{strftime('%c')}] GET {self.path}")
        if self.path == '/index.html' or self.path == '/':
            f = open('index.html', 'rb')
            self.wfile.write(b'HTTP/1.1 200 OK\n\n')
            self.wfile.write(f.read())
            f.close()
        elif self.path.endswith(".jpg") or self.path.endswith(".png"):
            f = open('../' + self.path, 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        elif self.path == '/style.css':
            self.serve_file('style.css')
        elif self.path.startswith('/tips.html') or self.path == '/':
            f = open('tips.html', 'rb')
            self.wfile.write(b'HTTP/1.1 200 OK\n\n')
            self.wfile.write(f.read())
            f.close()
        elif self.path.startswith('/blog') or self.path == '/':
            f = open('blog.html', 'rb')
            self.wfile.write(b'HTTP/1.1 200 OK\n\n')
            self.wfile.write(f.read())
            f.close()
        elif self.path == '/about.html' or self.path == '/' or self.path == '/about' or self.path.startswith('/bio'):
            f = open('about.html', 'rb')
            self.wfile.write(b'HTTP/1.1 200 OK\n\n')
            self.wfile.write(f.read())
            f.close()
        else:
            self.do_404()

    def do_404(self):
        resp = b"""
        HTTP/1.1 404 Not Found
        Server: Omega 3D Prints

        <html>
            <head>
                <title>Sorry dude, wrong file</title>
            </head>
            <body>
                <h1>That file doesn't exist</h1>
                <p>Please try again when you can learn to spel</p>
            </body>
        </html>"""
        self.wfile.write(resp)


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    print(f"Serving from http://{server_address[0]}:{server_address[1]}")
    print("Press Ctrl-C to quit\n")
    HTTPServer(server_address, CS2610Assn1).serve_forever()
