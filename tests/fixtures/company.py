

import pytest

from tests.base import fake

from api.models import Company


@pytest.fixture(scope='module')
def new_company(app):
    params = {
        'name': fake.company(),
    }
    company = Company(**params)
    return company.save()


@pytest.fixture(scope='module')
def new_company_two(app):
    params = {
        'name': fake.company(),
    }
    company = Company(**params)
    return company.save()