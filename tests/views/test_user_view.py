"""
Module of tests for user endpoints
"""
from flask import json

# app config
from config import AppConfig

from mock.user import USER_ONE_VALID_PASSWORD, INVALID_PASSWORD

from tests.base import fake
from api.constants.messages import (ERROR_MESSAGES, SUCCESS_MESSAGES)

from api.auth import AuthToken

BASE_URL = AppConfig.API_BASE_URL_V1


class TestUserSignUpResource:

    """
    Tests endpoint for signing/registering a user
    """

    def test_user_signup_with_valid_data_succeeds(
        self, client, init_db, new_company):
        """
            Parameters:
                client(FlaskClient): fixture to get flask test client
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """
        payload = {
            'company_id' : new_company.id,
            'email' : fake.email(),
            'password' : USER_ONE_VALID_PASSWORD,
            'confirm_password' : USER_ONE_VALID_PASSWORD
        }

        response = client.post(
            f'{BASE_URL}/users/signup',
            data=json.dumps(payload), content_type='application/json')

        response_json = json.loads(response.data.decode())
        assert response.status_code == 201
        assert response_json['status'] == 'success'
        assert response_json['message'] == SUCCESS_MESSAGES['USER_SIGNUP']

        data = response_json['data']

        assert AuthToken.decode_auth_token(data['token']) is not None

        assert data['user']['id'] is not None
        assert data['user']['email'] == payload['email']

        assert data['user']['company']['id'] == new_company.id
        assert data['user']['company']['name'] == new_company.name

    
    def test_user_signup_with_non_matching_passwords_fails(
        self, client, init_db, new_company):
        """
            Parameters:
                client(FlaskClient): fixture to get flask test client
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """

        #payload with passwords not matching
        payload = {
            'company_id' : new_company.id,
            'email' : fake.email(),
            'password' : USER_ONE_VALID_PASSWORD,
            'confirm_password' : INVALID_PASSWORD
        }

        response = client.post(
            f'{BASE_URL}/users/signup',
            data=json.dumps(payload), content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['PASSWORDS_MISMATCH']


    def test_user_signup_with_invalid_email_address_fails(
        self, client, init_db, new_company):
        """
            Parameters:
                client(FlaskClient): fixture to get flask test client
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """

        #payload with invalid email address
        payload = {
            'company_id' : new_company.id,
            'email' : fake.first_name(),
            'password' : USER_ONE_VALID_PASSWORD,
            'confirm_password' : USER_ONE_VALID_PASSWORD
        }

        response = client.post(
            f'{BASE_URL}/users/signup',
            data=json.dumps(payload), content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['DEFAULT']
        assert data['errors'] == dict(email=[ERROR_MESSAGES['INVALID_EMAIL']])


    def test_user_signup_with_empty_request_body_fails(
        self, client, init_db):
        """
            Parameters:
                client(FlaskClient): fixture to get flask test client
                init_db(SQLAlchemy): fixture to initialize the test database
        """

        #empty payload
        payload = {}

        response = client.post(
            f'{BASE_URL}/users/signup',
            data=json.dumps(payload), content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['DEFAULT']
        assert data['errors'] == dict(email=[ERROR_MESSAGES['REQUIRED_FIELD']], password=[ERROR_MESSAGES['REQUIRED_FIELD']])



    def test_user_signup_with_existing_email_address_fails(
        self, client, init_db, user_one):
        """
            Parameters:
                client(FlaskClient): fixture to get flask test client
                init_db(SQLAlchemy): fixture to initialize the test database
                user_one (User): Fixture to create a new user
        """

        #payload with invalid email address
        payload = {
            'company_id' : user_one.company_id,
            'email' : user_one.email,
            'password' : USER_ONE_VALID_PASSWORD,
            'confirm_password' : USER_ONE_VALID_PASSWORD
        }

        response = client.post(
            f'{BASE_URL}/users/signup',
            data=json.dumps(payload), content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 409
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['EMAIL_EXISTS']


    
    def test_user_signup_with_not_strong_password_fails(
        self, client, init_db, new_company):
        """
            Parameters:
                client(FlaskClient): fixture to get flask test client
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """

        #payload with not strong password
        payload = {
            'company_id' : new_company.id,
            'email' : fake.email(),
            'password' : 'pass',
            'confirm_password' : 'pass'
        }

        response = client.post(
            f'{BASE_URL}/users/signup',
            data=json.dumps(payload), content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['DEFAULT']
        assert data['errors'] == dict(password=[ERROR_MESSAGES['NOT_STRONG_PASSWORD']])



class TestUserLoginResource:
    """
    Tests endpoint for a user to login
    """

    def test_can_login_with_right_credentials_succeeds(
            self, client, init_db, user_one):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
        """

        response = client.post(
            f'{BASE_URL}/users/login',
            data=json.dumps(dict(email=user_one.email, password=USER_ONE_VALID_PASSWORD)), 
            content_type='application/json')

        response_json = json.loads(response.data.decode())
        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert response_json['message'] == SUCCESS_MESSAGES['USER_LOGIN']

        data = response_json['data']
        assert data['token'] is not None
        assert user_one.id == AuthToken.decode_auth_token(data['token'])['sub']['id']

        assert data['user']['id'] == user_one.id
        assert data['user']['email'] == user_one.email

        assert data['user']['company']['id'] == user_one.company.id
        assert data['user']['company']['name'] == user_one.company.name

    
    def test_can_login_with_wrong_password_fails(
            self, client, init_db, user_one):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
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
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
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
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
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