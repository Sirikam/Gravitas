from django.conf.urls import url
from . import views
from django.conf.urls import url
from apps.documents.views import list

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tdt4180/$', views.tdt4180, name='tdt4180'),
    url(r'^tdt4120/$', views.tdt4120, name='tdt4120'),
    url(r'^tdt4145/$', views.tdt4145, name='tdt4145'),
    url(r'^list/$', list, name='list'),
]