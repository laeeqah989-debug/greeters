from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        page = f"<h1>Hello, Sam!</h1><p>Today is {date.today():%B %d, %Y}</p>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(page.encode())

if __name__ == "__main__":
    print(f"listening on {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
