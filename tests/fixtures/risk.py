
import pytest

from tests.base import fake

from api.models import Risk


@pytest.fixture(scope='module')
def new_risk(app, new_company, new_risk_type):
    params = {
        'data': {
            'firstName' : fake.first_name()
        },
        'company_id' : new_company.id,
        'risk_type_id' : new_risk_type.id
    }
    risk = Risk(**params)
    return risk.save()


@pytest.fixture(scope='module')
def new_multiple_risks(app, new_company, new_risk_type1):
    risks = []
    for each in range(3):
        params = {
            'data': {
                'firstName' : fake.first_name()
            },
            'company_id' : new_company.id,
            'risk_type_id' : new_risk_type1.id
        }
        risk = Risk(**params)
        risks.append(risk.save())
    return risks