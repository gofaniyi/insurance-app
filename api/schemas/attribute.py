# Third party libraries
from marshmallow import (fields, post_load, post_dump,
                         validates_schema, ValidationError)

from api.constants.messages import ERROR_MESSAGES
from enum import Enum

# Schemas
from api.schemas.base import BaseSchema, common_args
from api.schemas.utils import string_length_validator
from humps.camel import case

from api.models.attribute import Attribute



class InputControlChoiceEnum(Enum):
    """
    Input controls enums
    """

    TEXTAREA = "textarea"
    TEXT = "text"
    NUMBER = "number"
    DROPDOWN = "dropdown"
    CHECKBOX = "checkbox"
    RADIOBUTTON = "radio button"
    DATE = "date"

    @classmethod
    def get_multichoice_fields(cls):
        return [cls.DROPDOWN.value, cls.CHECKBOX.value, cls.RADIOBUTTON.value]

    @classmethod
    def get_singlechoice_fields(cls):
        return [cls.TEXTAREA.value, cls.TEXT.value, cls.DATE.value, cls.NUMBER.value]

    @classmethod
    def get_all_choices(cls):
        return cls.get_multichoice_fields() + cls.get_singlechoice_fields()


def input_control_validation(value):
    """Check that the supplied input_control is one of the accepted types"""

    input_controls = InputControlChoiceEnum.get_all_choices()
    if value.lower() not in input_controls:
        raise ValidationError(ERROR_MESSAGES['INPUT_CONTROL'].format(
            input_controls=str(input_controls).strip('[]')))



def validate_choices_after_dump(data):
    """
    Checks if choices should be returned to the client.

    if the input control is not a multi-choice type,
    then the choices are not returned to the client,
    else the choices is converted into an array and returned to the client

    (data)dict: attributes data

    Returns: None
    """

    if not data['choices'] or data['choices'] == ['']:
        del data['choices']
    else:
        data['choices'] = data['choices'][0].split(',')


def remove_duplicate(choices):
    """
    Remove duplicates from choices
    """

    unique_choices = []
    for choice in choices:
        choice = choice.strip()
        if choice and choice.lower() not in unique_choices:
            unique_choices.append(choice.lower())

    return unique_choices


def validate_multi_choice(input_control, choices):
    """ Validates if the input_control is in the list of choices or not

    Args:
        input_control: the value to be tested
        choices: the list of values to be tested against

    Raises:
        MarshError: if the input_control is multi_choice does not exist in the
        choices list
    """
    multi_choices = InputControlChoiceEnum.get_multichoice_fields()
    if input_control in multi_choices and not choices: 
        raise ValidationError(ERROR_MESSAGES['CHOICES_REQUIRED'], 'choices')
    return


def validate_choices(data):
    """
    Validates if choices is required or not
    """
    input_control = data.get('input_control', ''). lower()

    choices = data.get('choices', [])

    choices = ','.join(remove_duplicate(choices))
    single_choices = InputControlChoiceEnum.get_singlechoice_fields()
    data['choices'] = choices

    if input_control:
        # Raises an Exception if input_control is a multichoice and choices are empty
        validate_multi_choice(input_control, choices)

        # Raises an Exception if input_control is not a multichoice
        if input_control in single_choices and choices: 
            data['choices'] = ''
    # When updating, input_control filed may not be provided in request body
    else:
        # In that case, we want to ignore choices in the request body
        del data['choices']


class AttributeSchema(BaseSchema):
    """Attribute model schema"""

    _key = fields.String(load_from='label', dump_to='key')

    label = fields.String(**common_args(validate=(string_length_validator(60))))
    is_required = fields.Boolean(
        required=True,
        load_from='isRequired',
        dump_to='isRequired',
        error_messages={'required': ERROR_MESSAGES['REQUIRED_FIELD']})
    input_control = fields.String(
        **common_args(validate=(string_length_validator(60),input_control_validation)),
        load_from='inputControl',
        dump_to='inputControl')
    choices = fields.List(fields.String(validate=string_length_validator(60)))

    @validates_schema
    def validate_choice_decorator(self, data):
        return validate_choices(data)

    @post_load
    def create_attribute(self, data):
        """Return attribute object after successful loading into schema"""
        
        # When updating, `label` may not be provided in request's body.
        if data.get('_key'):
            data['_key'] = case(data['_key'])

        if not data.get('id'):
            return Attribute(**data)
        return data

    @post_dump
    def dump_attribute(self, data):
        """
        Return attribute object after successful dumping as array of strings
        """
        return validate_choices_after_dump(data)