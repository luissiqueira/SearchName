# coding=utf-8
from __future__ import absolute_import

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
from django.db import IntegrityError
from core.models import Log, Entity

import random
import requests


@shared_task
def log_create_entity(entity):
    """
    :param entity: Uma instância de core.models.Entity
    :type entity: core.models.Entity
    """
    log = Log(entity_key=entity.number, kind=Log.CREATE)
    log.description = 'Name: %s' % entity.name
    log.save()


@shared_task
def log_read_entity(entity):
    """
    :param entity: Uma instância de core.models.Entity
    :type entity: core.models.Entity
    """
    log = Log(entity_key=entity.number, kind=Log.READ)
    log.description = 'Name: %s' % entity.name
    log.save()


@shared_task
def log_update_entity(entity, old_values):
    """
    :type entity: core.models.Entity
    :type old_values: dict
    """
    log = Log(entity_key=entity.number, kind=Log.UPDATE)
    old_name = old_values['name'] if 'name' in old_values else ''
    log.description = 'Old name: %s\nNew name: %s' % (old_name, entity.name)
    log.save()


@shared_task
def log_delete_entity(entity):
    """
    :param entity: Uma instância de core.models.Entity
    :type entity: core.models.Entity
    """
    log = Log(entity_key=entity.number, kind=Log.DELETE)
    log.description = 'Name: %s' % entity.name
    log.save()


@periodic_task(run_every=crontab(minute="*/2"))
def import_names():
    response = requests.get('http://uinames.com/api/names.json').json()

    for idx in range(0, 3):
        country = random.choice(response)
        genre = random.choice(["male", "female"])
        name = random.choice(country[genre])
        surname = random.choice(country["surnames"])
        full_name = '%s %s' % (name, surname)

        try:
            Entity.objects.create(name=full_name)
        except IntegrityError:
            print 'Number previously created'

    print 'import_names finished'