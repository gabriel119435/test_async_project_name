import asyncio
import json
import string
from datetime import datetime
from random import choice, randint

from asgiref.sync import sync_to_async
from django.core import serializers

from simple_app.models import Dev
from simple_app.services import s_svc


async def create_random_string():
    await asyncio.sleep(1)
    return ''.join(choice(string.ascii_letters) for _ in range(randint(10, 20)))


async def read():
    resp = json.loads(await sync_to_async(serializers.serialize)("json", Dev.objects.all()))
    resp.insert(0, await create_random_string())
    return resp


@sync_to_async
def create(dev_dict):
    new_dev = Dev(name=dev_dict["name"], age=dev_dict["age"], level=dev_dict["level"])
    new_dev.full_clean()
    new_dev.save()
    return {"saved": serializers.serialize("json", [new_dev])},


@sync_to_async
def delete(pk):
    Dev.objects.filter(pk=pk).delete()


async def a_read_slow():
    return await sync_to_async(s_svc.read_slow)()


async def read_slow_but_better():
    start = datetime.now()

    young_devs, ab_devs, not_junior_devs = await asyncio.gather(
        a_serialize(Dev.objects.filter(age__gte=20, age__lte=30)),
        a_serialize(Dev.objects.filter(name__icontains='ab')),
        a_serialize(Dev.objects.exclude(level='junior')),
    )
    print('total', (datetime.now() - start).total_seconds())
    return {
        "young_devs": young_devs,
        "ab_devs": ab_devs,
        "not_junior_devs": not_junior_devs,
    }


async def a_serialize(qs):
    return json.loads(await sync_to_async(serializers.serialize)("json", qs))
