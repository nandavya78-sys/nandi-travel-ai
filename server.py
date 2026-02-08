from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            try:
                with open("index.html", "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"index.html not found")
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/chat":
            self.send_text("Ask me about flights or hotels. Use + to start.")

        elif self.path == "/flight":
            self.send_json([
                {"airline":"Air India","route":"BLR → LHR","stops":"Non-stop","price":"₹28,400"},
                {"airline":"British Airways","route":"BLR → LHR","stops":"1 Stop","price":"₹31,800"},
                {"airline":"Lufthansa","route":"BLR → LHR","stops":"1 Stop","price":"₹34,600"}
            ])

        elif self.path == "/hotel":
            self.send_json([
                {"name":"The Ritz London","stars":5,"distance":"0.8 mi","price":"₹42,000/night"},
                {"name":"Park Plaza Westminster","stars":4,"distance":"1.5 mi","price":"₹18,500/night"},
                {"name":"Premier Inn City","stars":3,"distance":"3.2 mi","price":"₹9,200/night"}
            ])
        else:
            self.send_response(404)
            self.end_headers()

    def send_text(self, text):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(text.encode())

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


PORT = int(os.environ.get("PORT", 8000))

print(f"Server running on 0.0.0.0:{PORT}")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
