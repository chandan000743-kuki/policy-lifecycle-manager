from flask import Flask, request, jsonify
from middleware.day2input_sanitizer import is_malicious

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Day 2 Security Service Running"
    }

@app.route("/validate", methods=["POST"])
def validate_input():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "status": "error",
            "reason": "Text input is required"
        }), 400

    text = data.get("text", "")

    if is_malicious(text):
        return jsonify({
            "status": "blocked",
            "reason": "Malicious input detected"
        }), 400

    return jsonify({
        "status": "safe",
        "message": "Input accepted"
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)