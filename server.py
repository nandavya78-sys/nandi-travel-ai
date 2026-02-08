from http.server import BaseHTTPRequestHandler,HTTPServer
import json

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path in ["/","/index.html"]:
            with open("index.html","rb") as f:
                self.send_response(200)
                self.send_header("Content-Type","text/html")
                self.end_headers()
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path=="/chat":
            self.send_text("🙂 Ask me about flights or hotels. Use + to start.")

        elif self.path=="/flight":
            self.send_json([
                {"airline":"Air India","route":"BLR → LHR","stops":"Non-stop","price":"₹28,400"},
                {"airline":"British Airways","route":"BLR → LHR","stops":"1 Stop","price":"₹31,900"},
                {"airline":"Lufthansa","route":"BLR → LHR","stops":"1 Stop","price":"₹34,600"}
            ])

        elif self.path=="/hotel":
            self.send_json([
                {"name":"The Ritz London","star":5,"dist":"0.8 mi","price":"₹42,000/night"},
                {"name":"Park Plaza Westminster","star":4,"dist":"1.5 mi","price":"₹18,500/night"},
                {"name":"Premier Inn City","star":3,"dist":"3.2 mi","price":"₹9,200/night"}
            ])

    def send_text(self,text):
        self.send_response(200)
        self.send_header("Content-Type","text/plain")
        self.end_headers()
        self.wfile.write(text.encode())

    def send_json(self,data):
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

import os

PORT = int(os.environ.get("PORT", 8000))

print(f"Server running on 0.0.0.0:{PORT}")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()


