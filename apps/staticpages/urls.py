from django.conf.urls import url
from .views import StaticView

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', StaticView.as_view(template_name='staticpages/login.html'), name='login'),
    url(r'^homepage/$', StaticView.as_view(template_name='staticpages/homepage.html'), name='homepage'),
    url(r'^schedule/$', StaticView.as_view(template_name='staticpages/schedule.html'), name='schedule')
]