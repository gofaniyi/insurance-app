

import pytest

from tests.base import fake

from api.models import SuspendedToken


@pytest.fixture(scope='module')
def new_suspended_token(app):
    params = {
        'token': fake.alphanumeric(50),
    }
    suspended_token = SuspendedToken(**params)
    return suspended_token.save()