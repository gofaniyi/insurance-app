# Third Party
import re

from marshmallow import (fields, post_load)

# Schemas
from api.schemas.base import BaseSchema, common_args
from .attribute import AttributeSchema

from api.models.risk_type import RiskType

from exception.validation import ValidationError

from api.constants.messages import ERROR_MESSAGES

class RiskTypeSchema(BaseSchema):
    """Risk-type model schema"""

    name = fields.String()
    company_id = fields.Integer(
        load_only=False,
        load_from="companyId",
        dump_to="companyId")
    company = fields.Nested(
        'CompanySchema',
        dump_only=True,
        only=['id', 'name'],
        dump_to="company")

    risks = fields.Nested(
        "RiskSchema",
        many=True,
        load_from="risks",
        dump_to="risks")

    risks_count = fields.Integer(dump_to='risksCount', dump_only=True)


    @post_load
    def validate_risk_type(self, data):
        """Return risk type object after successful loading of data"""

        record_id = data.get('id')
        name = data.get('name')
        company_id = data.get('company_id')

        data.pop('id', None)  # remove id from kwargs if found or return None

        if record_id:
            result = RiskType.filter(**data).filter(
                RiskType.id == record_id).first(
                )  # selects the first query object for model records

            if result:
                return None  # return None if query object is found

        # check name column for duplications
        if name and company_id:
            result = RiskType.query.with_entities(RiskType.name)\
                .filter(RiskType.name.ilike(name), RiskType.company_id==company_id).first()

            if result and result[0].lower() == name.lower():
                raise ValidationError(
                {
                    'message': ERROR_MESSAGES['EXISTS'].format('Risk Type')
                }, 409)



class EagerLoadRiskTypeAttributesSchema(RiskTypeSchema):
    """Schema for Risk Type with eager loaded attributes"""

    custom_attributes = fields.Method(
        'get_eager_loaded_attributes',
        load_from='customAttributes',
        dump_to='customAttributes')

    def get_eager_loaded_attributes(self, obj):
        """Get serialized eager loaded attributes"""

        attribute_schema = AttributeSchema(many=True)
        return attribute_schema.dump(obj.eager_loaded_attributes).data
