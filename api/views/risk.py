"""Module for users resource"""
# Third-party libraries
from flask_restplus import Resource
from flask import request

# Middlewares
from main import api
# Models
from api.models import Risk
from api.schemas.risk import RiskSchema

from api.constants.messages import SUCCESS_MESSAGES
from api.decorators import token_required


@api.route('/risks')
class RiskResource(Resource):
    """Resource class for risks"""

    @token_required
    def get(self):
        """
        Gets risks list
        """
        risks = Risk.filter()

        risk_schema = RiskSchema(many=True)

        return (
            {
                "data": risk_schema.dump(risks).data,
                "message": SUCCESS_MESSAGES["FETCHED"].format("Risks"),
                "status": "success",
            },
            200,
        )


    @token_required
    def post(self):
        """
        POST method for creating risks.

        """
        request_data = request.get_json()

        request_data['companyId'] = request.decoded_token.get('sub').get('company')['id']

        risk_schema = RiskSchema()
        risk_data = risk_schema.load_object_into_schema(
            request_data)

        risk = Risk(**risk_data)

        risk = risk.save()

        return {
            'status': 'success',
            'message': SUCCESS_MESSAGES['CREATED'].format('Risk'),
            'data' : risk_schema.dump(risk).data
        }, 201