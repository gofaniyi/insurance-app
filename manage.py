"""Module with application entry point."""

# Third party Imports
import sys, click
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
    if AppConfig.DEBUG:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


@app.route('/bus')
def template():
    """Checks the health of application and returns 'Health App Server' as json."""
    return render_template("index.html")

@app.route('/health')
def health_check():
    """Checks the health of application and returns 'Health App Server' as json."""
    return jsonify(dict(message='Healthy App Server')), 200

@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def seed():
    """
    Seeds the database with sample data

    Return:
        func: call the function if successful or the click help option if unsuccesful
    """
    g.seed = 'seeding'
    print('Seeding Company data')

    from api.models import Company
    data = [
        {'name' : 'Nigeria Insurance'},
    ]

    user_data = [
        {'email' : 'example@sample.com'},
        {'email' : 'britecore@sample.com'}
    ]
    try:
        company = Company(**data)
        company.save()


    except:
        pass
    print('Seeded Company data')

if __name__ == '__main__':
    app.run()
