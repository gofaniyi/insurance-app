"""
Module of tests for risk endpoints
"""
from flask import json

# app config
from config import AppConfig

from api.constants.messages import (ERROR_MESSAGES, SUCCESS_MESSAGES)

from tests.base import fake

BASE_URL = AppConfig.API_BASE_URL_V1


class TestRiskResource:

    def test_get_all_risks_succeeds(
            self, client, init_db, user_one, new_multiple_risks):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_multiple_risks (Risk): Fixture to create new risks
        """

        response = client.get(
            f'{BASE_URL}/risks', 
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),)
            
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['message'] == SUCCESS_MESSAGES['FETCHED'].format('Risks')


    def test_get_all_risk_without_authentication_fails(
            self, client, init_db):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """

        response = client.get(
            f'{BASE_URL}/risks')

        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['JWT_INVALID_TOKEN']


    def test_create_risk_with_valid_data_succeeds(
            self, client, init_db, user_one, new_risk_type_with_attribute):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_risk_type_with_attribute (RiskType): Fixture to create a new risk type
        """
        payload = {
            'data': {
                'model' : fake.alphanumeric(10),
            },
            'riskTypeId' : new_risk_type_with_attribute.id
        }

        response = client.post(
            f'{BASE_URL}/risks', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')
            
        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert data['status'] == 'success'
        assert data['message'] == SUCCESS_MESSAGES['CREATED'].format('Risk')


    def test_create_risk_with_invalid_risk_type_fails(
            self, client, init_db, user_one):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
        """
        payload = {
            'data': {
                'firstName' : fake.first_name(),
            },
            'riskTypeId' : 'sampleId'
        }

        response = client.post(
            f'{BASE_URL}/risks', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['status'] == 'error'


    def test_create_risk_with_missing_data_structure_fails(
            self, client, init_db, user_one, new_risk_type_with_attribute):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_risk_type_with_attribute (RiskType): Fixture to create a new risk type
        """
        payload = {
            'data': {
                'firstName' : fake.first_name(),
            },
            'riskTypeId' : new_risk_type_with_attribute.id
        }

        response = client.post(
            f'{BASE_URL}/risks', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['status'] == 'error'

    def test_create_risk_with_invalid_data_structure_fails(
            self, client, init_db, user_one, new_risk_type_with_attribute):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_risk_type_with_attribute (RiskType): Fixture to create a new risk type
        """
        payload = {
            'data': {
                'firstName' : fake.first_name(),
                'model' : 'NAS1344'
            },
            'riskTypeId' : new_risk_type_with_attribute.id
        }

        response = client.post(
            f'{BASE_URL}/risks', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['status'] == 'error'


    def test_create_risk_with_no_authorization_fails(
            self, client, init_db):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """
        payload = {
        }

        response = client.post(
            f'{BASE_URL}/risks', 
            data=json.dumps(payload),
            content_type='application/json')
        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['JWT_INVALID_TOKEN']
