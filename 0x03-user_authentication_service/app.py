#!/usr/bin/env python3
"""
Flask app
"""
from flask import (
    Flask,
    request,
    jsonify,
    abort,
    redirect,
    url_for
)

from auth import Auth

app = Flask(__name__)
AUTH = Auth()




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
