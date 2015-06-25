# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Data da \xc3\xbaltima modifica\xc3\xa7\xc3\xa3o')),
                ('number', models.BigIntegerField(default=core.utils.fake_random_number, serialize=False, verbose_name=b'N\xc3\xbamero', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Entidade',
                'verbose_name_plural': 'Entidades',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Data de cria\xc3\xa7\xc3\xa3o')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Data da \xc3\xbaltima modifica\xc3\xa7\xc3\xa3o')),
                ('entity_key', models.CharField(max_length=30, verbose_name=b'Chave da entidade')),
                ('kind', models.CharField(max_length=6, verbose_name=b'Tipo de log')),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
            ],
            options={
                'ordering': ('-modified_at',),
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]
