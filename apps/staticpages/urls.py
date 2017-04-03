from django.conf.urls import url
from .views import StaticView, logout_view

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'staticpages/login.html'}, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^homepage/$', StaticView.as_view(template_name='staticpages/homepage.html'), name='homepage'),
    url(r'^schedule/$', StaticView.as_view(template_name='staticpages/schedule.html'), name='schedule'),
    url(r'^contact/$', StaticView.as_view(template_name='staticpages/contact.html'), name='contact')
]