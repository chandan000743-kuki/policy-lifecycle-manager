from flask import Flask
from routes.day13security_test import day13_bp
from middleware.day12talisman import enable_talisman

app = Flask(__name__)

enable_talisman(app)

app.register_blueprint(day13_bp)

@app.route("/health")
def health():
    return {
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(debug=False)