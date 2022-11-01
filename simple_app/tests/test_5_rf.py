import json

import pytest
from django.test import RequestFactory, AsyncRequestFactory

from simple_app.views import s_v, a_v


@pytest.mark.django_db
def test_with_rf(random_user):
    request = RequestFactory().get('/dev/')
    response = s_v.dev(request)
    json_response = json.loads(response.content)
    assert isinstance(json_response[0], str)
    assert len(json_response) == 2


@pytest.mark.django_db
async def test_a_with_rf(a_random_user):
    request = AsyncRequestFactory().get('/adev/')
    response = await a_v.dev(request)
    json_response = json.loads(response.content)
    assert isinstance(json_response[0], str)
    assert len(json_response) == 2
