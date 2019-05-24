"""
Module of tests for user endpoints
"""
from flask import json

# app config
from config import AppConfig

BASE_URL = AppConfig.API_BASE_URL_V1

from mock.user import USER_ONE_VALID_PASSWORD, INVALID_PASSWORD


class TestUserView:
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
        assert data['message'] == 'User logged in successfully'

    
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
        assert data['message'] == 'User login attempt failed'
        assert data['error'] == 'Email or password is incorrect'

    
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
        assert data['message'] == 'User login attempt failed'
        assert data['error'] == 'Email or password is incorrect'
    