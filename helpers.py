import requests
import config
from flask import redirect, render_template, request
import random

def bookLookUp(api_key, title, author):
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}&{}&key={}".format(title, author, api_key))
    
    # Parse response
    parsed_response = r.json()
    items = parsed_response["items"]

    # Set local variables
    published_year = '3000'
    counter = 0

    # iterate through entries in API call
    for entry in items:
        year = items[counter]["volumeInfo"]["publishedDate"]
        if title == items[counter]["volumeInfo"]["title"]:
            if year < published_year:
                published_year = year
                book_to_parse = items[counter]["volumeInfo"]
                counter += 1
            else:
                counter += 1

    return book_to_parse


def listToString(s):
    seperator = ", "

    return seperator.join(s)

    

    

    


       