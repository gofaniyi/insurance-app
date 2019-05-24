""" Module with email validator. """
import re

from marshmallow import ValidationError as MarshValidationError
from exception.validation import ValidationError

from api.models import User


EMAIL_REGEX = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.I | re.UNICODE)


def email_validator(data):
    """
    Checks if given string is at least 1 character and only contains characters
    that make a valid andela email.
    """

    data = data.lower()

    # Check if email pattern is matched
    if not EMAIL_REGEX.match(data):
        raise MarshValidationError('This is an invalid email address')


class UserValidator:
    """Validate user details"""

    @classmethod
    def validate(cls, data):
        """Validate user fields against database"""
        if len(data) < 1:
            raise MarshValidationError('No valid field(s) in request body')

        email = data.get('email')
        user = User.get_by_email(email=email)
        if user:
            raise ValidationError(
            {
                'message': 'email already exist'
            }, 409)

