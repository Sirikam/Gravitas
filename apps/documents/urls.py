from django.conf.urls import url
from . import views
from django.conf.urls import url
from apps.documents.views import list, DocumentView

urlpatterns = [
    url(r'^$', DocumentView.as_view(template_name='documents/main.html'), name='index'),
    url(r'^tdt4180/$', DocumentView.as_view(template_name='documents/tdt4180.html'), name='tdt4180'),
    url(r'^tdt4120/$', DocumentView.as_view(template_name='documents/tdt4120.html'), name='tdt4120'),
    url(r'^tdt4145/$', DocumentView.as_view(template_name='documents/tdt4145.html'), name='tdt4145'),
    url(r'^list/$', list, name='list'),
]