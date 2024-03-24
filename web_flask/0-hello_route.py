#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function to return Hellow HBNB"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0, port='5000')
