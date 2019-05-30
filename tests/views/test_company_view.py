"""
Module of tests for company endpoints
"""
from flask import json

# app config
from config import AppConfig

from api.constants.messages import (ERROR_MESSAGES, SUCCESS_MESSAGES)

BASE_URL = AppConfig.API_BASE_URL_V1


class TestCompanyResource:

    def test_get_all_companies_succeeds(
            self, client, init_db, new_multiple_companies):
        """
        Parameters:
            client(FlaskClient): fixture to get flask test client
            init_db(SQLAlchemy): fixture to initialize the test database
            new_multiple_companies (Company): Fixture to create new companies
        """

        response = client.get(
            f'{BASE_URL}/companies')
            
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert data['status'] == 'success'
        assert data['message'] == SUCCESS_MESSAGES['FETCHED'].format('Companies')
