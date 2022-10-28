import json
import string
from datetime import datetime
from random import choice, randint

from django.core import serializers

from simple_app.models import Dev


def create_random_string():
    return ''.join(choice(string.ascii_letters) for _ in range(randint(10, 20)))


def read():
    resp = json.loads(serializers.serialize("json", Dev.objects.all()))
    resp.insert(0, create_random_string())
    return resp


def create(dev_dict):
    new_dev = Dev(name=dev_dict["name"], age=dev_dict["age"], level=dev_dict["level"])
    new_dev.full_clean()
    new_dev.save()
    return {"saved": serializers.serialize("json", [new_dev])},


def delete(pk):
    Dev.objects.filter(pk=pk).delete()


def read_slow():
    start = datetime.now()

    young_devs = json.loads(serializers.serialize("json", Dev.objects.filter(age__gte=20, age__lte=30)))
    a_devs = json.loads(serializers.serialize("json", Dev.objects.filter(name__icontains='a')))
    not_junior_devs = json.loads(serializers.serialize("json", Dev.objects.exclude(level='junior')))

    print('total', (datetime.now() - start).total_seconds())

    return {
        "young_devs": young_devs,
        "a_devs": a_devs,
        "not_junior_devs": not_junior_devs,
    }
