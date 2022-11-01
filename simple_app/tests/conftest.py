import pytest
import pytest_asyncio
from asgiref.sync import sync_to_async
from model_bakery import baker

from simple_app.models import Dev


@pytest.fixture
def random_user():
    print('random_user')
    return baker.make(Dev)


# @pytest_asyncio.fixture
@pytest.fixture
async def a_random_user():
    return await sync_to_async(baker.make)(Dev)
