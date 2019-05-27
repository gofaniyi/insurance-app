"""Test model user module"""

# Local Modules
from api.models import SuspendedToken

from tests.base import fake

from datetime import datetime as dt

class TestSuspendedTokenModel:

    def test_save(self, init_db):
        """Test for creating a new suspended_token
        
            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
        """
        params = {
            'token': fake.alphanumeric(50)
        }
        suspended_token = SuspendedToken(**params)
        assert suspended_token == suspended_token.save()

    def test_get(self, init_db, new_suspended_token):
        """Test for get method

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_suspended_token (SuspendedToken): Fixture to create a new suspended token
        """
        assert SuspendedToken.get(new_suspended_token.id) == new_suspended_token

    def test_update(self, init_db, new_suspended_token):
        """Test for update method

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_suspended_token (SuspendedToken): Fixture to create a new suspended token
        """
        now = dt.utcnow()
        new_suspended_token.update(suspended_on=now)
        assert new_suspended_token.suspended_on == now

    def test_delete(self, init_db, new_suspended_token):
        """Test for delete method

            Args:
                init_db(SQLAlchemy): fixture to initialize the test database
                new_suspended_token (SuspendedToken): Fixture to create a new suspended token
        """
        new_suspended_token.delete()
        assert SuspendedToken.get(new_suspended_token.id) == None

    def test_model_string_representation(self, init_db, new_suspended_token):
        """ Should compute the string representation of a suspended token

        Args:
            init_db(SQLAlchemy): fixture to initialize the test database
            new_suspended_token (SuspendedToken): Fixture to create a new suspended token
        """
        assert repr(new_suspended_token) == f'<Token: {new_suspended_token.token}>'
