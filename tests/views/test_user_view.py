"""
Module of tests for user endpoints
"""
from flask import json

# app config
from config import AppConfig

from mock.user import USER_ONE_VALID_PASSWORD, INVALID_PASSWORD

from tests.base import fake
from api.constants.messages import (ERROR_MESSAGES, SUCCESS_MESSAGES)

BASE_URL = AppConfig.API_BASE_URL_V1




class TestUserLoginResource:
    """
    Tests endpoint for adding person to a center
    """

    def test_can_login_with_right_credentials_succeeds(
            self, client, init_db, user_one):
        """
        Should return an 200 status code and new user data when data provided
        in request is valid
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """

        response = client.post(
            f'{BASE_URL}/users/login',
            data=json.dumps(dict(email=user_one.email, password=USER_ONE_VALID_PASSWORD)), content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['message'] == SUCCESS_MESSAGES['USER_LOGIN']

    
    def test_can_login_with_wrong_password_fails(
            self, client, init_db, user_one):
        """
        Should return an 200 status code and new user data when data provided
        in request is valid
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """
        
        response = client.post(
            f'{BASE_URL}/users/login',
            data=json.dumps(dict(email=user_one.email, password=INVALID_PASSWORD)), content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'fail'
        assert data['message'] == ERROR_MESSAGES['USER_LOGIN']
        assert data['error'] == ERROR_MESSAGES['INVALID_LOGIN_CREDENTIALS']

    
    def test_can_login_with_wrong_email_fails(
            self, client, init_db, user_one):
        """
        Should return an 200 status code and new user data when data provided
        in request is valid
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """
        
        response = client.post(
            f'{BASE_URL}/users/login',
            data=json.dumps(dict(email='wrong@samle.com', password=USER_ONE_VALID_PASSWORD)), content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'fail'
        assert data['message'] == ERROR_MESSAGES['USER_LOGIN']
        assert data['error'] == ERROR_MESSAGES['INVALID_LOGIN_CREDENTIALS']
    

class TestUserLogoutResource:

    def test_user_logout_with_valid_token_succeeds(
            self, client, init_db, user_one):
        """
        Should return an 200 status code and new user data when data provided
        in request is valid
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """
        response = client.post(
            f'{BASE_URL}/users/logout', 
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ))

        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['message'] == SUCCESS_MESSAGES['USER_LOGOUT']

    def test_user_logout_with_invalid_token_fails(
            self, client, init_db):
        """
        Should return an 200 status code and new user data when data provided
        in request is valid
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """
        response = client.post(
            f'{BASE_URL}/users/logout', 
            headers=dict(
                Authorization=f'Bearer {fake.alphanumeric(50)}'
            ))

        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['JWT_INVALID_TOKEN']