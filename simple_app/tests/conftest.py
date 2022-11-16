import pytest
from asgiref.sync import sync_to_async
from model_bakery import baker

from simple_app.models import Dev


@pytest.fixture
def random_user():
    print('fixture random_user')
    return baker.make(Dev, name='random_user')


# @pytest_asyncio.fixture
@pytest.fixture
async def a_random_user():
    print('fixture a_random_user')
    return await sync_to_async(baker.make)(Dev, name='a_random_user')


@pytest.fixture(autouse=True)
def random_user_2():
    print('fixture random_user_2')
    return baker.make(Dev, name='random_user_2')


# all non @pytest.mark.django_db(transaction=True) will persist this async fixture!
# remove all async fixtures to allow removing (transaction=True) from tests
@pytest.fixture(autouse=True)
async def a_random_user_2():
    print('fixture a_random_user_2')
    return await sync_to_async(baker.make)(Dev, name='a_random_user_2')
