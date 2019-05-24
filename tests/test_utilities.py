from api.views.utils import get_auth_token
from tests.base import fake

token = fake.alphanumeric(30)

class RequestMock:

    @property
    def headers(self):
        return dict(Authorization=f'Bearer {token}')

request = RequestMock()

class TestUtilities:
    
    def test_get_auth_token(self):
        """ tests that the method returns date in datetime format"""
        auth_token = get_auth_token(request)
        assert auth_token == token