from unittest import mock

import pytest

from simple_app.services import s_svc, a_svc


@pytest.mark.django_db
@mock.patch("simple_app.services.s_svc.create_random_string", return_value=False)
def test_mock(mocked_method_above):
    assert not s_svc.read()[0]


@pytest.mark.django_db
@mock.patch("simple_app.services.a_svc.create_random_string", return_value=False)
async def test_mock_async(mocked_method_above):
    assert not (await a_svc.read())[0]
