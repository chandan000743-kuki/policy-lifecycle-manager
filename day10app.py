from flask import Flask, request, jsonify
from middleware.day8security_headers import add_security_headers
from middleware.day10security import require_jwt, simple_rate_limit, contains_injection

app = Flask(__name__)

add_security_headers(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Day 10 Security Sign-Off App Running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/protected-test", methods=["GET"])
@require_jwt
def protected_test():
    return jsonify({
        "message": "JWT verified successfully"
    })


@app.route("/rate-limit-test", methods=["GET"])
@simple_rate_limit(max_requests=5, window_seconds=60)
def rate_limit_test():
    return jsonify({
        "message": "Request allowed"
    })


@app.route("/injection-test", methods=["POST"])
def injection_test():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "Text field is required"
        }), 400

    text = data["text"]

    if contains_injection(text):
        return jsonify({
            "error": "Injection attempt blocked",
            "message": "Suspicious input detected"
        }), 400

    return jsonify({
        "message": "Input accepted",
        "text": text
    })


if __name__ == "__main__":
    app.run(debug=True)