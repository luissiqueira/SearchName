from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from haystack.query import SearchQuerySet

from rest_framework import generics


from .forms import EntityForm
from .models import Entity, Log
from .serializers import LogSerializer, EntitySerializer


class EntityListView(ListView):
    model = Entity
    paginate_by = 500


class EntityDetailView(DetailView):
    model = Entity

    def get(self, request, *args, **kwargs):
        from .tasks import log_read_entity
        log_read_entity.delay(self.get_object())
        return super(EntityDetailView, self).get(request, *args, **kwargs)


class EntityCreate(CreateView):
    model = Entity
    success_url = reverse_lazy('entities')
    fields = ['name']


class EntityUpdate(UpdateView):
    model = Entity
    form_class = EntityForm


class EntityDelete(DeleteView):
    model = Entity
    success_url = reverse_lazy('entities')


class LogListView(ListView):
    model = Log
    paginate_by = 500


class BaseIndexListAPIView(generics.ListAPIView):
    model = None

    def get_queryset(self):
        search_term = self.request.query_params.get('q')
        if search_term is not None and len(search_term) > 2:
            return SearchQuerySet().filter(content=search_term).models(self.model)
        else:
            return self.model.objects.none()


class EntityListAPIView(BaseIndexListAPIView):
    serializer_class = EntitySerializer
    model = Entity


class LogListAPIView(BaseIndexListAPIView):
    serializer_class = LogSerializer
    model = Log