from haystack import indexes

from .models import Log, Entity


class EntityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, model_attr='name')
    name = indexes.CharField(model_attr='name')
    number = indexes.IntegerField(model_attr='number')
    modified_at = indexes.DateTimeField(model_attr='modified_at')

    def get_model(self):
        return Entity

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def get_updated_field(self):
        return "modified_at"


class LogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, model_attr='description')
    entity_key = indexes.CharField(model_attr='entity_key')
    kind = indexes.CharField(model_attr='kind')
    description = indexes.CharField(model_attr='description')
    modified_at = indexes.DateTimeField(model_attr='modified_at')

    def get_model(self):
        return Log

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def get_updated_field(self):
        return "modified_at"