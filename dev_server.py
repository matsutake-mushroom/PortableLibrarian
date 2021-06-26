from flask import Flask, render_template, request

appname = "AI Librarian"
version = "0.0.1"

app = Flask(__name__, static_folder='img')

@app.route("/")
def index():
    return render_template("index.html", title= " ".join([appname, version]))

@app.route("/credit")
def credit():
    return render_template("credit.html", title= " ".join([appname, version]))

def welcome_message():
    return "AI司書(" + version + ") のチャットルームへようこそ！何でも話しかけてみてください！"


@app.route("/api/query", methods=["POST", "GET"])
def api_answer():
    if request.args:#GET (ping)
        if request.args["ping"]:
            return welcome_message()

    if request.form:#Chat input or API
        query = request.form["userInput"]
        return query + ": と解釈しました。返答を考えています…"

    return "test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)