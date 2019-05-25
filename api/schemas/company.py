""" Module with user model schemas. """

# Third Party
from marshmallow import (fields, post_load)

# Schemas
from api.schemas.base import BaseSchema, common_args
from api.schemas.utils import CompanyValidator

class CompanySchema(BaseSchema):
    """ Company model schema. """
    
    name = fields.String(**common_args())

    @post_load
    def is_valid(self, data):
        """
        Ensure id fields reference existing resource
        and name supplied is not owned by an exising company

        Arguments:
            data (dict): request body

        Raises:
            ValidationError: Used to raise exception if request body is empty
        """
        CompanyValidator.validate(data)
