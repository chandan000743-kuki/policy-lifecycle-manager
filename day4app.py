from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from services.day4_rate_limiter import handle_rate_limit_error

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

app.register_error_handler(429, handle_rate_limit_error)


@app.route("/")
def home():
    return jsonify({
        "message": "Day 4 Rate Limiting Service Running",
        "default_limit": "30 requests per minute"
    })


@app.route("/test-limit")
def test_limit():
    return jsonify({
        "status": "success",
        "message": "Default rate limit active"
    })


@app.route("/generate-report", methods=["POST"])
@limiter.limit("10 per minute")
def generate_report():
    return jsonify({
        "status": "success",
        "message": "Report generation request accepted",
        "limit": "10 requests per minute"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5003)