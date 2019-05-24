"""Module for users resource"""
# Third-party libraries
from flask_restplus import Resource
from flask import request

# Middlewares
from main import api
# Models
from api.models import User

# Schemas
from api.schemas.user import UserSchema
from api.views.utils import get_auth_token
from api.decorators import token_required


@api.route('/users/login')
class UserLoginResource(Resource):
    """Resource class for migrating people data into activo"""

    def post(self):
        """POST method for updating activo user table with andela personnel
        records

        Returns:
            tuple: Success response with 200 status code
        """

        request_data = request.get_json()

        user, is_authenticated = User.authenticate(
                email=request_data.get('email'), password=request_data.get('password')
              )
        if user and is_authenticated:
            return {
                'status': 'success',
                'message': 'User logged in successfully',
                'token' : user.token
            }, 200
        else:
            return {
            'status': 'fail',
            'message': 'User login attempt failed',
            'error' : 'Email or password is incorrect'
        }, 401

        

@api.route('/users/logout')
class UserLogoutResource(Resource):
    """Resource class for migrating people data into activo"""

    @token_required
    def post(self):
        """POST method for updating activo user table with andela personnel
        records

        Returns:
            tuple: Success response with 200 status code
        """
        import pdb; pdb.set_trace()
        token = get_auth_token(request)

        status = User.logout(token)

        if status:
            return {
                'status': 'success',
                'message': 'User logged out successfully',
            }, 200
        else:
            return {
            'status': 'fail',
            'message': 'User logout attempt failed',
        }, 401