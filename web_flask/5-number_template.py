#!/usr/bin/python3
"""
Script that starts a Flask web application with routes:
    . /: display Hello HBNB
    . /hbnb: display HBNB
    . /c/<text>: display C followd by value of text
    . /python/<text>: display Python followed by value of text
"""
from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def print_python(text):
    """it returns python followed by the path to the url"""
    text = text.split('_')
    text = ' '.join(text)
    return ("Python {}".format(text))


@app.route("/number/<int:n>", strict_slashes=False)
def print_integer(n):
    """dynamic route"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_number_template(n):
    """it returns an HTML page with n in an H1 tag"""
    return (render_template("5-number.html", number=n))


if (__name__) == "__main__":
    app.run(port=5000, host='0.0.0.0')
