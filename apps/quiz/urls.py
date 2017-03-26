from django.conf.urls import url
from apps.quiz.views import *


urlpatterns = [
    url(r'^$', index, name='quiz_categories'),
    url(r'^category/(?P<category_id>\d+)', view_category, name='quiz_category'),
    url(r'^take/(?P<quiz_id>[0-9]+)/$', quiz_take, name='quiz_take'),

]
