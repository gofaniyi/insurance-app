""" Module with email validator. """
import re

from marshmallow import ValidationError as MarshValidationError
from exception.validation import ValidationError

from api.models import User, Company
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

        email = data.get('email')
        UserValidator.validate_email_exists(email)
        

    @staticmethod
    def validate_email_exists(email):
        validate_exist(User, 'EMAIL_EXISTS', email=email)


class CompanyValidator:
    """Validate company details"""

    @classmethod
    def validate(cls, data):
        """Validate company fields"""
        
        if len(data) < 1:
            raise MarshValidationError(ERROR_MESSAGES['EMPTY_PAYLOAD'])

        CompanyValidator.validate_name_exists(data.get('email'))
        

    @staticmethod
    def validate_name_exists(name):
        validate_exist(Company, 'COMPANY_EXISTS', name=name)


def validate_exist(model, error_key, **kwargs):
    obj = model.filter(**kwargs).first()
    if obj:
        raise ValidationError(
        {
            'message': ERROR_MESSAGES[error_key]
        }, 409)

def raise_error(error_key, *args, **kwargs):
    """Raises a Marshmallow validation error

    Args:
        error_key (str): The key for accessing the correct error message
        *args: Arguments taken by the serialization error message
        **kwargs:
            fields (list): The fields where the error will appear

    Raises:
        ValidationError: Marshmallow validation error
    """
    raise MarshValidationError(ERROR_MESSAGES[error_key].format(*args),
                           kwargs.get('fields'))

def string_length_validator(length):
    """ Returns a function that checks data over a given length
    Args:
        length (Integer): Length a string must not exceed
    Returns:
        Function which validates length of the data
    """

    def length_validator(data):
        """ Checks if data does not exceed a given length
            Args:
                data (String): data to be validated
            Raises:
                validation error if data exceeds a given length
        """

        if len(data) > length:
            raise_error('string_length', length, fields=data)

    return length_validator