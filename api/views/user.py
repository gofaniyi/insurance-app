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

from api.constants.messages import SUCCESS_MESSAGES, ERROR_MESSAGES


@api.route('/users/signup')
class UserSignUpResource(Resource):
    """Resource class for user signup"""

    def post(self):
        """POST method for user signup

        Returns:
            tuple: Success response with 201 status code
        """
        request_data = request.get_json()

        user_schema = UserSchema()
        user_data = user_schema.load_object_into_schema(request_data)
     
        user_data.pop('confirm_password')

        user = User(**user_data)
        user.save()

        return {
            'status': 'success',
            'message': SUCCESS_MESSAGES['USER_SIGNUP'],
            'token' : user.token,
            'user' : dict(id=user.id,email=user.email)
        }, 201



@api.route('/users/login')
class UserLoginResource(Resource):
    """Resource class for user login"""

    def post(self):
        """POST method for user login

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
                'message': SUCCESS_MESSAGES['USER_LOGIN'],
                'token' : user.token,
                'user' : dict(id=user.id,email=user.email)
            }, 200
        else:
            return {
            'status': 'fail',
            'message': ERROR_MESSAGES['USER_LOGIN'],
            'error' : ERROR_MESSAGES['INVALID_LOGIN_CREDENTIALS']
        }, 401

        

@api.route('/users/logout')
class UserLogoutResource(Resource):
    """Resource class for user logout"""

    @token_required
    def post(self):
        """POST method for user logout

        Returns:
            tuple: Success response with 200 status code
        """
        token = get_auth_token(request)

        User.logout(token)

        return {
            'status': 'success',
            'message': SUCCESS_MESSAGES['USER_LOGOUT'],
        }, 200