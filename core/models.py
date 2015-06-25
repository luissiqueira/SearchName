# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models

from .utils import fake_random_number


class BaseModel(models.Model):
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    modified_at = models.DateTimeField('Data da última modificação', auto_now=True)

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super(BaseModel, cls).from_db(db, field_names, values)
        # customization to store the original field values on the instance
        instance._loaded_values = dict(zip(field_names, values))
        return instance

    class Meta:
        abstract = True


class Entity(BaseModel):
    number = models.BigIntegerField('Número', default=fake_random_number, primary_key=True)
    name = models.CharField('Nome', max_length=255)

    def save(self, *args, **kwargs):
        from .tasks import log_create_entity, log_update_entity

        if self._state.adding:
            log_create_entity.delay(self)
        else:
            log_update_entity.delay(self, self._loaded_values)

        super(Entity, self).save(*args, **kwargs)

    def delete(self, **kwargs):
        from .tasks import log_delete_entity

        log_delete_entity.delay(self)
        super(Entity, self).delete(**kwargs)

    def get_absolute_url(self):
        return reverse('entity-detail', kwargs={'pk': self.number})

    def __unicode__(self):
        return '%s - %d' % (self.name, self.number)

    class Meta:
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'
        ordering = ('name',)


class Log(BaseModel):
    CREATE, READ, UPDATE, DELETE = 'CREATE', 'READ', 'UPDATE', 'DELETE'

    KIND_CHOICES = (
        (CREATE, CREATE),
        (READ,   READ),
        (UPDATE, UPDATE),
        (DELETE, DELETE)
    )

    entity_key = models.CharField('Chave da entidade', max_length=30)
    kind = models.CharField('Tipo de log', max_length=6)
    description = models.TextField('Descrição')

    def __unicode__(self):
        return '%s - %s' % (self.entity_key, self.kind)

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
        ordering = ('-modified_at',)