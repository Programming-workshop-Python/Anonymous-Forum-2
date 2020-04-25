from flask import jsonify
from main import app


@app.route("/")
def index():
    return jsonify(
        {
            "msg": "Hello world!",
        }
    ), 200
