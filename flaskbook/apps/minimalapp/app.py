
from flask import Flask, render_template, url_for, current_app, g, request, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "yangjunmo5420"

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello"

@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello~ {name}"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]
        
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")