"""Test model user module"""

# Local Modules
from api.models import Company

from tests.base import fake

class TestCompanyModel:

    def test_save(self, init_db):
        """Test for creating a new company
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
        """
        params = {
            'name': fake.company()
        }
        company = Company(**params)
        assert company == company.save()

    def test_get(self, init_db, new_company):
        """Test for get method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """
        assert Company.get(new_company.id) == new_company

    def test_update(self, init_db, new_company):
        """Test for update method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """
        company_name = fake.company()
        new_company.update(name=company_name)
        assert new_company.name == company_name

    def test_delete(self, init_db, new_company):
        """Test for delete method
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """
        new_company.delete()
        assert Company.get(new_company.id) == None

    def test_model_string_representation(self, init_db, new_company):
        """ Should compute the string representation of a company

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """
        assert repr(new_company) == f'<Company: {new_company.name}>'
