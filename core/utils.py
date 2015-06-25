from django.db.models import BigIntegerField
from random import randint


def fake_random_number():
    return randint(0, BigIntegerField.MAX_BIGINT)