import os
import requests
import urllib.parse
import config
from flask import redirect, render_template, request

def bookLookUp(title, author, api_key):
    # contact API
    try:
        api_key = config.api_key
        title = request.form.get('title')
        author = request.form.get('author')
        response = requests.get("https://www.goodreads.com/book/title.xml?author={}&key={}&title={}".format(author,api_key,title)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        information = response.json()
        return {
            "average_rating": information["average_rating"],
            "ratings_sum": information["ratings_sum"]),
        }
    except (KeyError, TypeError, ValueError):
        return None

