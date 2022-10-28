from random import choice, randint

from django.core.management import BaseCommand

from simple_app.models import Level, Dev
from simple_app.services.s_svc import create_random_string


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
