from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "Day 7 OWASP ZAP Security Review Service Running"
    }


@app.route("/zap-summary")
def zap_summary():
    return jsonify({
        "scan_type": "OWASP ZAP Baseline Scan",
        "target": "http://127.0.0.1:5004",
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "status": "ZAP scan report documented"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5005)