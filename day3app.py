from flask import Flask, request, jsonify
from middleware.day3_sanitizer import sanitize_input

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "Day 3 Input Sanitisation Service Running"
    }


@app.route("/sanitize", methods=["POST"])
def sanitize():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "status": "error",
            "message": "Text field is required"
        }), 400

    text = data.get("text", "")

    result = sanitize_input(text)

    if not result["safe"]:
        return jsonify({
            "status": "blocked",
            "message": result["error"],
            "cleaned_text": result["cleaned_text"]
        }), 400

    return jsonify({
        "status": "success",
        "message": "Input sanitised successfully",
        "cleaned_text": result["cleaned_text"]
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5002)