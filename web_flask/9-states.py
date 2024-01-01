#!/usr/bin/python3

"""
    HBNB Route that displays a list of states
"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Displays a list of states"""
    states = list(storage.all(State).values())
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_with_id(id):
    """ Display single state"""
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            found_state = state
    return render_template('9-states.html', state=found_state)


@app.teardown_appcontext
def teardown_req(exception=None):
    """ Closes the session after the request """
    storage.close()


if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0')
