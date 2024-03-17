#!/usr/bin/env python3
"""Different views for star wars api"""
from flask import Flask, render_template
from flask_cors import CORS
import uuid


app = Flask(__name__)


@app.route('/', strict_slashes=True)
def home():
    """Render landing page"""
    return render_template('index.html', cache_id=uuid.uuid4())


@app.route('/login', strict_slashes=True)
def login():
    """Render login form"""
    return render_template('login.html', cache_id=uuid.uuid4())


@app.route('/signup', strict_slashes=True)
def signup():
    """Render signup form"""
    return render_template('signup.html', cache_id=uuid.uuid4())

@app.route('/movies', strict_slashes=True)
def movie_list():
    """Cache results in redis and return the list"""
    return render_template('movies.html', cache_id=uuid.uuid4())


if __name__ =="__main__":
    """Run app"""
    app.run(host='0.0.0.0', port=5001)
