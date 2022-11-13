#!/usr/bin/python3
"""
it contains flask route
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """It returns Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """It return HBNB"""
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """A dynamic link that takes in a string"""
    text = text.split('_')
    text = ' '.join(text)
    return ("C {}".format(text))


if (__name__) == "__main__":
    app.run(port=5000, host='0.0.0.0')
