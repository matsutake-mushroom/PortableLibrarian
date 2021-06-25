from flask import Flask, render_template

appname = "AI Librarian"
version = "0.0.1"

app = Flask(__name__, static_folder='img')

@app.route("/")
def index():
    return render_template("index.html", title= " ".join([appname, version]))

@app.route("/credit")
def credit():
    return render_template("credit.html", title= " ".join([appname, version]))

@app.route("/api/query", methods=["POST"])
def api_answer():
    return "test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)