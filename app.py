from flask import Flask, render_template, request, redirect
import requests
import config
import pprint

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return render_template("book_find.html")

@app.route('/book_find', methods=["GET", "POST"])
def test():
    api_key = config.api_key
    title = request.form.get('title')
    author = request.form.get('author')
    
    # contact API
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}&{}&key={}".format(title, author, api_key))
    
    # Parse response
    parsed_response = r.json()

    published_year = '3000'
    items = parsed_response["items"]
    counter = 0

    for entry in items:
        year = items[counter]["volumeInfo"]["publishedDate"]
        if title = items[counter]["volumeInfo"]["title"]
            if year < published_year:
                published_year = year
                book_to_parse = items[counter]["volumeInfo"]
                counter += 1
            else:
                counter += 1

    print(book_to_parse)
    print(published_year)

    return render_template("book_find.html", book_to_parse = book_to_parse, published_year = published_year)
