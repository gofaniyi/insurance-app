"""Module with application entry point."""

# Third party Imports
import sys
from os import environ

import click
from flask import jsonify, render_template, g
from sqlalchemy import text

# Local Imports
from main import create_app
from config import config, AppConfig
from api.database import db

# create application object
app = create_app(AppConfig)


@app.route('/')
def index():
    return jsonify(dict(message='Welcome to the Insurance API'))


@app.route('/health')
def health_check():
    """Checks the health of application and returns 'Health App Server' as json."""
    return jsonify(dict(message='Healthy App Server')), 200

if __name__ == '__main__':
    app.run()
