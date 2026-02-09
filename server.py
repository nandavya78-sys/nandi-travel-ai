from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- FRONTEND ----------
@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


# ---------- CHAT ----------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "").lower()

    if "flight" in user_msg:
        return jsonify({"reply": "Sure ✈️ Click + and choose Flights to search."})
    if "hotel" in user_msg:
        return jsonify({"reply": "Got it 🏨 Click + and choose Hotels to search."})

    return jsonify({"reply": "Hi there! Ask me about flights or hotels 😊"})


# ---------- FLIGHTS ----------
@app.route("/flight", methods=["POST"])
def flight():
    return jsonify([
        {"airline": "Air India", "route": "BLR → LHR", "stops": "Non-stop", "price": "₹28,400"},
        {"airline": "British Airways", "route": "BLR → LHR", "stops": "1 Stop", "price": "₹31,800"},
        {"airline": "Lufthansa", "route": "BLR → LHR", "stops": "1 Stop", "price": "₹34,600"}
    ])


# ---------- HOTELS ----------
@app.route("/hotel", methods=["POST"])
def hotel():
    return jsonify([
        {"name": "The Ritz London", "stars": 5, "price": "₹42,000 / night"},
        {"name": "Park Plaza Westminster", "stars": 4, "price": "₹18,500 / night"},
        {"name": "Premier Inn City", "stars": 3, "price": "₹9,200 / night"}
    ])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
