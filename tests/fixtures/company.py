

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


@pytest.fixture(scope='module')
def new_multiple_companies(app):
    companies = []
    for each in range(3):
        params = {
            'name': fake.company()
        }
        company = Company(**params)
        companies.append(company.save())
    return companies
