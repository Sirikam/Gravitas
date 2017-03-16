from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Quiz, Question, Answer
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from django.urls import resolve

from apps.courses.models import Course


class QuizView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        active_page = resolve(request.path_info).url_name
        before_pages = []
        after_pages = []
        page_found = False


        context['before_pages'] = before_pages
        context['after_pages'] = after_pages
        context.update({
            'Quiz': Quiz.objects.all(),
            'Question': Question.objects.all(),
            'Answer': Answer.objects.all(),
            'Course': Course.objects.all()}
        )

        return self.render_to_response(context)