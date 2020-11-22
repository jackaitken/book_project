import requests
import config
from flask import redirect, render_template, request
import pprint

def bookLookUp(api_key, title, author):
    # contact API
        r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}&{}&key={}".format(title, author, api_key))
    # Parse response
        return r.json()


       