"""Test model user module"""

# Local Modules
from api.models import SuspendedToken

from tests.base import fake

from datetime import datetime as dt

class TestSuspendedModel:

    def test_save(self, init_db):
        """Test for creating a new suspended_token"""
        params = {
            'token': fake.alphanumeric(50)
        }
        suspended_token = SuspendedToken(**params)
        assert suspended_token == suspended_token.save()

    def test_get(self, init_db, new_suspended_token):
        """Test for get method"""
        assert SuspendedToken.get(new_suspended_token.id) == new_suspended_token

    def test_update(self, init_db, new_suspended_token):
        """Test for update method"""
        now = dt.utcnow()
        new_suspended_token.update(suspended_on=now)
        assert new_suspended_token.suspended_on == now

    def test_delete(self, init_db, new_suspended_token):
        """Test for delete method"""
        new_suspended_token.delete()
        assert SuspendedToken.get(new_suspended_token.id) == None

    def test_user_model_string_representation(self, init_db, new_suspended_token):
        """ Should compute the string representation of a suspended_token

        Args:
            new_suspended_token (object): Fixture to create a new suspended_token
        """
        assert repr(new_suspended_token) == f'<Token: {new_suspended_token.token}>'
