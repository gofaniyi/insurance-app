


import pytest

from tests.base import fake

from api.models.attribute import Attribute


@pytest.fixture(scope='module')
def new_attribute(app, new_risk_type):
    params = dict(
        _key='model',
        label='model',
        is_required=True,
        input_control='text',
        choices=None,
        risk_type_id=new_risk_type.id
    )
    attribute = Attribute(**params)
    return attribute.save()