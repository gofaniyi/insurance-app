"""Module fo testing asset category models"""
import pytest

from api.models import Attribute, RiskType
from tests.base import fake


class TestRiskTypeModel:
    """Test class for the risk-type model class"""

    def test_save(self, init_db, new_company):
        """
            Test for creating a new risk-type

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_company (Company): Fixture to create a new company
        """
        params = {
            'name': fake.industry(),
            'company_id' : new_company.id
        }
        risk_type = RiskType(**params)
        assert risk_type == risk_type.save()

    def test_update(self, init_db, new_risk_type):
        """
            Test that a new risk-type gets updated

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk_type (RiskType): Fixture to create a new risk-type
        """

        new_risk_type.update(name='automobiles')

        assert new_risk_type.name == 'automobiles'


    def test_get(self, init_db, new_risk_type):
        """
            Test that a new risk-type gets fetched

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk_type (RiskType): Fixture to create a new risk-type
        """

        assert RiskType.get(new_risk_type.id) == new_risk_type


    def test_attributes(self, init_db, new_risk_type):
        """
            Test that a new risk-type gets associated with an attribute

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_risk_type (RiskType): Fixture to create a new risk-type
        """

        attribute = Attribute(
            _key='first_name',
            label='first_name',
            is_required=True,
            input_control='text',
            choices=None)

        new_risk_type.attributes.append(attribute)
        attribute.save()
        new_risk_type.save()
        assert new_risk_type.attributes[0] == attribute

    def test_model_string_representation(self, init_db, new_risk_type):
        """ Should compute the string representation of an risk-type

        Args:
            init_db(SQLAlchemy): fixture to initialize the test database
            new_risk_type (RiskType): Fixture to create a new risk-type
        """
        assert repr(new_risk_type) == f'<RiskType {new_risk_type.name}>'
