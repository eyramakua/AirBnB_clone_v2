#!/usr/bin/python3
"""
starts a web flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function to return Hellow HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function to return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """function to display C"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    """display python texts"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num_display(n):
    """display n is the number"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
