from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os

class Handler(BaseHTTPRequestHandler):

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            base = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(base, "index.html"), "rb") as f:
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())

        elif self.path == "/flights":
            self.send_json([
                {
                    "id": i,
                    "airline": f"Airline {i}",
                    "route": "BLR → DEL",
                    "class": "Economy",
                    "public": 28000 + i*600,
                    "corporate": 26500 + i*500,
                    "gst": 1300 + i*50
                } for i in range(1,7)
            ])

        elif self.path == "/hotels":
            self.send_json([
                {
                    "id": i,
                    "name": f"Hotel {i}",
                    "stars": 3 + (i % 3),
                    "distance": i * 2,
                    "price": 6500 + i*700
                } for i in range(1,7)
            ])

        else:
            self.send_response(404)
            self.end_headers()

PORT = int(os.environ.get("PORT", 8080))
print(f"Server running on 0.0.0.0:{PORT}")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
