import string
from random import choice, randint

from django.core.management import BaseCommand

from simple_app.models import Level, Dev


class Command(BaseCommand):
    def handle(self, *args, **options):
        devs = [
            Dev(
                name=create_random_string(),
                age=randint(20, 50),
                level=choice(Level.choices)[0]
            ) for _ in range(20000)
        ]
        Dev.objects.bulk_create(devs)


def create_random_string():
    return ''.join(choice(string.ascii_letters) for _ in range(randint(5, 15)))
