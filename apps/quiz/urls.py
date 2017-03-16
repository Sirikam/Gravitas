from django.conf.urls import url
from .views import QuizView

urlpatterns = [
    url(r'^$', QuizView.as_view(template_name='quiz/main.html'), name='index'),
   # url(r'^professor/$', QuizView.as_view(template_name='professor/main.html'), name='create'),
  #  url(r'^student/$', QuizView.as_view(template_name='quiz/student.html'), name='use'),
    url(r'^admin/$', QuizView.as_view(template_name='quiz/admin.html'), name='admin'),
]
