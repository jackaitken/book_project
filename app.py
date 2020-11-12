from flask import Flask, render_template, request, redirect
import config
import helpers

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        title = request.form.get('title')
        author = request.form.get('author')


    
