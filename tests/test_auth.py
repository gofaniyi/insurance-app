"""Test model auth module"""
from pytest import raises

# Local Modules
from api.auth import AuthToken
from exception.validation import ValidationError
from api.constants.messages import ERROR_MESSAGES

class TestAuthToken:
    """Tests for the authentication token helper"""

    def generate_token(self, value='sampleId', days=1):
        return AuthToken.encode_auth_token(value, days=days)

    def generate_expired_token(self):
        return self.generate_token(days=-1)

    def test_encode_auth_token(self):
        auth_token = self.generate_token()
        assert isinstance(auth_token, str) == True

    def test_decode_auth_token(self, init_db):
        auth_token = self.generate_token()
        decoded_token = AuthToken.decode_auth_token(auth_token)
        assert decoded_token['sub'] == 'sampleId'

    def test_decode_expired_token_fails(self, init_db):
        auth_token = self.generate_expired_token()
        with raises(ValidationError) as error:
            decoded_token = AuthToken.decode_auth_token(auth_token)
        exception = error.value
        assert exception.status_code == 401
        assert exception.error['message'] == ERROR_MESSAGES['JWT_EXPIRED_TOKEN']
        
        