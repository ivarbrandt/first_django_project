from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<val>\d+)$', views.show),
    url(r'^(?P<val1>\d+)/edit$', views.edit),
    url(r'^(?P<val2>\d+)/delete$', views.destroy),
]