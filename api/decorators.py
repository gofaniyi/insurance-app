# Standard library
from functools import wraps

from flask import request

import jwt
from api.views.utils import get_auth_token
from api.auth import AuthToken


def token_required(func):
    """Authentication decorator. Validates token from the client

    Args:
        func (function): Function to be decorated

    Returns:
        function: Decorated function

    Raises:
        ValidationError: Validation error
    """

    @wraps(func)
    def decorated_function(*args, **kwargs):
        
        token = get_auth_token(request)
        decoded_token = AuthToken.decode_auth_token(token)
        # setting the payload to the request object and can be accessed with \
        # request.decoded_token from the view
        setattr(request, 'decoded_token', decoded_token)

        return func(*args, **kwargs)

    return decorated_function
