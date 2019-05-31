""" Module with user model schemas. """

# Third Party
from marshmallow import (fields,post_load,)

# Schemas
from api.schemas.base import BaseSchema

from exception.validation import ValidationError
from sqlalchemy.orm import load_only

from api.constants.messages import ERROR_MESSAGES

class RiskSchema(BaseSchema):
    """ Company model schema. """
    
    data = fields.Dict(
        load_from="data", dump_to="data")

    risk_type_id = fields.Integer(
        load_from="riskTypeId",
        dump_to="riskTypeId")

    company_id = fields.Integer(
        load_only=False,
        load_from="companyId",
        dump_to="companyId")
    company = fields.Nested(
        'CompanySchema',
        dump_only=True,
        only=['id', 'name'],
        dump_to="company")


    @post_load
    def validate_risk_data(self, data):
        """Return risk data object after successful loading of data"""
       
        risk_type_id = data.get('risk_type_id')


        data = data.get('data')

        from api.models.risk_type import RiskType
        
        
        risk_type = RiskType.get(risk_type_id)

        if not risk_type:
            raise ValidationError(
                {
                    'message': ERROR_MESSAGES['EXISTS'].format('Risk Type')
                }, 400)

        attributes = risk_type.attributes.all()

        errors = {}
        for attribute in attributes:
            if not attribute.is_required and attribute._key not in data:
                errors[attribute._key] = ERROR_MESSAGES['ATTRIBUTE_NOT_FOUND']

        attribute_keys = [attribute._key for attribute in attributes]
        
        for key, value in data.items():
            if key not in attribute_keys:
                errors[key] = ERROR_MESSAGES['ATTRIBUTE_NOT_RELATED_1'].format(risk_type.name)
        
        if errors:
            raise ValidationError(
            {
                'message': ERROR_MESSAGES['BAD_DATA_ATTRIBUTE'],
                'error' : errors
            }, 400)


    @staticmethod
    def collate_attribute_not_related_errors():
        
