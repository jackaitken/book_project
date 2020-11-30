from flask import Flask, render_template, request, redirect
import requests
import config
from helpers import listToString
import random

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return render_template("book_find.html")

@app.route('/book_find', methods=["GET", "POST"])
def book_find():
    api_key = config.api_key
    title = request.form.get('title').lower()
    author = request.form.get('author').lower()

    if not title and author:
        return render_template ("apology.html")
    else: 
        r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}&{}&key={}".format(title, author, api_key))

        # Parse response
        items = r.json()["items"]
        counter = 0
        for row in items:
            try:
                category = items[counter]["volumeInfo"]["categories"]
                counter += 1
            except KeyError:
                counter += 1
        

        return render_template("book_find.html", items = items, listToString = listToString, category = category)

@app.route('/apology', methods=["GET", "POST"])
def apology():  
    return render_template("apology.html")

@app.route('/new_book', methods=["GET", "POST"])
def new_book():
    href = request.form.get('book')
    href = requests.get("https://www.googleapis.com/books/v1/volumes?q={}".format(category))
    items = href.json()["items"]
    total_items = r.json()["totalItems"]

    random_book = items[random.randint(0, total_items)]["volumeInfo"]
    random_book_title = random_book["title"]
    random_book_author = random_book["authors"]

    return render_template("new_book.html", title = random_book_title, author = random_book_author)

