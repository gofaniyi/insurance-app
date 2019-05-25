""" Module for base marshmallow schema. """
from marshmallow import Schema, fields

from exception.validation import ValidationError

from api.constants.messages import ERROR_MESSAGES


class BaseSchema(Schema):
    """Base marshmallow schema with common attributes."""
    
    id = fields.Integer(dump_only=True)

    created_at = fields.DateTime(dump_only=True, dump_to='createdAt')
    updated_at = fields.DateTime(dump_only=True, dump_to='updatedAt')

    def load_json_into_schema(self, data):
        """Helper function to load raw json request data into schema"""
        data, errors = self.loads(data)

        BaseSchema.raise_errors(errors)

        return data

    def load_object_into_schema(self, data, partial=False):
        """Helper function to load python objects into schema"""
        data, errors = self.load(data, partial=partial)

        BaseSchema.raise_errors(errors)

        return data

    @staticmethod
    def raise_errors(errors):
        if errors:
            raise ValidationError(
                dict(errors=errors, message=ERROR_MESSAGES['DEFAULT']), 400)


def common_args(**kwargs):
    """ Returns the common arguments used in marshmallow fields.
    Args:
        kwargs: key word arguments use in fields
        ie validate=some_function

    Returns:
        dict: Resultant fields to be passed to a schema

    """

    return {
        "required": True,
        "validate": kwargs.get('validate'),
        "error_messages": {
            'required': ERROR_MESSAGES['REQUIRED_FIELD']
        }
    }