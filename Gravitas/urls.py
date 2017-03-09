"""Gravitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from apps.staticpages.views import index
from django.conf.urls import include, url
from django.views.generic import RedirectView #for den siste funskjonen


urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^staticpages/', include('apps.staticpages.urls', namespace='staticpages')),
    url(r'^quiz/', include('apps.quiz.urls', namespace='quiz')),
    url(r'^progressbar/', include('apps.progressbar.urls', namespace='progressbar')),
    url(r'^upload/', include('apps.upload.urls', namespace='upload')),
    url(r'^users/',include('apps.users.urls', namespace='users')),
    url(r'^courses/', include('apps.courses.urls')),
    url(r'^documents/', include('apps.documents.urls', namespace='documents')),

    url(r'^$', RedirectView.as_view(url='/documents/list/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

