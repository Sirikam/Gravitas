from django.conf.urls import url
from . import views

urlpatterns = [
    # /users/
    url(r'^$', views.index, name='index'),
    #/users/id_nr/
    url(r'^(<person_id>[0-9]+)$',views.detail, name='detail')

]