from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/<filename>")
def render(filename):
    try: 
        return render_template(f"{filename}.html")
    except TemplateNotFound:
        return "Página não encontrada", 404