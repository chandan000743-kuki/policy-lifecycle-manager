from flask import Blueprint, request, jsonify
from middleware.day13auth import require_token

day13_bp = Blueprint("day13", __name__)

request_count = 0


@day13_bp.route("/secure-data", methods=["GET"])
@require_token
def secure_data():

    return jsonify({
        "message": "Secure data accessed successfully"
    })


@day13_bp.route("/xss-test", methods=["POST"])
def xss_test():

    data = request.get_json()

    text = data.get("text", "")

    if "<script>" in text.lower():
        return jsonify({
            "error": "XSS attempt blocked"
        }), 400

    return jsonify({
        "message": "Safe input accepted"
    })


@day13_bp.route("/rate-limit-test", methods=["GET"])
def rate_limit_test():

    global request_count

    request_count += 1

    if request_count > 5:
        return jsonify({
            "error": "Too Many Requests"
        }), 429

    return jsonify({
        "message": "Request successful"
    })