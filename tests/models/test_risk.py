"""Test model user module"""

# Local Modules
from api.models import Risk

from tests.base import fake

class TestRiskModel:

    def test_save(self, init_db, new_company, new_risk_type):
        """Test for creating a new risk
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
                new_risk_type (RiskType): Fixture to create a new risk type
        """
        params = {
            'data': {},
            'risk_type_id': new_risk_type.id,
            'company_id': new_company.id
        }
        risk = Risk(**params)
        assert risk == risk.save()

    def test_get(self, init_db, new_risk):
        """Test for get method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk (Risk): Fixture to create a new risk
        """
        assert Risk.get(new_risk.id) == new_risk

    def test_update(self, init_db, new_risk):
        """Test for update method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk (Risk): Fixture to create a new risk
        """
        data = {
            'firstName' : fake.first_name(),
            'lastName' : fake.last_name()
        }
        new_risk.update(data=data)
        assert new_risk.data == data

    def test_delete(self, init_db, new_risk):
        """Test for delete method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk (Risk): Fixture to create a new risk
        """
        new_risk.delete()
        assert Risk.get(new_risk.id) == None

    def test_model_string_representation(self, init_db, new_risk):
        """ Should compute the string representation of a risk

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk (Risk): Fixture to create a new risk
        """
        assert repr(new_risk) == f'<Risk>'
