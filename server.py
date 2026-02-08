from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


HTML_FALLBACK = """
<!DOCTYPE html>
<html>
<head>
  <title>Nandi Travel AI</title>
  <style>
    body {
      background:#0b1220;
      color:white;
      font-family:Arial;
      padding:40px;
    }
    h1 { color:#4da3ff; }
    button {
      padding:10px 16px;
      margin:6px;
      border-radius:6px;
      border:none;
      cursor:pointer;
    }
  </style>
</head>
<body>
  <h1>Hi there 👋</h1>
  <p>Nandi’s Travel AI is running successfully.</p>
  <button onclick="fetchData('/flight')">Flights</button>
  <button onclick="fetchData('/hotel')">Hotels</button>
  <pre id="out"></pre>

<script>
function fetchData(type){
  fetch(type, {method:'POST'})
    .then(r=>r.json())
    .then(d=>document.getElementById('out').textContent =
      JSON.stringify(d,null,2))
}
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_FALLBACK.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/flight":
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

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


PORT = int(os.environ.get("PORT", 8080))
print(f"Server running on 0.0.0.0:{PORT}")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
