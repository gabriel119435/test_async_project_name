from django.db import models


class Level(models.TextChoices):
    jr = "junior"
    md = "middle"
    sn = "senior"


class Dev(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    level = models.CharField(max_length=6, choices=Level.choices)
