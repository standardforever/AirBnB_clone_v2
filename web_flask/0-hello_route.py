#!/usr/bin/python3
"""
. A flask web application that listening on 0.0.0.0,
port 5000
. Routes:
    . /: display (Hello HBNB!)
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """It returns Hello HBNB"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
