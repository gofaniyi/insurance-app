"""Module for users resource"""
# Third-party libraries
from flask_restplus import Resource
from flask import request, jsonify

# Middlewares
from main import api
# Models
from api.models import RiskType

# Schemas
from api.schemas import RiskTypeSchema, RiskSchema, AttributeSchema, EagerLoadRiskTypeAttributesSchema
from api.decorators import token_required

from api.constants.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

from exception.validation import ValidationError
from .utils import parse_attributes_data


@api.route("/risk-types")
class RiskTypeResource(Resource):
    """
    Resource class for creating and getting risk types
    """

    @token_required
    def post(self):
        """
        POST method for creating risk-types.

        Payload should have the following parameters:
            name(str): name of the risk-type
        """

        request_data = request.get_json()

        request_data['companyId'] = request.decoded_token.get('sub').get('company')['id']

        risk_type_schema = RiskTypeSchema()
        risk_type_data = risk_type_schema.load_object_into_schema(
            request_data)

        risk_type = RiskType(**risk_type_data)

        attributes_data = request_data.get('customAttributes')

        if attributes_data:
            attributes_schema = AttributeSchema(
                many=True, exclude=['id'])

            attributes = attributes_schema.load_object_into_schema(
                attributes_data)
            risk_type.attributes = attributes
            attributes = attributes_schema.dump(attributes).data
        else:
            raise ValidationError(
                {'message': ERROR_MESSAGES['PROVIDE_CUSTOM_ATTRIBUTES']})

        risk_type = risk_type.save()

        return {
            'status': 'success',
            'message': SUCCESS_MESSAGES['RISK_TYPE_CREATED'],
            'data' : risk_type_schema.dump(risk_type).data
        }, 201

    @token_required
    def get(self):
        """
        Gets risk-type list
        """

        risk_types = RiskType.filter(company_id=request.decoded_token.get('sub').get('company')['id'])

        risk_type_schema = EagerLoadRiskTypeAttributesSchema(many=True)

        return (
            {
                "data": risk_type_schema.dump(risk_types).data,
                "message": SUCCESS_MESSAGES["FETCHED"].format("Risk Types"),
                "status": "success",
            },
            200,
        )



@api.route('/risk-types/<int:risk_type_id>')
class SingleRiskTypeResource(Resource):
    """Resource class for carrying out operations on a single risk type"""

    @token_required
    def get(self, risk_type_id):
        """
        Get a single risk type
        """

        risk_type = RiskType.get_or_404(risk_type_id)

        return (
            {
                "data": EagerLoadRiskTypeAttributesSchema().dump(risk_type).data,
                "message": SUCCESS_MESSAGES["FETCHED"].format("Risk Type"),
                "status": "success",
            },
            200,
        )

    @token_required
    def delete(self, risk_type_id):
        """
        Delete a single risk type
        """

        risk_type = RiskType.get_or_404(risk_type_id)

        risk_type.delete()

        return (
            {
                "message": SUCCESS_MESSAGES["DELETED"].format("Risk Type"),
                "status": "success",
            },
            200,
        )

    @token_required
    def put(self, risk_type_id):
        """
        Updates risk type and the corresponding attributes
        """

        risk_type = RiskType.get_or_404(risk_type_id)
        request_data = request.get_json()
        
        request_data['id'] = risk_type.id

        risk_type_schema = RiskTypeSchema()
        risk_type_data = risk_type_schema.load_object_into_schema(
            request_data, partial=True)

        attributes_data = request_data.get('customAttributes')
        attributes_schema = AttributeSchema(many=True)

        if attributes_data:
            attributes_schema_data = attributes_schema.load_object_into_schema(
                attributes_data, partial=True) 

            parse_attributes_data(risk_type, attributes_schema_data,
                                  risk_type_id)

        risk_type.update(**risk_type_data)

        attributes = attributes_schema.dump(
            risk_type.attributes.all()).data
        risk_type_data = risk_type_schema.dump(risk_type).data

        response = jsonify({
            "status": 'success',
            "message": SUCCESS_MESSAGES['UPDATED'].format('Risk type'),
            "data": {
                **risk_type_data, "customAttributes": attributes
            }
        })

        response.status_code = 200
        return response


@api.route('/risk-types/<int:risk_type_id>/risks')
class SingleRiskTypeRisksResource(Resource):
    """Resource class for carrying out operations on a single risk type"""

    @token_required
    def get(self, risk_type_id):
        """
        Get a single risk type risks
        """
        
        risk_type = RiskType.get_or_404(risk_type_id)

        risks = risk_type.risks.all()

        risk_schema = RiskSchema(many=True)

        return (
            {
                "data": risk_schema.dump(risks).data,
                "message": SUCCESS_MESSAGES["FETCHED"].format("Risks"),
                "status": "success",
            },
            200,
        )