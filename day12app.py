from flask import Flask
from routes.day12health import day12health_bp
from middleware.day12talisman import enable_talisman

app = Flask(__name__)

enable_talisman(app)

app.register_blueprint(day12health_bp)

@app.route("/")
def home():
    return {
        "message": "Day 12 Flask-Talisman Security App Running"
    }

if __name__ == "__main__":
    app.run(debug=False)