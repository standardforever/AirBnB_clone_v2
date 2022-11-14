#!/usr/bin/python3
"""
Displaying object from database
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """Close session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_state():
    """return the list of state"""
    state = storage.all(State).values()
    return(render_template("7-states_list.html", state_list=state))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 