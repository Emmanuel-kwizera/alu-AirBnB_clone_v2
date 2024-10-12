#!/usr/bin/python3

"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Comment"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Comment"""
    return "HBNB"


@app.route('/c/<text>')
def text_var(text):
    """Comment"""
    no_underscore = text.replace('_', ' ')
    return "C {}".format(no_underscore)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_route_python(text="is cool"):
    """Comment"""
    no_underscore = text.replace('_', ' ')
    return "Python {}".format(no_underscore)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
