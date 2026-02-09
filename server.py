from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os

class Handler(BaseHTTPRequestHandler):

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        # Serve UI
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

        # Flights API
        elif self.path == "/flights":
            self.send_json([
                {
                    "airline": f"Airline {i}",
                    "stops": "Non-stop" if i % 2 == 0 else "1 Stop",
                    "class": "Economy",
                    "public": 28000 + i * 600,
                    "corporate": 26500 + i * 500,
                    "gst": 1300 + i * 50
                } for i in range(1,7)
            ])

        # Hotels API
        elif self.path == "/hotels":
            self.send_json([
                {
                    "name": f"Hotel {i}",
                    "stars": 3 + (i % 3),
                    "distance": i * 2,
                    "price": 6500 + i * 700
                } for i in range(1,7)
            ])

        else:
            self.send_response(404)
            self.end_headers()


PORT = int(os.environ.get("PORT", 8080))
print(f"Server running on 0.0.0.0:{PORT}")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
