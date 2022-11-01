import pytest
from asgiref.sync import sync_to_async

from simple_app.models import Dev
from simple_app.services import a_svc, s_svc


@pytest.mark.django_db
def test_delete_sync(random_user):
    assert Dev.objects.filter(pk=random_user.pk).exists()
    s_svc.delete(random_user.pk)
    assert not Dev.objects.filter(pk=random_user.pk).exists()


@pytest.mark.django_db
def test_delete_sync_with_a(a_random_user):
    print(f'a_random_user type: {type(a_random_user)}')
    assert Dev.objects.filter(pk=a_random_user.pk).exists()
    s_svc.delete(a_random_user.pk)
    assert not Dev.objects.filter(pk=a_random_user.pk).exists()


# @pytest.mark.asyncio
@pytest.mark.django_db
async def test_async():
    a = Dev(name='a', age=1, level="junior")
    await sync_to_async(a.save)()
    assert await sync_to_async(Dev.objects.filter(pk=a.pk).exists)()
    await a_svc.delete(a.pk)
    assert not await sync_to_async(Dev.objects.filter(pk=a.pk).exists)()


@pytest.mark.django_db
async def test_async_with_a_fixture(a_random_user):
    print(f'a_random_user type: {type(a_random_user)}')
    assert await sync_to_async(Dev.objects.filter(pk=a_random_user.pk).exists)()
    await a_svc.delete(a_random_user.pk)
    assert not await sync_to_async(Dev.objects.filter(pk=a_random_user.pk).exists)()


# async test with sync fixture hangs the test
@pytest.mark.django_db
async def not_a_test_async_with_s_fixture(random_user):
    print(random_user.pk)
    await sync_to_async(random_user.save)()
    print(await Dev.objects.all().acount())
    assert await sync_to_async(Dev.objects.filter(pk=random_user.pk).exists)()
    await a_svc.delete(random_user.pk)
    assert not await sync_to_async(Dev.objects.filter(pk=random_user.pk).exists)()
