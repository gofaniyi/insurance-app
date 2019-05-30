

import pytest

from tests.base import fake

from api.models import RiskType, Attribute


@pytest.fixture(scope='module')
def new_risk_type(app, new_company):
    params = {
        'name': fake.industry(),
        'company_id' : new_company.id
    }
    risk_type = RiskType(**params)
    return risk_type.save()


@pytest.fixture(scope='module')
def new_risk_type1(app, new_company):
    params = {
        'name': fake.industry(),
        'company_id' : new_company.id
    }
    risk_type = RiskType(**params)
    return risk_type.save()

@pytest.fixture(scope='module')
def new_risk_type_with_attribute(app, new_company):
    params = {
        'name': fake.industry(),
        'company_id' : new_company.id
    }
    risk_type = RiskType(**params)
    risk_type = risk_type.save()

    attribute = Attribute(
            _key='model',
            label='model',
            is_required=False,
            input_control='text',
            choices='choice')
    risk_type.attributes.append(attribute)
    return risk_type.save()

@pytest.fixture(scope='module')
def new_risk_type_with_attribute1(app, new_company):
    params = {
        'name': fake.industry(),
        'company_id' : new_company.id
    }
    risk_type = RiskType(**params)
    risk_type = risk_type.save()

    attribute = Attribute(
            _key='branch',
            label='branch',
            is_required=False,
            input_control='text',
            choices='choice')
    risk_type.attributes.append(attribute)
    return risk_type.save()



@pytest.fixture(scope='module')
def new_company_two_risk_type(app, new_company_two):
    params = {
        'name': fake.industry(),
        'company_id' : new_company_two.id
    }
    risk_type = RiskType(**params)
    return risk_type.save()


@pytest.fixture(scope='module')
def new_multiple_risk_types(app, new_company):
    risk_types = []
    for each in range(2):
        params = {
                'name': fake.industry(),
                'company_id' : new_company.id
        }
        risk_type = RiskType(**params)
        risk_types.append(risk_type.save())