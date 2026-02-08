from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/flight")
def flight():
    return jsonify([
        {"airline": "Air India", "route": "BLR → LHR", "stops": "Non-stop", "price": "₹28,400"},
        {"airline": "British Airways", "route": "BLR → LHR", "stops": "1 Stop", "price": "₹31,800"},
        {"airline": "Lufthansa", "route": "BLR → LHR", "stops": "1 Stop", "price": "₹34,600"}
    ])

@app.route("/hotel")
def hotel():
    return jsonify([
        {"name": "The Ritz London", "stars": 5, "distance": "0.8 mi", "price": "₹42,000/night"},
        {"name": "Park Plaza Westminster", "stars": 4, "distance": "1.5 mi", "price": "₹18,500/night"},
        {"name": "Premier Inn City", "stars": 3, "distance": "3.2 mi", "price": "₹9,200/night"}
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
