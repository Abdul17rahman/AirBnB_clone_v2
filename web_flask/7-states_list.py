#!/usr/bin/python3

"""
    HBNB Route that displays a list of states
"""
from models import storage
from models.state import State
from flask import Flask, abort, render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ Displays a list of states"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_req(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, port='5000', host='0.0.0.0')
