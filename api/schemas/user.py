""" Module with user model schemas. """

# Third Party
from marshmallow import (fields, post_load)

# Schemas
from api.schemas.base import BaseSchema, common_args
from api.schemas.utils import email_validator, UserValidator

class UserSchema(BaseSchema):
    """ User model schema. """
    email = fields.String(**common_args(validate=email_validator))

    @post_load
    def validate_fields_against_db(self, data):
        """
        Ensure id fields reference existing resource
        and email supplied is not owned by an exising user

        Arguments:
            data (dict): request body

        Raises:
            ValidationError: Used to raise exception if request body is empty
        """
        
        data['email'] = data.get('email').lower()
        UserValidator.validate(data)
