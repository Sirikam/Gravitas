from django.conf.urls import url
from .views import CourseView

urlpatterns = [
    url(r'^$', CourseView.as_view(template_name='courses/admin.html'), name='admin'),
]