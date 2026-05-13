from flask import Flask, request, jsonify
from middleware.day8security_headers import add_security_headers
from middleware.day11security import validate_request

app = Flask(__name__)

add_security_headers(app)


@app.before_request
def security_check():
    result = validate_request()

    if result:
        return result


@app.route("/")
def home():
    return jsonify({
        "message": "Day 11 ZAP Active Scan App Running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/test-input", methods=["POST"])
def test_input():
    data = request.get_json()

    return jsonify({
        "message": "Input accepted safely",
        "data": data
    })


if __name__ == "__main__":
    app.run(debug=True)