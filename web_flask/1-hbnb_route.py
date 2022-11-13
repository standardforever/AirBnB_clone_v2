#!/usr/bin/python3
"""
. script that starts a Flask web application
. The web application is listening on 0.0.0.0, port 5000
. Routes:
    . /: display (Hello HBNB!)
    . /hbnb: display (HBNB)
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

if (__name__) == "__main__":
    app.run(port=5000, host='0.0.0.0')
