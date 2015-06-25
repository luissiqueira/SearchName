"""searchname URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from core import urls as core_urls
from core.views import LogListAPIView, EntityListAPIView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^core/', include(core_urls)),

    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),

    url(r'^api/logs/$', LogListAPIView.as_view(), name='api_logs'),
    url(r'^api/entities/$', EntityListAPIView.as_view(), name='api_entities'),
]
