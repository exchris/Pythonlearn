#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# importing flask module
from flask import Flask

# initializing a variable of flask
app = Flask(__name__)

# decorationg index function with the app.route
@app.route('/')
def index():
    return "WELCOME!!! This is the home page."


if __name__ == "__main__":
    app.run(debug=True)