""" Module with user model schemas. """

# Third Party
from marshmallow import (fields, post_load)

# Schemas
from api.schemas.base import BaseSchema, common_args
from api.schemas.utils import email_check, password_check, UserValidator


class UserSchema(BaseSchema):
    """ User model schema. """
    email = fields.String(**common_args(validate=email_check))
    password = fields.String(**common_args(validate=password_check))
    confirm_password = fields.String()
    company_id = fields.Integer(
        load_from='companyId',
        load_only=True, dump_to="companyId",)
    company = fields.Nested(
        'CompanySchema', only=['id', 'name'], dump_to="company")

    @post_load
    def is_valid(self, data):
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
