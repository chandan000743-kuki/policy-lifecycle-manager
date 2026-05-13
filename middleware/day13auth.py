from functools import wraps
from flask import request, jsonify

def require_token(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({
                "error": "Unauthorized",
                "message": "JWT token missing"
            }), 401

        if token != "Bearer admin-token":
            return jsonify({
                "error": "Forbidden",
                "message": "Invalid role or token"
            }), 403

        return f(*args, **kwargs)

    return wrapper