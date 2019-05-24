"""Test model auth module"""

# Local Modules
from api.auth import AuthToken

class TestAuthToken:
    """Tests for the authentication token helper"""

    def generate_token(self, value='sampleId'):
        return AuthToken.encode_auth_token(value)

    def test_encode_auth_token(self):
        """ tests that the method returns date in datetime format"""
        auth_token = self.generate_token()
        assert isinstance(auth_token, bytes) == True

    def test_decode_auth_token(self):
        """ tests that the method returns start of the day's date"""
        auth_token = self.generate_token()
        decoded_token = AuthToken.decode_auth_token(auth_token)
        assert decoded_token == 'sampleId'