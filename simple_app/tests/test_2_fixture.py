import os

import pytest
from asgiref.sync import sync_to_async
from django.conf import settings as _settings
from model_bakery import baker

from simple_app.models import Dev


@pytest.fixture(autouse=True)
def set_anything_to_everyone(settings):
    settings.PUDIM_URL = "http://www.pudim.com.br"


@pytest.fixture
def user_a_name():
    Dev(name='a', age=1, level="junior").save()


@pytest.fixture
def user_b_name_with_baker():
    open("test_file_to_be_deleted", 'w').close()
    yield baker.make(Dev, name='b')
    os.remove("test_file_to_be_deleted")


@pytest.mark.django_db(transaction=True)
def test_with_models(user_a_name, user_b_name_with_baker, random_user):
    print(f'autouse: {_settings.PUDIM_URL}')
    print(user_a_name, user_b_name_with_baker, random_user)
    Dev(name='a', age=2, level="middle").save()
    Dev(name='c', age=3, level="senior").save()
    a_devs = Dev.objects.filter(name='a').count()
    total = Dev.objects.all().count()
    print(list(Dev.objects.values_list('name', flat=True)))
    assert a_devs == 2
    assert total == 7


@pytest.mark.django_db(transaction=True)
async def test_with_models_a(random_user):
    total = await Dev.objects.all().acount()
    await sync_to_async(print)('names', Dev.objects.values_list('name', flat=True))
    assert total == 3
