from django.conf.urls import url
from . import views
<<<<<<< HEAD
=======
from django.conf.urls import url
from apps.documents.views import list
>>>>>>> 6d78dea3fafa37899db67f031ab7e089efe59f1b

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tdt4180/$', views.tdt4180, name='tdt4180'),
    url(r'^tdt4120/$', views.tdt4120, name='tdt4120'),
<<<<<<< HEAD
    url(r'^tdt4145/$', views.tdt4145, name='tdt4145')
=======
    url(r'^tdt4145/$', views.tdt4145, name='tdt4145'),
    url(r'^list/$', list, name='list'),
>>>>>>> 6d78dea3fafa37899db67f031ab7e089efe59f1b
]