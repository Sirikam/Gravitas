from django.conf.urls import url
from . import views
from django.conf.urls import url
from apps.documents.views import list, DocumentView, DocumentCourse_view

urlpatterns = [
    url(r'^$', DocumentView.as_view(template_name='documents/main.html'), name='index'),
    url(r'^list/$', list, name='list'),
    url(r'^(?P<course_id>[0-9]+)/$', DocumentCourse_view, name='DocCourseView')
]