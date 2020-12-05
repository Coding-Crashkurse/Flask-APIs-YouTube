from flask import Flask
from flask import render_template

app = Flask(__name__)

data = "Hello World"


@app.route("/")
def hello_world():
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
