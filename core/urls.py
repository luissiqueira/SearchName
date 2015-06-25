from django.conf.urls import url
from core.views import EntityListView, EntityDetailView, EntityUpdate, EntityDelete, EntityCreate
from core.views import LogListView

urlpatterns = [
    url(r'^records/$', EntityListView.as_view(), name='entities'),
    url(r'^records/create$', EntityCreate.as_view(), name='entity-create'),
    url(r'^records/(?P<pk>[-\w]+)$', EntityDetailView.as_view(), name='entity-detail'),
    url(r'^records/(?P<pk>[-\w]+)/edit$', EntityUpdate.as_view(), name='entity-edit'),
    url(r'^records/(?P<pk>[-\w]+)/delete', EntityDelete.as_view(), name='entity-delete'),

    url(r'^log/$', LogListView.as_view(), name='logs'),
]