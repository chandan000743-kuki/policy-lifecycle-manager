from flask import Flask
from middleware.day8security_headers import add_security_headers

app = Flask(__name__)

# Apply security headers
add_security_headers(app)

@app.route("/health")
def health():
    return {
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(debug=True)