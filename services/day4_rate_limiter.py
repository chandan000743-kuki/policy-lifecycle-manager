from flask import jsonify


def handle_rate_limit_error(error):
    retry_after = None

    if hasattr(error, "retry_after"):
        retry_after = error.retry_after

    return jsonify({
        "status": "error",
        "message": "Rate limit exceeded. Please try again later.",
        "retry_after": retry_after
    }), 429