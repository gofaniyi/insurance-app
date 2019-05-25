"""
Module of tests for risk-type endpoints
"""
from flask import json

# app config
from config import AppConfig

from tests.base import fake
from api.constants.messages import (ERROR_MESSAGES, SUCCESS_MESSAGES)

BASE_URL = AppConfig.API_BASE_URL_V1


class TestRiskTypeResource:

    def test_create_risk_type_with_valid_data_succeeds(
            self, client, init_db, user_one):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
        """
        payload = {
            'name' : fake.industry(),
            'customAttributes' : [
                {
                    "label": "brand",
                    "isRequired": True,
                    "inputControl": "text",
                    'key': 'brand',
                }, 
                {
                    "label": "color",
                    "isRequired": True,
                    "inputControl": "dropdown",
                    "choices": ["blue", "red", "black"],
                    'key': 'color'
                }
            ] 
        }

        response = client.post(
            f'{BASE_URL}/risk-types', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert data['status'] == 'success'
        assert data['message'] == SUCCESS_MESSAGES['RISK_TYPE_CREATED']



    def test_create_risk_type_with_existing_company_risk_type_fails(
            self, client, init_db, user_one, new_risk_type):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_risk_type (RiskType): Fixture to create a new risk type
        """

        payload = {
            'name' : new_risk_type.name,
            'customAttributes' : [
                {
                    "label": "brand",
                    "isRequired": True,
                    "inputControl": "text",
                    'key': 'brand',
                }, 
                {
                    "label": "color",
                    "isRequired": True,
                    "inputControl": "dropdown",
                    "choices": ["blue", "red", "black"],
                    'key': 'color'
                }
            ] 
        }

        response = client.post(
            f'{BASE_URL}/risk-types', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 409
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['EXISTS'].format('Risk Type')



    def test_create_risk_type_with_incomplete_request_body_fails(
            self, client, init_db, user_one):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
        """

        payload = {
            'name' : 'sampleIndustry',
        }

        response = client.post(
            f'{BASE_URL}/risk-types', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['PROVIDE_CUSTOM_ATTRIBUTES']


    def test_create_risk_type_with_different_company_risk_type_succeeds(
            self, client, init_db, user_one, new_risk_type, new_company_two_risk_type):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_risk_type (RiskType): Fixture to create a new risk type
            new_company_two_risk_type (RiskType): Fixture to create a new risk type
        """
        new_company_two_risk_type.name = 'insurance'
        new_company_two_risk_type.save()

        payload = {
            'name' : new_company_two_risk_type.name,
            'customAttributes' : [
                {
                    "label": "brand",
                    "isRequired": True,
                    "inputControl": "text",
                    'key': 'brand',
                }, 
                {
                    "label": "color",
                    "isRequired": True,
                    "inputControl": "dropdown",
                    "choices": ["blue", "red", "black"],
                    'key': 'color'
                }
            ] 
        }

        response = client.post(
            f'{BASE_URL}/risk-types', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')

        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert data['status'] == 'success'
        assert data['message'] == SUCCESS_MESSAGES['RISK_TYPE_CREATED']


    def test_create_risk_type_with_no_authorization_succeeds(
            self, client, init_db):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """
        payload = {
            'name' : fake.industry(),
            'customAttributes' : [
                {
                    "label": "brand",
                    "isRequired": True,
                    "inputControl": "text",
                    'key': 'brand',
                }, 
                {
                    "label": "color",
                    "isRequired": True,
                    "inputControl": "dropdown",
                    "choices": ["blue", "red", "black"],
                    'key': 'color'
                }
            ] 
        }

        response = client.post(
            f'{BASE_URL}/risk-types', 
            data=json.dumps(payload),
            content_type='application/json')
        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['JWT_INVALID_TOKEN']


    def test_get_all_risk_types_succeeds(
            self, client, init_db, user_one, new_multiple_risk_types):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_multiple_risk_types (RiskType): Fixture to create a new risk type
        """

        response = client.get(
            f'{BASE_URL}/risk-types', 
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ))

        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['message'] == SUCCESS_MESSAGES['FETCHED'].format('Risk Types')

    
    def test_get_all_risk_types_without_authentication_fails(
            self, client, init_db):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """

        response = client.get(
            f'{BASE_URL}/risk-types')

        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['JWT_INVALID_TOKEN']


class TestSingleRiskTypeResource:

    def test_get_a_risk_type_without_authentication_fails(
            self, client, init_db):
        """
        Args:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """

        response = client.get(
            f'{BASE_URL}/risk-types/2212910')
        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['JWT_INVALID_TOKEN']


    def test_get_a_risk_type_invalid_id_fails(
            self, client, init_db, user_one):
        """
        Args:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
        """

        response = client.get(
            f'{BASE_URL}/risk-types/2212910', 
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ))
        data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['NOT_FOUND'].format('Risk type')


    def test_get_a_risk_type_succeeds(
            self, client, init_db, user_one, new_risk_type):
        """
        Args:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_risk_type (RiskType): Fixture to create a new risk type
        """

        response = client.get(
            f'{BASE_URL}/risk-types/{new_risk_type.id}', 
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ))
            
        response_json = json.loads(response.data.decode())
        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert response_json['message'] == SUCCESS_MESSAGES['FETCHED'].format('Risk Type')
        data = response_json['data']
        assert data['name'] == new_risk_type.name
        assert data['id'] == new_risk_type.id

        #Assert that you can only retrieve risk types under your company
        assert data['companyId'] == user_one.company_id


    def test_update_a_risk_type_with_no_authorization_succeeds(
            self, client, init_db):
        """
        Args:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
        """
        payload = {
            'name' : fake.industry(),
            'customAttributes' : [
                {
                    "label": "brand",
                    "isRequired": True,
                    "inputControl": "text",
                    'key': 'brand',
                }, 
                {
                    "label": "color",
                    "isRequired": True,
                    "inputControl": "dropdown",
                    "choices": ["blue", "red", "black"],
                    'key': 'color'
                }
            ] 
        }

        response = client.put(
            f'{BASE_URL}/risk-types/29293', 
            data=json.dumps(payload),
            content_type='application/json')
        data = json.loads(response.data.decode())
        assert response.status_code == 401
        assert data['status'] == 'error'
        assert data['message'] == ERROR_MESSAGES['JWT_INVALID_TOKEN']


    def test_update_a_risk_type_with_valid_data_succeeds(
            self, client, init_db, user_one, new_risk_type):
        """
        Args:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_risk_type (RiskType): Fixture to create a new risk type
        """
        payload = {
            'name' : 'updated_industry',
            'customAttributes' : [
                {
                    "label": "brand",
                    "isRequired": True,
                    "inputControl": "text",
                    'key': 'brand',
                }, 
                {
                    "label": "color",
                    "isRequired": True,
                    "inputControl": "dropdown",
                    "choices": ["blue", "red", "black"],
                    'key': 'color'
                }
            ] 
        }

        response = client.put(
            f'{BASE_URL}/risk-types/{new_risk_type.id}', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')

        response_json = json.loads(response.data.decode())
        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert response_json['message'] == SUCCESS_MESSAGES['UPDATED'].format('Risk type')

        data = response_json['data']
        assert data['name'] == 'updated_industry'
        assert data['customAttributes'][0]['key'] == 'brand' or 'color'



    def test_update_a_risk_type_with_only_attributes_succeeds(
            self, client, init_db, user_one, new_risk_type_with_attribute):
        """
        Args:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            user_one (User): Fixture to create a new user
            new_risk_type_with_attribute (Risk Type): Fixture to create a new risk
        """
        payload = {
            'customAttributes' : [
                {
                    "label": "brand",
                    "isRequired": True,
                    "inputControl": "text",
                    'key': 'brand',
                }, 
                {
                    "label": "color",
                    "isRequired": True,
                    "inputControl": "dropdown",
                    "choices": ["blue", "red", "black"],
                    'key': 'color'
                }
            ] 
        }

        response = client.put(
            f'{BASE_URL}/risk-types/{new_risk_type_with_attribute.id}', 
            data=json.dumps(payload),
            headers=dict(
                Authorization=f'Bearer {user_one.token}'
            ),
            content_type='application/json')

        response_json = json.loads(response.data.decode())
        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert response_json['message'] == SUCCESS_MESSAGES['UPDATED'].format('Risk type')
        
        data = response_json['data']
        assert data['id'] == new_risk_type_with_attribute.id
        assert data['name'] == new_risk_type_with_attribute.name
        assert len(data['customAttributes']) == 3