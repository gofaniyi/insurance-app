""" Module with email validator. """
import re

from marshmallow import ValidationError as MarshValidationError
from exception.validation import ValidationError

from api.models import User
from api.constants.messages import ERROR_MESSAGES





def email_check(value):
    """
    Checks if given string is at least 1 character and only contains characters
    that make a valid andela email.
    """

    EMAIL_REGEX = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.I | re.UNICODE)

    value = value.lower()

    # Check if email pattern is matched
    if not EMAIL_REGEX.match(value):
        raise MarshValidationError(ERROR_MESSAGES['INVALID_EMAIL'])

def password_check(value):

    PASSWORD_REGEX = re.compile(
        r'[A-Za-z0-9@#$%^&+=]{8,}', re.I | re.UNICODE)

    if not PASSWORD_REGEX.match(value):
        raise MarshValidationError(ERROR_MESSAGES['NOT_STRONG_PASSWORD'])

class UserValidator:
    """Validate user details"""

    @classmethod
    def validate(cls, data):
        """Validate user fields"""
        
        if len(data) < 1:
            raise MarshValidationError(ERROR_MESSAGES['EMPTY_PAYLOAD'])

        UserValidator.validate_passwords(data.get('password'), data.get('confirm_password'))

        email = data.get('email')
        UserValidator.validate_email_exists(email)
        

    @staticmethod
    def validate_email_exists(email):
        user = User.get_by_email(email=email)
        if user:
            raise ValidationError(
            {
                'message': ERROR_MESSAGES['EMAIL_EXISTS']
            }, 409)

    @staticmethod
    def validate_passwords(password, confirm_password):
        if password != confirm_password:
            raise ValidationError(
            {
                'message': ERROR_MESSAGES['PASSWORDS_MISMATCH']
            }, 400)