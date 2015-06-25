from rest_framework.serializers import ModelSerializer

from .models import Entity, Log


class EntitySerializer(ModelSerializer):
    class Meta:
        model = Entity
        fields = ['number', 'name']


class LogSerializer(ModelSerializer):
    class Meta:
        model = Log
        fields = ['entity_key', 'kind', 'description']