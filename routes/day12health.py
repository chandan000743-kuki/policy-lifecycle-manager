from flask import Blueprint, jsonify

day12health_bp = Blueprint("day12health", __name__)

@day12health_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "security": "flask-talisman enabled"
    })