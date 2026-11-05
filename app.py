from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
<<<<<<< HEAD
        page = f"<h1>Hi, Sam!</h1><p>Today is {date.today():%B %d, %Y}</p>"
=======
        page = f"<h1>Hey, Sam!</h1><p>Today is {date.today():%B %d, %Y}</p>"
>>>>>>> greet-hey
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(page.encode())

if __name__ == "__main__":
    print(f"listening on {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
