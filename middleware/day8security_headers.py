from flask import Flask

def add_security_headers(app: Flask):

    @app.after_request
    def apply_headers(response):

        response.headers["X-Content-Type-Options"] = "nosniff"

        response.headers["X-Frame-Options"] = "DENY"

        response.headers["Referrer-Policy"] = "no-referrer"

        response.headers["Content-Security-Policy"] = "default-src 'self'"

        return response