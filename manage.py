"""Module with application entry point."""

# Third party Imports
import sys, click
import requests, flask_s3
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
    print('Seeding Company data')

    companies_data = [
        {'name' : 'Integrated Insurance'},
        {'name' : 'Insurance Institute'}
    ]

    users_data = [
        {'email' : 'example@sample.com', 'password' : 'example1234'},
        {'email' : 'britecore@sample.com', 'password' : 'britecore1234'}
    ]

    for index, company_data in enumerate(companies_data):
        create_entry(company_data, users_data[index])

    print('Seeded Company data')




@app.cli.command(context_settings=dict(token_normalize_func=str.lower))
def upload():
    """
    upload static files to s3

    Return:
        func: call the function if successful or the click help option if unsuccesful
    """
    print('Uploading static files to S3....')

    flask_s3.create_all(app)

    print('Uploaded static files to S3.....')

def create_entry(company_data, user_data):
    from api.models import Company, User

    try:
        company = Company(**company_data)
        company.save()

        user = User(**dict(company_id=company.id, **user_data))
        user.save()
    except Exception as e:
        print(e)
        pass

if __name__ == '__main__':
    app.run()
