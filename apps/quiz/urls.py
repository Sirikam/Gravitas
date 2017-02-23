from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
   # url(r'^professor/$', create, name='create'),
  #  url(r'^student/$', use, name='use'),
    url(r'^admin/$', views.admin, name='admin'),
]
