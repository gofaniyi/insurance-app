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

        
