from flask import request, jsonify

blocked_patterns = [
    "<script>",
    "DROP TABLE",
    "UNION SELECT",
    "' OR 1=1 --",
    "system prompt",
    "ignore previous instructions"
]

def validate_request():
    data = request.get_json(silent=True)

    if not data:
        return None

    text = str(data)

    for pattern in blocked_patterns:
        if pattern.lower() in text.lower():
            return jsonify({
                "error": "Blocked malicious request",
                "pattern_detected": pattern
            }), 400

    return None