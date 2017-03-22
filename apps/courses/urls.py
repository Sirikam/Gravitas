from django.conf.urls import url
from .views import CourseView,view
from .models import Course

urlpatterns = [
    url(r'^$', CourseView.as_view(template_name='courses/admin.html'), name='admin'),
    url(r'^(?P<course_id>[0-9]+)/$', view, name='template')
]