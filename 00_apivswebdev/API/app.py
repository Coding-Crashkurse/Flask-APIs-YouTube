from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)

CORS(app)

data = "Hello World"


@app.route("/")
def hello_world():
    return jsonify({"text": data})


if __name__ == "__main__":
    app.run(debug=True)

