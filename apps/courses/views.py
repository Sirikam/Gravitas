from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Course
from apps.documents.models import Document
from apps.users.models import User
from apps.quiz.models import Quiz, Question, Answer
from apps.users.models import Person

from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from django.urls import resolve

# Create your views here.


class CourseView(TemplateResponseMixin, ContextMixin, View):
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
                'Course':Course.objects.all(),
                'Document':Document.objects.all(),
                'User':User.objects.all()}
        )
        return self.render_to_response(context)

def view(request, course_id):
    current_course= Course.objects.filter(pk=course_id).get()
    participants = []
    users = Person.objects.all()
    #for user in users:
     #   if user.objects.filter(user__course__course_code__icontains=current_course.course_code):
      #      participants.append(user)

    return render(request, 'courses/course_template.html',
                  {'current_course':current_course,
                   'participants':participants,
                   'Course':Course.objects.all()
                  })