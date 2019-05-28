"""Module with application entry point."""

# Third party Imports
import sys
import requests
from os import environ

import click
from flask import jsonify, render_template, g, request
from sqlalchemy import text

# Local Imports
from main import create_app
from config import config, AppConfig
from api.database import db

# create application object
app = create_app(AppConfig)



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


@app.route('/health')
def health_check():
    """Checks the health of application and returns 'Health App Server' as json."""
    return jsonify(dict(message='Healthy App Server')), 200

if __name__ == '__main__':
    app.run()
