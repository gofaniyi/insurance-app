import pytest

from tests.base import fake

from api.models import User


@pytest.fixture(scope='module')
def new_user(app, new_company):
    params = {
        'company_id'  : new_company.id,
        'email': fake.email(),
        'password' : fake.password()
    }
    user = User(**params)
    return user.save()


@pytest.fixture(scope='module')
def user_one(app, new_company):
    params = {
        'company_id' : new_company.id,
        'email': fake.email(),
        'password' : 'samplePassword1234!@#$'
    }
    user = User(**params)
    return user.save()
