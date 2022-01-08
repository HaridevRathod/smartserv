from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.defaults import patterns, url


urlpatterns = [
    url(r'^/$', views.login, name='login'),
    url(r'^dasboard/$', views.dasboard, name='dasboard'),
]