"""Module for users resource"""
# Third-party libraries
from flask_restplus import Resource
from flask import request

# Middlewares
from main import api
# Models
from api.models import Company
from api.schemas.company import CompanySchema

from api.constants.messages import SUCCESS_MESSAGES


@api.route('/companies')
class CompanyResource(Resource):
    """Resource class for company"""

    def get(self):
        """
        Gets companies list
        """
        import pdb; pdb.set_trace()
        companies = Company.filter()

        company_schema = CompanySchema(many=True)

        return (
            {
                "data": company_schema.dump(companies).data,
                "message": SUCCESS_MESSAGES["FETCHED"].format("Companies"),
                "status": "success",
            },
            200,
        )
