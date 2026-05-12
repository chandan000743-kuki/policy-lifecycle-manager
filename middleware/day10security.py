from functools import wraps
from flask import request, jsonify
import time
import re

request_log = {}

def require_jwt(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({
                "error": "Unauthorized access blocked",
                "message": "Missing or invalid JWT token"
            }), 401

        return f(*args, **kwargs)
    return wrapper


def simple_rate_limit(max_requests=5, window_seconds=60):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            ip = request.remote_addr
            now = time.time()

            if ip not in request_log:
                request_log[ip] = []

            request_log[ip] = [
                timestamp for timestamp in request_log[ip]
                if now - timestamp < window_seconds
            ]

            if len(request_log[ip]) >= max_requests:
                return jsonify({
                    "error": "Too Many Requests",
                    "message": "Rate limit exceeded"
                }), 429

            request_log[ip].append(now)
            return f(*args, **kwargs)
        return wrapper
    return decorator


def contains_injection(text):
    patterns = [
        r"<script.*?>.*?</script>",
        r"('|\\\")\\s*OR\\s*1=1",
        r"DROP\\s+TABLE",
        r"UNION\\s+SELECT",
        r"ignore previous instructions",
        r"system prompt"
    ]

    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False