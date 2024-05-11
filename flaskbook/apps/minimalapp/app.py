from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello"

@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello~ {name}"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

