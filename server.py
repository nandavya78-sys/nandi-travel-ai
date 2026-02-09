from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            try:
                base = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(base, "index.html"), "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    self.wfile.write(f.read())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/flights":
            self.send_json([
                {
                    "airline": "Air India",
                    "public": 28400,
                    "corporate": 27510,
                    "gst": 1310,
                    "stops": "Non-stop"
                }
            ])

        if self.path == "/hotels":
            self.send_json([
                {
                    "name": "Taj Palace",
                    "stars": 5,
                    "distance": 2,
                    "price": 9200
                }
            ])

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

PORT = int(os.environ.get("PORT", 8080))
print(f"Server running on 0.0.0.0:{PORT}")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
